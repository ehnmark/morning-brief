import logging
from agent_framework.azure import AzureAIAgentClient
from http_utils import retrieve_rss_text_items
from typing_extensions import Never
from pydantic import BaseModel
from agent_framework import (
    AgentExecutor,
    AgentExecutorRequest,
    AgentExecutorResponse,
    ChatAgent,
    ChatMessage,
    Role,
    WorkflowBuilder,
    WorkflowContext,
    executor,
    ai_function
)

class RelevantLink(BaseModel):
    url: str
    title: str
    excerpt: str

class RelevantLinks(BaseModel):
    items: list[RelevantLink]

class WorkflowInput(BaseModel):
    config: dict

@executor()
async def collater(responses: list[AgentExecutorResponse], ctx: WorkflowContext[ChatMessage, str]) -> None:
    prompt = "Use the following data for the report as per the instructions. Ensure all links in the final report are formatted as Markdown links [Title](URL):\n\n"
    for response in responses:
        links = RelevantLinks.model_validate_json(response.agent_run_response.text)
        for link in links.items:
            prompt += f"- {link.title}: {link.url}\n{link.excerpt}\n\n"
    request = AgentExecutorRequest(messages=[ChatMessage(Role.USER, text=prompt)], should_respond=True)
    await ctx.send_message(request)

@executor()
async def report_writer(response: AgentExecutorResponse, ctx: WorkflowContext[Never, str]) -> None:
    text = response.agent_run_response.text
    await ctx.yield_output(text)

@executor()
async def dispatcher(input: WorkflowInput, ctx: WorkflowContext[ChatMessage]):
    prompt = f"Retrieve data relevant to a morning brief on Japanese equities for the date {input.config['date']}"
    request = AgentExecutorRequest(messages=[ChatMessage(Role.USER, text=prompt)], should_respond=True)
    await ctx.send_message(request)

@ai_function(name="rss_tool")
async def rss_tool(url: str) -> str:
    logging.info(f"Fetching RSS from {url}")
    return await retrieve_rss_text_items(url, max_items=5)

async def create_retrieval_executors(config, stack, credential):
    retrieval_executors = []
    for name, url in config["urls"].items():
        agent = await stack.enter_async_context(
            ChatAgent(
                chat_client=AzureAIAgentClient(async_credential=credential),
                instructions=config["instructions"]["retrieval_agents"].format(url=url),
                response_format=RelevantLinks,
                tools=[rss_tool],
            )
        )
        executor = AgentExecutor(agent, id=f"{name}_executor")
        retrieval_executors.append(executor)
    return retrieval_executors

async def create_reporting_executor(config, stack, credential):
    reporting_chat_agent = await stack.enter_async_context(
        ChatAgent(
            chat_client=AzureAIAgentClient(async_credential=credential),
            instructions=config["instructions"]["reporting_agent"],
        )
    )
    return AgentExecutor(reporting_chat_agent, id="reporting_executor")

async def build_workflow(config, stack, credential):
    retrieval_executors = await create_retrieval_executors(config, stack, credential)
    reporting_executor = await create_reporting_executor(config, stack, credential)

    # Workflow definition
    workflow = (
        WorkflowBuilder()
        .set_start_executor(dispatcher)
        .add_fan_out_edges(dispatcher, retrieval_executors)
        .add_fan_in_edges(retrieval_executors, collater)
        .add_edge(collater, reporting_executor)
        .add_edge(reporting_executor, report_writer)
        .build()
    )
    return workflow
