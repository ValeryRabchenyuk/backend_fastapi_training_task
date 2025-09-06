## AVB DEV
### Task for Python Developers
---

### Run the Service

Install dependencies:

```bash
pip install fastapi uvicorn aiohttp
```
### Run the server:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8080
```

### The service will be available at:
👉 http://127.0.0.1:8080
---

### Endpoints
1. Shorten URL

POST /

Create a short link for a given URL.
```bash
curl -X POST "http://127.0.0.1:8080/" \
     -H "Content-Type: application/json" \
     -d '{"url":"https://example.com/long/page"}'
```

Example response: {"short_url":"http://127.0.0.1:8080/a1B9xZ"}

2. Redirect to Original URL

GET /{short_id}

Open the shortened URL in your browser, or test with curl:

```bash
curl -v http://127.0.0.1:8080/a1B9xZ
```

Expected response:

HTTP/1.1 307 Temporary Redirect
Location: https://example.com/long/page

3. Async External Request

GET /async

Makes an async request to a test API and returns JSON data.

```bash
curl http://127.0.0.1:8080/async
```

Example response:

{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
---

### Interactive Docs

Swagger UI is available at:
http://127.0.0.1:8080/docs
