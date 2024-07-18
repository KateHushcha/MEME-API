import allure
import requests
from endpoints.base_api import BaseApi


class MemePutUpdate(BaseApi):
    def meme_change_with_put(self, meme_id, url, token):
        header = {'Content-Type': 'application/json', 'Authorization': token}
        payload = {
            'url': url,
            'id': meme_id,
            'text': str,
            'tags': list,
            'info': object
        }
        self.response = requests.put(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            json=payload,
            headers=header
        )
        self.response_json = self.response.json()
    @allure.step('Updated url with put')
    def meme_updated_url(self, url):
        return self.response_json['url'] == url
