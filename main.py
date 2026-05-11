from fastapi import FastAPI, HTTPException
from schema import GenreURLChoices, Band

app = FastAPI()

BANDS = [
    {"id":1, "name": "The Kinks", "genre": "Rock"},
    {"id":2, "name": "Aphex Twin", "genre": "Electronic"},
    {"id":3, "name": "Black Sabbath", "genre": "Metal", "albums": [
        {"title": "Master of Reality", "release_date": "1971-07-21"},
    ]},
    {"id":4, "name": "Wu-Tang Clan", "genre": "Hip-Hop"},
]

@app.get("/bands")
async def bands() -> list[Band]:
    return [
        Band(**b) for b in BANDS
    ]

@app.get("/bands/{band_id}", status_code=200)
async def band(band_id: int) -> Band:

    # for existing_band in BANDS:
    #     if existing_band["id"] == band_id:
    #         return Band(**existing_band)
    # raise HTTPException(status_code=404, detail="Band not found")

    existing_band = next((Band(**b) for b in BANDS if b["id"] == band_id), None)
    if existing_band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return existing_band

@app.get("/band/genre/{genre}")
async def band_for_genre(genre: GenreURLChoices) -> list[Band]:
    return [
        Band(**b) for b in BANDS if b["genre"].lower() == genre.value
    ]