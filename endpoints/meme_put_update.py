import allure
import requests
from endpoints.base_api import BaseApi


class MemePutUpdate(BaseApi):
    def meme_change_with_put(self, meme_id, url, token):
        header = {'Content-Type': 'application/json', 'Authorization': token}
        payload = {'url': url}
        self.response = requests.put(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            json=payload,
            headers=header
        )
        print("Response status code:", self.response.status_code)
        print("Response content:", self.response.content)
        self.response.raise_for_status()
        self.response_json = self.response.json()
    @allure.step('Updated url with put')
    def meme_updated_url(self, url):
        return self.response_json['url'] == url
