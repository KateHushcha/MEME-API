from pydantic import BaseModel
import datetime


class MemeInfo(BaseModel):
    description: str
    author: str
    date: datetime.date


class MemeData(BaseModel):
    text: str
    url: str
    tags: list
    info: MemeInfo


class DeletedMeme(BaseModel):
    message: str
