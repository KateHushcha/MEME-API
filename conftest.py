import pytest
import requests
from endpoints.auth_token import GetAuthToken
from tests.data import payloads
from endpoints.meme_put_update import MemePutUpdate
from endpoints.meme_by_id import GetMemeById
from endpoints.meme_deletion import MemeDeleted
from endpoints.meme_new import NewMemePost
from endpoints.meme_all import GetAllMemes


@pytest.fixture(scope='session')
def token():
    getting_token = GetAuthToken()
    user_token = getting_token.get_token(payloads.auth_name)
    return user_token
    

@pytest.fixture()
def new_meme_for_test(token):
    payload = payloads.brand_new_meme
    new_meme_for_test = NewMemePost()
    new_meme_for_test.create_meme(payload=payload, token=token)
    new_meme_id = new_meme_for_test.response.json()["id"]
    yield new_meme_id
    deleted_meme_after = MemeDeleted()
    deleted_meme_after.meme_deletion(new_meme_id)


@pytest.fixture()
def updated_with_put():
    return MemePutUpdate()


@pytest.fixture()
def getting_meme_by_id():
    return GetMemeById()


@pytest.fixture()
def deleted_meme():
    return MemeDeleted()


@pytest.fixture()
def token_for_auth():
    return GetAuthToken()


@pytest.fixture
def for_new_meme():
    return NewMemePost()


@pytest.fixture()
def all_memes():
    return GetAllMemes()


