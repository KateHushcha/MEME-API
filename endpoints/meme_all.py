import allure
import requests
from endpoints.base_api import BaseApi


class GetAllMemes(BaseApi):
    @allure.step('Getting all memes')
    def get_all_memes(self, token):
        header = {'Authorization': token}
        self.response = requests.get(
            'http://167.172.172.115:52355/meme',
            headers=header
        )
        self.response_json = self.response.json()
