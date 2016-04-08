import os

import dotenv
import requests


DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(DOTENV_PATH):
    dotenv.load_dotenv(DOTENV_PATH)


NBG_PRIMARY_KEY = os.getenv('NBG_PRIMARY_KEY')
NBG_SECONDARY_KEY = os.getenv('NBG_SECONDARY_KEY')
NBG_API_HOST = os.getenv('NBG_API_HOST', 'https://nbgdemo.azure-api.net/echo')
NBG_RESOURCE_URL = '%s/resource' % NBG_API_HOST

DEFAULT_HEADERS = {
    'Ocp-Apim-Subscription-Key': NBG_SECONDARY_KEY,
    'Content-Type': 'application/json'
}


def create_resource(data={}):
    response = requests.post(
        NBG_RESOURCE_URL, headers=DEFAULT_HEADERS, json=data
    )
    return response


def modify_resource(data={}):
    response = requests.put(
        NBG_RESOURCE_URL, headers=DEFAULT_HEADERS, json=data
    )
    return response


def remove_resource(data={}):
    response = requests.delete(
        NBG_RESOURCE_URL, headers=DEFAULT_HEADERS, json=data
    )
    return response


def retrieve_resource_headers(data={}):
    response = requests.head(
        NBG_RESOURCE_URL, headers=DEFAULT_HEADERS, json=data
    )
    return response


def retrieve_resource(data={}):
    response = requests.get(
        NBG_RESOURCE_URL, headers=DEFAULT_HEADERS, params=data
    )
    return response


def retrieve_resource_cached(data={}):
    url = '%s-cached' % NBG_RESOURCE_URL
    response = requests.get(
        url, headers=DEFAULT_HEADERS, params=data
    )
    return response
