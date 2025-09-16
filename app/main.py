from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import models, schemas, crud, utils
from .database import engine, get_db
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)


@app.post("/", response_model=schemas.URLInfo, status_code=201)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db, url)


@app.get("/async")
async def async_request():
    return await utils.fetch_json()


@app.get("/{short_id}")
def redirect_url(short_id: str, db: Session = Depends(get_db)):
    db_url = crud.get_url(db, short_id)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(db_url.original_url, status_code=307)
