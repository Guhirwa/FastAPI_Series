from datetime import date
from enum import Enum
from pydantic import BaseModel

class GenreURLChoices(Enum):
    Rock = "rock"
    Electronic = "electronic"
    Metal = "metal"
    Hip_Hop = "hip-hop"

class BandBase(BaseModel):
    name: str
    genre: str
    albums: list[Album] = []

class Album(BaseModel):
    title: str
    release_date: date