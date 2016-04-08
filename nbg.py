import json
import os

import dotenv
import requests


DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(DOTENV_PATH):
    dotenv.load_dotenv(DOTENV_PATH)


NBG_PRIMARY_KEY = os.getenv('NBG_PRIMARY_KEY')
NBG_SECONDARY_KEY = os.getenv('NBG_SECONDARY_KEY')
NBG_API_HOST = os.getenv('NBG_API_HOST', 'https://nbgdemo.azure-api.net/echo')

DEFAULT_HEADERS = {
    'Ocp-Apim-Subscription-Key': NBG_SECONDARY_KEY,
    'Content-Type': 'application/json'
}


def create_resource(data):
    url = '%s/resource' % NBG_API_HOST
    body = data

    if isinstance(body, dict):
        body = json.dumps(body)

    response = requests.post(url, headers=DEFAULT_HEADERS, data=body)
    return response
