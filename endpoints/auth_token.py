import allure
import requests
from endpoints.base_api import BaseApi

class GetAuthToken(BaseApi):
    @allure.step('Getting an authorization token')
    def get_token(self, payload):
        self.response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=payload
        )
        self.response_json = self.response.json()
        token = self.response_json['token']
        return token
    