import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class Config:
    API_KEY = os.getenv("TRELLO_API_KEY")
    TOKEN = os.getenv("TRELLO_TOKEN")
    BOARD_ID = os.getenv("TRELLO_BOARD_ID")
    BASE_URL = "https://api.trello.com/1"
    AI_MODEL = os.getenv("AI_MODEL", "tinyllama")

    @staticmethod
    def validate():
        if not all([Config.API_KEY, Config.TOKEN]):
            raise ValueError("❌ Missing Trello API Key or Token in .env file.")

# Validate immediately upon import
Config.validate()