import allure
import requests
from endpoints.base_api import BaseApi


class GetMemeById(BaseApi):
    def get_meme_id(self, meme_id, token):
        header = {'Authorization': token}
        self.response = requests.get(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            headers=header
        )
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.response_json = self.response.status_code

    @allure.step('Checking meme id')
    def check_meme_id(self, meme_id):
        return self.response_json['id'] == meme_id
 