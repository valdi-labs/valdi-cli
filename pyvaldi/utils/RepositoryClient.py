from pyvaldi.utils.AuthorizationClient import AuthorizationClient
from pyvaldi.utils.api.repo import account_repositories
import json


class RepositoryClient(AuthorizationClient):
    def get_repositories(self):
        response = account_repositories(self.access_token)
        if response.ok:
            print(json.dumps(json.loads(response.text)['items'], indent=4))
            # TODO Consider parsing output like with tasks
        else:
            print(f'[HTTP {response.status_code}] {json.loads(response.text)["detail"]}')
