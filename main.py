from fastapi import FastAPI, HTTPException

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

@app.get("/bands/{band_id}")
async def band(band_id: int) -> dict:

    # for existing_band in BANDS:
    #     if existing_band["id"] == band_id:
    #         return existing_band
    # raise HTTPException(status_code=404, detail="Band not found")

    existing_band = next((b for b in BANDS if b["id"] == band_id), None)
    if existing_band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return existing_band