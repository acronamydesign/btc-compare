import os
from pathlib import Path

class AuthManager:
    def __init__(self):
        self.home = str(Path().home())

    def load_credentials(self):
        api_key = ''
        sec = ''
        if os.path.exists(self.home + '\credentials.txt'):
            with open(self.home + '\credentials.txt', 'r') as fo:
                for line in fo:
                    line = line.strip()
                    if line.startswith('api '):
                        api_key = line.replace('api ', '')
                    if line.startswith('sec '):
                        sec = line.replace('sec ', '')
            return {'api':api_key,'secret':sec}
        else:
            return False

    def create_credentials(self):
        if not os.path.exists(self.home + '\credentials.txt'):
            api_key = input("api key: ")
            secret = input("api secret: ")
            with open(self.home + '\credentials.txt','w') as f:
                f.write('api ' + api_key + "\n" + 'sec ' + secret )

    def delete_credentials(self):
        if os.path.exists(self.home + '\credentials.txt'):
            os.remove(self.home + '\credentials.txt')



    def authenticate(self):
        credentials = self.load_credentials()
        if not credentials:
            self.create_credentials()
            return self.load_credentials()
        else:
            return credentials