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
    @allure.step("Checking meme's url")
    def meme_url_is(self, url):
        return self.response_json['url'] == url
    @allure.step("Checking meme's tags")
    def meme_tags_are(self,tags):
        return self.response_json['tags'] == tags
    @allure.step("Checking meme's info")
    def meme_info_is(self, info):
        return self.response_json['info'] == info
