import re
import json 
from anthropic import Anthropic
from config.config import ANTHROPIC_API_KEY

class AnthropicService: 
    def __init__(self): 
        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
    
    def classify(self, prompt: str): 
        try:
            response = self.client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=1024,
                temperature=0,
                messages=[{"role": "user", "content": prompt}]
            )

            text = response.content[0].text 
            match = re.search(r"\{.*\}", text, re.DOTALL)

            if not match:
                raise ValueError("no JSON found in claude response")

            return json.loads(match.group())

        except Exception as e: 
            return {
                "match": False,
                "score": 0,
                "confidence": 0,
                "language": "unknown",
                "orientation": "unknown",
                "content_niche": "unknown",
                "matched_keywords": [],
                "reason": str(e)
            }
    