import requests
from dotenv import load_dotenv
import json
import os

# Load in the environment variables and then extract our OpenAI API key from it
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_KEY')


# Set up the headers which are needed for the request
headers = {
    'Authorization': f"Bearer {OPENAI_API_KEY}",
    'Content-Type': 'application/json', # Request JSON to be returned as it is nice in our use-case
    'model': 'gpt-3.5-turbo', # Specify the model we want to use, this is currently the most performant one offered
}

def get_response(USER_QUERY):
    # Set up the request body
    data = {
        'messages': [
            {"role": "system", "content": "You are a helpful assistant."}, # Need to give the AI model some context to work with
            {"role": "user", "content": f'{USER_QUERY}'} # Feed it the query/question provided by the user
        ],
        'max_tokens': 500, # Specify the tokens, this limits quantity of response obtained from the model (This is quite a generous number of tokens)
        'model': 'gpt-3.5-turbo'
    }

    # Make the call to the API endpoint
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers,
        json=data,
        timeout = 30 # Timeout is overidden and specified to be 30 seconds, this is because  API calls to OpenAI services can take a while
    )

    # If the response is 200, its successful, so extract the reply from the response and return it
    if response.status_code == 200:
        response = response.json()['choices'][0]['message']['content'].strip()
        return response

    # If we reach here this means something went wrong, in that case return an error message
    else:
        error_message = f'Failed to obtain a response from the API\nStatus code: {response.status_code}\n{response.text}'
        return error_message
