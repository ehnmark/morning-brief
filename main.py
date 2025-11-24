import asyncio
import logging
from contextlib import AsyncExitStack
from azure.identity.aio import AzureCliCredential
from agent_framework import WorkflowOutputEvent
from workflow import build_workflow, WorkflowInput
from config import get_config

async def main(config):
    async with AsyncExitStack() as stack:
        credential = await stack.enter_async_context(AzureCliCredential())        
        workflow = await build_workflow(config, stack, credential)

        # Run workflow
        input = WorkflowInput(config=config)
        async for event in workflow.run_stream(input):
            logging.debug(event)
            if isinstance(event, WorkflowOutputEvent):
                print(event.data)

if __name__ == "__main__":
    config = get_config()
    asyncio.run(main(config))