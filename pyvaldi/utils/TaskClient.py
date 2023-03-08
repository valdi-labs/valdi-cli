from pyvaldi.utils.AuthorizationClient import AuthorizationClient
from pyvaldi.utils.api.task import account_tasks
import json


class TaskClient(AuthorizationClient):
    def get_tasks(self):
        response = account_tasks(self.access_token)
        if response.ok:
            parsed_tasks = []
            for task in json.loads(response.text)['items']:
                parsed_tasks.append({
                    'task_id': task['task_id'],
                    'name': task['name'],
                    'created': task['created'],  # TODO Reformat timestamp to human readable format
                    'status': task['status']
                })
            print(json.dumps(parsed_tasks, indent=4))
        else:
            print(f'[HTTP {response.status_code}] {json.loads(response.text)["detail"]}')