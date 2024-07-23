import pytest
import requests
from endpoints.auth_token import GetAuthToken
from tests.data import payloads
from endpoints.meme_put_update import MemePutUpdate
from endpoints.meme_by_id import GetMemeById
from endpoints.meme_deletion import MemeDeleted


@pytest.fixture(scope='session')
def token():
    getting_token = GetAuthToken()
    user_token = getting_token.get_token(payloads.auth_name)
    return user_token
    

@pytest.fixture()
def new_meme_for_test(token):
    payload = {
        "text": "When you deploy to production and nothing breaks.",
        "url": "https://i.imgflip.com/4/1bim.jpg",
        "tags": ["deployment", "programming", "success", "funny"],
        "info": {
            "description": "A meme that captures the rare and joyful moment when a deployment to production goes smoothly without any issues. The image typically features someone celebrating or expressing relief.",
            "author": "Unknown",
            "date": "2024-07-11"
        }
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': token
    }
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        json=payload,
        headers=headers
    )
    new_meme_id = response.json()["id"]
    yield new_meme_id
    requests.delete(f'http://167.172.172.115:52355/meme/{new_meme_id}', headers=headers)


@pytest.fixture()
def updated_with_put():
    return MemePutUpdate()


@pytest.fixture()
def getting_meme_by_id():
    return GetMemeById()


@pytest.fixture()
def deleted_meme():
    return MemeDeleted()
