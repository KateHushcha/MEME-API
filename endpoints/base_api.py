import requests
import allure
from endpoints.meme_schema import MemeData


class BaseApi():
    response = requests.Response
    response_json = dict
    data = MemeData

    @allure.step('Check status code')
    def check_status_code_is(self, code):
        return self.response.status_code == code
