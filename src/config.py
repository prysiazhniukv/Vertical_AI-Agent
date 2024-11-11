import os
import yaml
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Load sensitive data from .env
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Load system messages from YAML
    @staticmethod
    def load_system_message() -> str:
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'system_message.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config['system_message']
    
    SYSTEM_MESSAGE = load_system_message()