import allure
import requests
from endpoints.base_api import BaseApi


main_url = 'http://167.172.172.115:52355/meme'

class GetAllMemes(BaseApi):
    @allure.step('Getting all memes')
    def get_all_memes(self, token):
        header = {'Authorization': token}
        self.response = requests.get(
            main_url,
            headers=header
        )
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.response_json = self.response.status_code
