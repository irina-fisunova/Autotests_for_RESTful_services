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

    def get_api_all_pets (self, api_key, filter='my_pets'):
        all_pets_api = '/api/pets'
        url = base_url + all_pets_api

        all_pets_headars = {
            'accept': 'application/json',
            'auth_key': api_key,
        }

        all_pets_params = {
            'filter': filter,
        }

        all_pets_res = requests.get(url, headers=all_pets_headars, params=all_pets_params)

        return {
            'status': all_pets_res.status_code,
            'result': all_pets_res.json(),
        }