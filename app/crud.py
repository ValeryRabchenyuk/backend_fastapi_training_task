from sqlalchemy.orm import Session
from . import models, schemas
from .config import settings
import string
import random


def generate_short_id(length=6):
    """Генерация случайного идентификатора"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def create_url(db: Session, url: schemas.URLCreate) -> schemas.URLInfo:
    short_id = generate_short_id()
    db_url = models.URL(original_url=url.url, short_id=short_id)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return schemas.URLInfo(
        short_id=db_url.short_id,
        short_link=f"{settings.BASE_URL}/{db_url.short_id}",
        original_url=db_url.original_url
    )


def get_url(db: Session, short_id: str):
    return db.query(models.URL).filter(models.URL.short_id == short_id).first()
