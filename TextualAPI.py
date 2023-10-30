import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_KEY')


headers = {
    'Authorization': f"Bearer {OPENAI_API_KEY}",
    'Content-Type': 'application/json',
    'model': 'gpt-3.5-turbo',
}

def get_response(USER_QUERY):
    data = {
        'messages': [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'{USER_QUERY}'}
        ],
        'max_tokens': 500,
        'model': 'gpt-3.5-turbo'
    }

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers,
        json=data,
        timeout = 30
    )

    if response.status_code == 200:
        response = response.json()['choices'][0]['message']['content'].strip()
        return response

    else:
        error_message = f'Failed to obtain a response from the API\nStatus code: {response.status_code}\n{response.text}'
        return error_message
