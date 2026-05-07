from enum import Enum
from pydantic import BaseModel

class GenreURLChoices(Enum):
    Rock = "rock"
    Electronic = "electronic"
    Metal = "metal"
    Hip_Hop = "hip-hop"

class Band(BaseModel):
    id: int
    name: str
    genre: str