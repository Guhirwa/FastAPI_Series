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
async def bands(
        genre: GenreURLChoices | None = None,
        has_album: bool | None = None
) -> list[Band]:
    band_list = [Band(**b) for b in BANDS]

    if genre:
        band_list = [
            b for b in band_list if b.genre.lower() == genre.value
        ]
    if has_album is True:
        band_list = [
            b for b in band_list if len(b.albums) > 0
    ]
    elif has_album is False:
        band_list = [
            b for b in band_list if len(b.albums) == 0
        ]
    return band_list


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