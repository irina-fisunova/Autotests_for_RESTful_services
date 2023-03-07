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

    def post_api_create_pet_simple(self, api_key, create_pet_data):
        create_pet_simple = '/api/create_pet_simple'
        url = base_url + create_pet_simple

        create_pet_simple_headars = {
            'auth_key': api_key,
        }



        create_pet_simple_res = requests.post(url, headers=create_pet_simple_headars, data=create_pet_data)

        return {
            'status': create_pet_simple_res.status_code,
            'result': create_pet_simple_res.json(),
        }

    # def post_api_pets(self, api_key, create_pet_data, pet_photo_path):
    #     api_pets = '/api/pets'
    #     url = base_url + api_pets
    #
    #     api_pets_headars = {
    #         'accept': 'application/json',
    #         'Content-Type': 'multipart/form-data',
    #         'auth_key': api_key,
    #     }
    #
    #     # file = {'pet_photo': open(pet_photo_path, 'rb')}
    #     create_pet_data['pet_photo'] = open(pet_photo_path, 'rb')
    #     # print()
    #     # print(file)
    #
    #     api_pets_res = requests.post(url, headers=api_pets_headars, data=create_pet_data)
    #     print()
    #     print("api_pets_res: ")
    #     print(api_pets_res)
    #
    #     return {
    #         'status': api_pets_res.status_code,
    #         'result': api_pets_res,
    #     }

    def delete_api_pets_pet_id(self, api_key, pet_id):
        api_pets_pet_id = f'/api/pets/{pet_id}'
        url = base_url + api_pets_pet_id

        api_pets_pet_id_headars = {
            'auth_key': api_key,
        }

        api_pets_pet_id_res = requests.delete(url, headers=api_pets_pet_id_headars)

        return {
            'status': api_pets_pet_id_res.status_code,
        }