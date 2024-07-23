import allure
import requests
from endpoints.base_api import BaseApi


class MemePutUpdate(BaseApi):
    def meme_change_with_put(self, meme_id, payload, token):
        header = {'Content-Type': 'application/json', 'Authorization': token}
        self.response = requests.put(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            json=payload,
            headers=header
        )
        if self.response.status_code == 200:
            self.response_json = self.response.json()
        else:
            self.response_json = None

    @allure.step('Updated url with put')
    def meme_updated_url(self, url):
        return self.response_json['url'] == url
