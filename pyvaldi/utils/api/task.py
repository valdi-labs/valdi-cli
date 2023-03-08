import requests
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('BASE_URL')


def account_tasks(access_token):
    response = requests.request(method='GET',
                                url=f'{base_url}/account/tasks?task_type=container',
                                headers={'Authorization': f'Bearer {access_token}'}
                                )

    return response


def account_tasks_task(access_token, task_id):
    response = requests.request(method='GET',
                                url=f'{base_url}/account/tasks/{task_id}?include_container_output=true',
                                headers={'Authorization': f'Bearer {access_token}'}
                                )

    return response
