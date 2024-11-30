import pytest
import requests

from data.handle import Urls, Handle
from data.users_data import User
@pytest.fixture(scope="function")
def create_user():
    payload = User.create_user_data()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Urls.MAIN_URL}{Handle.CREATE_USER}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Urls.MAIN_URL}{Handle.DELETE_USER}", headers={'Authorization': f'{token}'})