import requests
from dotenv import load_dotenv
import os


# Load the env and extract the OpenAI API key
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_KEY')

# Set up the headers which will include the API key and specify the content type we want returned (json works in our case)
headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
    'Content-Type': 'application/json',
}

def get_image(PROMPT):
    """
    Method which calls the DALL E API, it gives it a description and retrieves an image back that is generated
    based on the description. This prompt is the prompt obtained from the user in some server.
    :param PROMPT: Prompt which the user provides, this is what the image is generated upon
    :return: Global image URL if retrieved successfuly, otherwise an error message if something went wrong
    """
    # Set up the parameters which need to be passed in the request
    data = {
        'prompt': PROMPT, # User prompt
        'n': 1, # Number of images to generate based on given prompt
        'size': '1024x1024', # Resolution of the generated image
        'model': 'image-alpha-001' # Model of the AI service we are using
    }

    # Set up a request to the given endpoint
    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers=headers, # Specify headers which we made earelier
        json = data,
        timeout = 30 # Timeout was manually overidden to avoid premature timeouts as this call can take a while
    )

    # If the response code is 200 (successful) extract the image URL and return it
    if response.status_code == 200:
        image_url = response.json()['data'][0]['url']
        return image_url
    # If the response code is not 200 then something must be wrong, tell user and rturn back an error message
    else:
        error_message = f'Ooops... something went wrong'
        return error_message



