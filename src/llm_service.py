from openai import OpenAI
from config import Config
from typing import Optional

class LLMService:
    def __init__(self, system_msg: Optional[str] = Config.SYSTEM_MESSAGE) -> None:
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.system_message = system_msg
    
    async def get_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content