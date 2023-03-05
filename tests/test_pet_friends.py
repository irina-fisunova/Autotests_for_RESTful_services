import pytest
from api import PetsApi
from settings import valid_email, valid_password

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