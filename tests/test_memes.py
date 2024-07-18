import allure
import pytest
from data import payloads
from endpoints.meme_new import NewMemePost
from endpoints.auth_token import GetAuthToken
from endpoints.meme_all import GetAllMemes
from endpoints.meme_by_id import GetMemeById
from endpoints.meme_put_update import MemePutUpdate

def test_auth_token():
    getting_token = GetAuthToken()
    getting_token.get_token(payloads.auth_name)
    assert getting_token.check_status_code_is(200)


@allure.feature('New memes')
@allure.title('New Meme Testing')
def test_new_meme(token):
    create_new_meme = NewMemePost()
    create_new_meme.create_meme(payloads.brand_new_meme, token)
    assert create_new_meme.check_status_code_is(200)
    assert create_new_meme.meme_text_is(payloads.brand_new_meme['text'])


@allure.title('Getting all memes')
@allure.story('Get')
def test_get_all_memes(token):
    get_all = GetAllMemes()
    get_all.get_all_memes(token)
    assert get_all.check_status_code_is(200)


@allure.story('Get')
@allure.feature('Exisitng memes')
def test_get_id_meme(new_meme_for_test, token):
    get_id_meme = GetMemeById()
    get_id_meme.get_meme_id(new_meme_for_test, token)
    assert get_id_meme.check_status_code_is(200)
    assert get_id_meme.check_meme_id(new_meme_for_test)


@pytest.mark.parametrize(
        'url', ['https://memes.com', 'https://media.giphy.com/media/26gsspf0UqJpMg9bG/giphy.gif', 'https://i.imgur.com/4M7IWwP.png'],
        ids=['WEB', 'GIF', 'PNG']
)
def test_meme_put_updated(updated_with_put, new_meme_for_test, url, token):
    updated_meme = MemePutUpdate()
    updated_meme.meme_change_with_put(new_meme_for_test, url, token)
    assert updated_meme.check_status_code_is(200)
    assert updated_meme.meme_updated_url(url)
