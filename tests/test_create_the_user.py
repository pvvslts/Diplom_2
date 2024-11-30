import pytest
import allure
import requests

from data.handle import Urls, Handle
from data.users_data import User
@allure.suite("Создание пользователя")
class TestCreateTheUser:

    @allure.description("Создание нового пользователя")
    @allure.title("Создание нового пользователя")
    def test_create_new_the_user_positive(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handle.CREATE_USER}', data=User.create_user_data())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.description("При создании существующего пользователя показывает предупреждение")
    @allure.title("Создание существующего пользователя")
    def test_create_full_the_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handle.CREATE_USER}', data=User.data_full)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.description("При создании пользователя с некорректыми данными показывает предупреждение")
    @allure.title("Создание пользователя с некорректными данными или без обязательных полей")
    @pytest.mark.parametrize("user_data", [User.data_not_email, User.data_not_password, User.data_not_name])
    def test_create_the_user_with_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Handle.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and "Email, password and name are required fields" in response.text