import requests
from src.config.config import Config

class TrelloService:
    def __init__(self):
        self.auth = {"key": Config.API_KEY, "token": Config.TOKEN}

    def get_card_data(self, card_id_or_url):
        # Clean ID logic
        card_id = card_id_or_url.split("/")[-1] if "/" in card_id_or_url else card_id_or_url
        
        url = f"{Config.BASE_URL}/cards/{card_id}"
        try:
            r = requests.get(url, params=self.auth, timeout=10)
            r.raise_for_status()
            data = r.json()
            return {"name": data.get("name"), "desc": data.get("desc", "")}
        except Exception as e:
            return {"error": f"Trello Error: {str(e)}"}