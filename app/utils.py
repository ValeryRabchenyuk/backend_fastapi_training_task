import aiohttp


async def fetch_json():
    """Асинхронный запрос к тестовому API."""
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as resp:
            return await resp.json()
