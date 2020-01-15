import json

from settings.json_encoder import JSONEncoderWithoutModificator


class User(object):
    def __init__(self, username, password):
        if username:
            self._username = username
        if password:
            self._password = password

    def get_headers(self, token):
        return {
            'Authorization': f'token {token}',
            'Content-Type': 'application/json'
        }

    @property
    def credential(self):
        return json.dumps(self, cls=JSONEncoderWithoutModificator)
