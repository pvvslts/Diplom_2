import allure
import requests

from data.handle import Urls, Handle
from data.users_data import User
@allure.suite('Изменение данных пользователя')
class TestChangeUserData:

    @allure.description("Изменение email-адреса авторизованного пользователя")
    @allure.title("Успешное изменение email-адреса авторизованного пользователя")
    def test_change_the_auth_user_email(self, create_user):
        payload = {'email': User.create_user_data()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handle.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.description("Изменение password авторизованного пользователя")
    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_change_the_auth_user_password(self, create_user):
        payload = {'password': User.create_user_data()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handle.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Изменение Name авторизованного пользователя")
    @allure.title("Успешное изменение Name авторизованного пользователя")
    def test_change_the_auth_user_name(self, create_user):
        payload = {'name': User.create_user_data()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handle.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.description("Изменение данных пользователя без авторизации")
    @allure.title("Изменение данных пользователя без авторизацией")
    def test_change_the_not_auth_user_data(self):
        r = requests.patch(f"{Urls.MAIN_URL}{Handle.CHANGE_USER_DATA}", data=User.create_user_data())
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'