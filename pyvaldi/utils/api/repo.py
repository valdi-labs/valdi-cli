import requests
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('BASE_URL')


def account_repositories(access_token):
    response = requests.request(method='GET',
                                url=f'{base_url}/account/repositories',
                                headers={'Authorization': f'Bearer {access_token}'}
                                )

    return response
