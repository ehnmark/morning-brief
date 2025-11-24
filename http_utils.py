import httpx
import feedparser
import logging
import asyncio

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()
        return response.text

async def fetch_and_parse_rss(url: str) -> list[tuple[str, str, str]]:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        results = []
        for entry in feed.entries:
            title = entry.get("title", "")
            pub_date = entry.get("published", entry.get("pubDate", ""))
            link = entry.get("link", "")
            results.append((title, pub_date, link))
        return results

async def is_text_content(url: str) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.head(url, follow_redirects=True, timeout=10.0)
            content_type = response.headers.get("content-type", "").lower()
            return "text" in content_type or "json" in content_type or "xml" in content_type
    except Exception:
        return False

async def retrieve_rss_text_items(url: str, max_items: int, max_len: int = 10000) -> str:
    items = await fetch_and_parse_rss(url)
    
    filtered_items = []
    for item in items:
        if len(filtered_items) >= max_items:
            break
        
        link = item[2]
        if await is_text_content(link):
            filtered_items.append(item)

    for item in filtered_items:
        logging.info(f"Will fetch {item[2]}")
    
    async def fetch_item(item):
        title, pub_date, link = item
        try:
            content = await fetch_url(link)
            if len(content) > max_len:
                content = content[:max_len] + "...(truncated)"
            return f"Title: {title}\nDate: {pub_date}\nLink: {link}\nContent:\n---\n{content}\n---"
        except Exception as e:
            logging.error(f"Failed to fetch {link}: {e}")
            return ""

    tasks = [fetch_item(item) for item in filtered_items]
    results = await asyncio.gather(*tasks)
    parts = [r for r in results if r]
    
    return "\n\n".join(parts)
