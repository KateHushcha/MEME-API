import allure
import requests
from endpoints.base_api import BaseApi


class NewMemePost(BaseApi):
    @allure.step('Creating a new meme')
    def create_meme(self, payload, token):
        header = {'Authorization': token}
        self.response = requests.post(
            'http://167.172.172.115:52355/meme',
            json=payload,
            headers=header
        )
        self.response_json = self.response.json()

    @allure.step("Checking meme's text")
    def meme_text_is(self,text):
        return self.response_json['text'] == text
