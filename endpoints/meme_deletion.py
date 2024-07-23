import allure
import requests
from endpoints.base_api import BaseApi
from endpoints.meme_schema import DeletedMeme


class MemeDeleted(BaseApi):
    @allure.step('Deleting a meme')
    def meme_deletion(self, meme_id, token):
        header = {'Content-Type': 'application/json', 'Authorization': token}
        self.response = requests.delete(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            headers=header
        )
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.response_json = {"message": self.response.text}
