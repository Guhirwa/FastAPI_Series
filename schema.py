from datetime import date
from enum import Enum
from pydantic import BaseModel

class GenreURLChoices(Enum):
    Rock = "rock"
    Electronic = "electronic"
    Metal = "metal"
    Hip_Hop = "hip-hop"

class Album(BaseModel):
    title: str
    release_date: date

class BandBase(BaseModel):
    name: str
    genre: str
    albums: list[Album] = []

class BandCreate(BandBase):
    pass

class BandWithID(BandCreate):
    id: int
