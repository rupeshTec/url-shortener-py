from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from shortener import URLShortener

app = FastAPI()
shortener = URLShortener()

class URLRequest(BaseModel):
    url: HttpUrl

@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_code = shortener.shorten(request.url)
    return {"short_url": f"http://shorty.in/{short_code}"}

@app.get("/{short_code}")
def resolve_url(short_code: str):
    original_url = shortener.resolve(short_code)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": original_url}
