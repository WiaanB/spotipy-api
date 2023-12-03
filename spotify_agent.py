import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = 'user-read-private user-read-email user-library-read user-library-modify user-read-recently-played playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private'

def create_spotify_instance() -> spotipy.Spotify:
    auth_manager = SpotifyOAuth(client_id=os.getenv("client_id"),
                                               client_secret= os.getenv("client_secret"),
                                               redirect_uri=os.getenv("redirect_url"),
                                               scope=scope)
    return spotipy.Spotify(auth_manager=auth_manager)
