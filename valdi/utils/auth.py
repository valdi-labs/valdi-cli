from getpass import getpass
from pathlib import Path
import valdi.utils.api.auth as auth
import json
import os

credential_loc = os.path.dirname(os.path.realpath(__file__)) + '/../../.valdi'
credential_file = 'token'


class AuthorizationClient:
    def __init__(self):
        self.refresh_token = None
        self.access_token = None

        try:
            with open(f'{credential_loc}/{credential_file}', 'r') as f:
                self.refresh_token = f.read()
                self.refresh_access_token()
        except:
            email = input('Account email: ')
            password = getpass()
            if self.login(email, password):
                try:
                    with open(f'{credential_loc}/{credential_file}', 'w') as f:
                        f.write(self.refresh_token)
                    print('Successfully configured.')
                except (FileNotFoundError, IOError) as e:
                    print(f'Error storing credentials: {e}')

    def login(self, email, password):
        response = auth.account_login(email, password)

        if response.ok:
            json_resp = json.loads(response.text)
            self.refresh_token = json_resp['refresh_token']
            self.access_token = json_resp['access_token']
            return True
        else:
            print(f'[HTTP {response.status_code}] {json.loads(response.text)["detail"]}')
            return False

    def refresh_access_token(self):
        response = auth.refresh_access_token(self.refresh_token)

        if response.ok:
            json_resp = json.loads(response.text)
            self.access_token = json_resp['access_token']
        else:
            print(f'[HTTP {response.status_code}] {json.loads(response.text)["detail"]}')
