import allure
import requests

from data.handle import Urls, Handle
from data.users_data import User

@allure.suite("Авторизация")
class TestLogin:
    @allure.description("Аторизация существующего пользователя")
    @allure.title("Авторизация существующего пользователя")
    def test_login_the_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handle.LOGIN}', data=User.data_correct)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.description("Авторизация несуществующего пользователя")
    @allure.title("Авторизация несуществующего пользователя, неверные логин и пароль")
    def test_login_the_user_with_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handle.LOGIN}', data=User.data_negative)
        assert response.status_code == 401 and response.json().get('success') == False