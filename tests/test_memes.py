import allure
import pytest
from data import payloads
from endpoints.meme_all import GetAllMemes


@allure.feature('Token')
@allure.title('Getting token')
def test_auth_token(token_for_auth):
    token_for_auth.get_token(payloads.auth_name)
    assert token_for_auth.check_status_code_is(200)
    assert token_for_auth.token_is_returned()


@allure.feature('Token')
@allure.title('Invalid token')
def test_auth_token_invalid(token_for_auth):
    token_for_auth.get_token(payloads.invalid_name)
    assert token_for_auth.check_status_code_is(400)


@allure.feature('New memes')
@allure.title('New Meme Testing')
def test_new_meme(for_new_meme, token):
    for_new_meme.create_meme(payloads.brand_new_meme, token)
    assert for_new_meme.check_status_code_is(200)
    assert for_new_meme.meme_text_is(payloads.brand_new_meme['text'])
    assert for_new_meme.meme_url_is(payloads.brand_new_meme['url'])
    assert for_new_meme.meme_tags_are(payloads.brand_new_meme['tags'])
    assert for_new_meme.meme_info_is(payloads.brand_new_meme['info'])


@allure.title('Getting all memes')
@allure.story('Get')
def test_get_all_memes(all_memes, token):
    all_memes.get_all_memes(token)
    assert all_memes.check_status_code_is(200)


@allure.title('Getting all memes')
@allure.story('Get')
def test_get_all_memes_without_token(all_memes):
    all_memes.get_all_memes(token=None)
    assert all_memes.check_status_code_is(401)


@allure.story('Get')
@allure.feature('Exisitng memes')
def test_get_id_meme(getting_meme_by_id, new_meme_for_test, token):
    getting_meme_by_id.get_meme_id(new_meme_for_test, token)
    assert getting_meme_by_id.check_status_code_is(200)
    assert getting_meme_by_id.check_meme_id(new_meme_for_test)


@allure.story('Get')
@allure.feature('Exisitng memes')
def test_get_id_without_token(getting_meme_by_id, new_meme_for_test):
    getting_meme_by_id.get_meme_id(new_meme_for_test, token=None)
    assert getting_meme_by_id.check_status_code_is(401)


@allure.story('Get')
@allure.feature('Exisitng memes')
def test_get_with_fake_id(getting_meme_by_id, token):
    meme_id = 4560000
    getting_meme_by_id.get_meme_id(meme_id, token)
    assert getting_meme_by_id.check_status_code_is(404)


@allure.story('Memes')
@allure.title('Changing a meme with put')
@pytest.mark.parametrize(
        'url', ['https://memes.com', 'https://media.giphy.com/media/26gsspf0UqJpMg9bG/giphy.gif', 'https://i.imgur.com/4M7IWwP.png'],
        ids=['WEB', 'GIF', 'PNG']
)
def test_meme_put_updated(updated_with_put, new_meme_for_test, url, token):
    payload = payloads.put_update_meme
    payload['url'] = url
    payload['id'] = new_meme_for_test
    updated_with_put.meme_change_with_put(new_meme_for_test, payload, token)
    assert updated_with_put.check_status_code_is(200)
    assert updated_with_put.meme_updated_url(url)


@allure.story('Memes')
@allure.title('Attempt to change with missing fields')
def test_meme_put_missing_filed(updated_with_put, new_meme_for_test, token):
    payload = payloads.put_update_missing_field
    payload['id'] = new_meme_for_test
    updated_with_put.meme_change_with_put(new_meme_for_test, payload, token)
    assert updated_with_put.check_status_code_is(400)


@allure.story('Memes')
@allure.title('Attempt to change with invalid data')
def test_meme_put_invalid_data(updated_with_put, new_meme_for_test, token):
    payload = payloads.put_update_invalid_data
    payload['id'] = new_meme_for_test
    updated_with_put.meme_change_with_put(new_meme_for_test, payload, token)
    assert updated_with_put.check_status_code_is(400)


@allure.feature('Main')
@allure.story('Memes')
@allure.title('Deleting newly created meme')
def test_meme_is_deleted(deleted_meme, new_meme_for_test, token):
    deleted_meme.meme_deletion(new_meme_for_test, token)
    assert deleted_meme.check_status_code_is(200)
    assert deleted_meme.meme_is_deleted(new_meme_for_test)


@allure.feature('Main')
@allure.story('Memes')
@allure.title('Deleting a meme without token')
def test_deleted_meme_without_token(deleted_meme, new_meme_for_test):
    deleted_meme.meme_deletion(new_meme_for_test, token=None)
    assert deleted_meme.check_status_code_is(401)


@allure.feature('Main')
@allure.story('Memes')
@allure.title('Deleting a fake meme')
def test_deleted_fake_meme(deleted_meme, token):
    meme_id = 8989897
    deleted_meme.meme_deletion(meme_id, token)
    assert deleted_meme.check_status_code_is(404)
