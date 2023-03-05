import json
import requests
from settings import base_url
class PetsApi:
    def get_api_key (self, email: str, password: str) -> json:

        key_api = "/api/key"
        key_headers = {
            'accept': 'application/json',
            'email': email,
            "password": password,
        }

        url = base_url + key_api
        key_res = requests.get(f"{url}", headers=key_headers)

        return {
            'status': key_res.status_code,
            'result': key_res.json(),
        }
