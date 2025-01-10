import allure
import requests

from data import Url


class Order:
    @allure.step("Получение списка заказов пользователя")
    def get_orders(self, token):
        headers = {"Authorization": token} if token else {}
        return requests.get(Url.RECEIVING_ORDERS_URL, headers=headers)

