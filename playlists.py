from fastapi import APIRouter
import spotify_agent
from pydantic import BaseModel

router = APIRouter()

class PlaylistSearchBody(BaseModel):
    id: list[str]

@router.post("/get")
def get_user(search_body: PlaylistSearchBody):
    sp = spotify_agent.create_spotify_instance()
    results = []
    for id in search_body.id:
        results.append(sp.playlist(id))
    return {"data": results}