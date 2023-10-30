import requests
from dotenv import load_dotenv
import os


load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_KEY')

headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
    'Content-Type': 'application/json',
}

def get_image(PROMPT):
    data = {
        'prompt': PROMPT,
        'n': 1,
        'size': '1024x1024',
        'model': 'image-alpha-001'
    }

    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers=headers,
        json = data,
        timeout = 30
    )

    if response.status_code == 200:
        image_url = response.json()['data'][0]['url']
        return image_url
    else:
        error_message = f'Ooops... something went wrong'
        return error_message



