from fastapi import APIRouter
import spotify_agent

router = APIRouter()

@router.get("/me")
def get_user():
    sp = spotify_agent.create_spotify_instance()
    results = sp.me()
    return {**results}

@router.get("/me/recently_played")
def get_recently_played():
    sp = spotify_agent.create_spotify_instance()
    results = sp.current_user_recently_played()
    return {**results}