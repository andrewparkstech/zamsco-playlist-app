from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SPOTIFY_API_TOKEN = os.getenv('SPOTIFY_API_TOKEN')
    APPLE_MUSIC_API_TOKEN = os.getenv('APPLE_MUSIC_API_TOKEN')
