import pytest
from api import PetsApi
from settings import valid_email, valid_password, create_pet_data, pet_photo
class TestPetsApi:
    def setup(self):
        self.pets_api = PetsApi

    def test_get_api_key(self):
        response_data = self.pets_api.get_api_key(self, email=valid_email, password=valid_password)

        assert response_data['status'] == 200
        assert 'key' in response_data['result']

    def test_get_api_all_pets(self):
        response_api_key = self.pets_api.get_api_key(self, email=valid_email, password=valid_password)
        api_key = response_api_key['result']['key']
        response_data = self.pets_api.get_api_all_pets(self, api_key)

        assert response_data['status'] == 200
        assert 'pets' in response_data['result']
        assert type(response_data['result']['pets']) is list

    def test_post_api_create_pet_simple(self):
        response_api_key = self.pets_api.get_api_key(self, email=valid_email, password=valid_password)
        api_key = response_api_key['result']['key']
        response_data = self.pets_api.post_api_create_pet_simple(self, api_key, create_pet_data)

        assert response_data['status'] == 200
        assert 'age' in response_data['result']
        assert create_pet_data['age'] == int(response_data['result']['age'])
        assert 'animal_type' in response_data['result']
        assert create_pet_data['animal_type'] == response_data['result']['animal_type']
        assert 'created_at' in response_data['result']
        assert 'id' in response_data['result']
        assert 'name' in response_data['result']
        assert create_pet_data['name'] == response_data['result']['name']
        assert 'pet_photo' in response_data['result']
        assert 'user_id' in response_data['result']
        assert response_data['result']['user_id'] == api_key

    def test_post_api_pets(self):
        response_api_key = self.pets_api.get_api_key(self, email=valid_email, password=valid_password)
        api_key = response_api_key['result']['key']
        print({'pet_photo': (open(pet_photo, 'rb'), 'image/jpeg')})
        response_data = self.pets_api.post_api_pets(self, api_key, create_pet_data, (open(pet_photo, 'rb'), 'image/jpeg'))

        # assert response_data['status'] == 200
        # assert 'age' in response_data['result']
        # assert create_pet_data['age'] == int(response_data['result']['age'])
        # assert 'animal_type' in response_data['result']
        # assert create_pet_data['animal_type'] == response_data['result']['animal_type']
        # assert 'created_at' in response_data['result']
        # assert 'id' in response_data['result']
        # assert 'name' in response_data['result']
        # assert create_pet_data['name'] == response_data['result']['name']
        # assert 'pet_photo' in response_data['result']
        # assert response_data['result']['pet_photo'] != ''
        # assert 'user_id' in response_data['result']
        # assert response_data['result']['user_id'] == api_key
        #
