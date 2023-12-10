from fastapi import APIRouter
import spotify_agent
from pydantic import BaseModel

router = APIRouter()

class PlaylistSearchBody(BaseModel):
    id: list[str]

class PlaylistGenerateBody(BaseModel):
    artists: list[str] | None = None
    genres: list[str] | None = None

@router.post("/get")
def get_user(search_body: PlaylistSearchBody):
    sp = spotify_agent.create_spotify_instance()
    results = []
    for id in search_body.id:
        results.append(sp.playlist(id))
    return {"data": results}

@router.post('/generate')
def generate_playlist(generate_body: PlaylistGenerateBody | None = None):
    sp = spotify_agent.create_spotify_instance()
    results = sp.recommendations(seed_artists=generate_body.artists, seed_genres=generate_body.genres)
    return {"data": results}