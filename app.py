import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_ID = os.getenv('API_ID')
print(API_ID)
print(API_KEY)
