import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

def create_spotify_instance(scope: str) -> spotipy.Spotify:
    auth_manager = SpotifyOAuth(client_id=os.getenv("client_id"),
                                               client_secret= os.getenv("client_secret"),
                                               redirect_uri=os.getenv("redirect_url"),
                                               scope=scope)
    return spotipy.Spotify(auth_manager=auth_manager)
