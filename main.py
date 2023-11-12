from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import spotify_agent

origins = [
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8000",
]

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}

# User Routes
@app.get("/me")
def get_user():
    sp = spotify_agent.create_spotify_instance("user-read-private")
    results = sp.me()
    return {**results}
@app.get("/get/{username}/recently_played")
def get_recently_played(username: str):
    sp = spotify_agent.create_spotify_instance("user-read-recently-played")
    results = sp.current_user_recently_played()
    return {**results}
