from fastapi import FastAPI

app = FastAPI()

BANDS = [
    {"id":1, "name": "The Kinks", "genre": "Rock"},
    {"id":2, "name": "The Aphex Twin", "genre": "Electronic"},
    {"id":3, "name": "Slowdive", "genre": "Shoegaz"},
    {"id":4, "name": "Wu-Tang Clan", "genre": "Hip-Hop"},
]

@app.get("/bands")
async def bands() -> list[dict]:
    return BANDS

@app.get("/about")
async def about() -> str:
    return "An Exceptional Company"