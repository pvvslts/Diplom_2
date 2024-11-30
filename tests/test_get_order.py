import allure
import requests

from data.handle import Urls, Handle
from data.ingridient import Ingridient
@allure.suite("Показать заказы пользователя")
class TestGetOrderUser:

    @allure.description("")
    @allure.title("Получение доступных заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        requests_create_order = requests.post(f"{Urls.MAIN_URL}{Handle.MAKE_ORDER}", headers=token, data=Ingridient.correct_ingridients_data)
        response_get_order = requests.get(f"{Urls.MAIN_URL}{Handle.GET_ORDERS}", headers=token)
        assert response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] == requests_create_order.json()['order']['number']

    @allure.description("")
    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_order_user_not_auth(self):
        r = requests.get(f"{Urls.MAIN_URL}{Handle.GET_ORDERS}")
        assert r.status_code == 401 and r.json()['message'] == "You should be authorised"