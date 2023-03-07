import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('BASE_URL')


def account_login(email, password):
    response = requests.request(method='POST',
                                url=f'{base_url}/account/login',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps({'email': email, 'password': password})
                                )

    return response


def refresh_access_token(refresh_token):
    response = requests.request(method='POST',
                                url=f'{base_url}/account/refresh_token',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps({'token': refresh_token})
                                )

    return response
