from pyvaldi.utils.AuthorizationClient import AuthorizationClient
from pyvaldi.utils.api.task import account_tasks, account_tasks_task
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

    def get_task(self, task_id):
        response = account_tasks_task(self.access_token, task_id)
        if response.ok:
            r = json.loads(response.text)
            del r['task_type'], \
                r['description'], \
                r['nodes_count'], \
                r['parameters'], \
                r['epochs'], \
                r['containers'][0]['name'], \
                r['containers'][0]['checksum'], \
                r['containers'][0]['duration'], \
                r['worker_devices'][0]['task_status'], \
                r['worker_devices'][0]['updated_at']
            print(json.dumps(r, indent=4))
        else:
            print(f'[HTTP {response.status_code}] {json.loads(response.text)["detail"]}')
