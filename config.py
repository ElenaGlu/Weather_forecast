import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_KEY_WEATHER = os.getenv('API_KEY_WEATHER')
DJANGO_KEY = os.getenv('DJANGO_KEY')
