from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import aiohttp
import string
import random

app = FastAPI()

url_storage = {}


class UrlRequest(BaseModel):
    url: str


def generate_short_id(length=6):
    """Генерация случайного идентификатора"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


@app.get("/async")
async def async_request():
    """Асинхронный запрос к внешнему API"""
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            data = await response.json()
    return data


@app.post("/", status_code=201)
async def shorten_url(request: UrlRequest):
    """Сокращение URL"""
    short_id = generate_short_id()
    url_storage[short_id] = request.url
    return {"short_url": f"http://127.0.0.1:8080/{short_id}"}


@app.get("/{short_id}")
async def redirect_to_url(short_id: str):
    """Редирект по короткому URL"""
    if short_id not in url_storage:
        raise HTTPException(status_code=404, detail="Short URL not found")
    original_url = url_storage[short_id]
    return RedirectResponse(original_url, status_code=307)
