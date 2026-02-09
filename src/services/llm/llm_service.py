import requests
from src.config.config import Config

class LLMService:
    def __init__(self):
        self.model = Config.AI_MODEL
        self.url = "http://localhost:11434/api/generate"

    def analyze_5w2h(self, title, description):
        # 1. We remove the pre-filled "WHY" so the AI doesn't choke.
        prompt = f"""### Instruction:
You are a Project Manager. Analyze the Input and write a 5W2H checklist.
Required format:
- WHAT: (The task)
- WHY: (The benefit)
- WHERE: (The location)
- WHEN: (The deadline)
- WHO: (The responsible)
- HOW: (The method)
- HOW MUCH: (The cost/effort)

### Input:
Task: {title}
Context: {description}

### Response:
"""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.3, # A bit more creativity to ensure it writes SOMETHING
                "num_ctx": 2048,
                "stop": ["###", "Input:"] 
            }
        }

        try:
            r = requests.post(self.url, json=payload, timeout=90)
            
            if r.status_code == 200:
                text = r.json().get("response", "").strip()
                if not text:
                    return "⚠️ The AI returned an empty response. Try adding more description to the card."
                return text
            
            return f"❌ Ollama Error: {r.status_code}"

        except Exception as e:
            return f"❌ Connection Error: {str(e)}"