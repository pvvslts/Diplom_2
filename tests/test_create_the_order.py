import allure
import requests

from data.handle import Urls, Handle
from data.ingridient import Ingridient
@allure.suite("Создание заказа")
class TestCreateTheOrder:
    @allure.description("Создание заказа авторизованным пользователем")
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_auth_order(self, create_user):
        token = {'Authorization': create_user[3]}
        r = requests.post(f"{Urls.MAIN_URL}{Handle.MAKE_ORDER}", headers=token, data=Ingridient.correct_ingridients_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Создание заказа не авторизованным пользователем")
    @allure.title("Создание заказа не авторизованным пользователем")
    def test_create_not_auth_order(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handle.MAKE_ORDER}", data=Ingridient.correct_ingridients_data)
        assert r.status_code == 200 and r.json().get("success") is True


    @allure.description("Создание заказа без ингридиентов")
    @allure.title("Создание заказа без ингридиентов")
    def test_create_order_with_ingridient(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handle.MAKE_ORDER}")
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.description("Создание с некорректным хешем ингридиента")
    @allure.title("Создание с некорректным хешем ингридиента")
    def test_create_order_with_invalid_hash_ingridient(self):
        response = requests.post(Urls.MAIN_URL + Handle.MAKE_ORDER, headers=Handle.headers,
                                 json=Ingridient.incorrect_ingridients_data)
        assert response.status_code == 500 and 'Internal Server Error' in response.text