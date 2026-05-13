from datetime import date
from enum import Enum
from pydantic import BaseModel, field_validator


class GenreChoices(Enum):
    Rock = "Rock"
    Electronic = "Electronic"
    Metal = "Metal"
    Hip_Hop = "Hip-Hop"

class Album(BaseModel):
    title: str
    release_date: date

class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Album] = []

class BandCreate(BandBase):
    @field_validator("genre", mode="before")
    @classmethod
    def title_case_genre(cls, value):
        if isinstance(value, str):
            return value.title()
        return value

class BandWithID(BandCreate):
    id: int
