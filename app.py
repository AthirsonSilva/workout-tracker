import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_ID = os.getenv('API_ID')
TOKEN = os.getenv('TOKEN')
NUTRITIONIX_ENDPOINT = os.getenv('NUTRITIONIX_ENDPOINT')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
GENDER = os.getenv('GENDER')
WEIGHT_KG = os.getenv('WEIGHT_KG')
HEIGHT_CM = os.getenv('HEIGHT_CM')
AGE = os.getenv('AGE')

exercise_text = input('Which exercised you did today: ')

exercise_headers = {
    "Authorization": f'Bearer {TOKEN}',
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

exercise_params = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

exercise_response = requests.post(url=NUTRITIONIX_ENDPOINT,
                                  json=exercise_params, headers=exercise_headers)
exercise_data = exercise_response.json()
print(exercise_data)

today = datetime.now()
formatted_date = today.strftime('%d/%m/%Y')
formatted_hour = today.strftime('%X')
print(formatted_date, formatted_hour)

for exercise in exercise_data['exercises']:
    sheet_input = {
        'workout': {
            'date': formatted_date,
            'time': formatted_hour,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }


sheet_response = requests.post(
    url=SHEETY_ENDPOINT, json=sheet_input)
sheet_data = sheet_response.json()
print(sheet_response)
