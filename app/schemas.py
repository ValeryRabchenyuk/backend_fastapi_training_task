from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    url: HttpUrl


class URLInfo(BaseModel):
    short_id: str
    short_link: str
    original_url: str

    class Config:
        orm_mode = True
