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