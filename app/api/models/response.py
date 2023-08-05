from typing import List
from pydantic import BaseModel


class EntityOut(BaseModel):
    start: int
    end: int
    type: str
    text: str


class EntitiesOut(BaseModel):
    entities: List[EntityOut]
    anonymized_text: str
