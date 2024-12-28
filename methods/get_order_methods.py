import allure
import requests

from data import RECEIVING_ORDERS_URL


class Order:
    @allure.step("Получение списка заказов пользователя")
    def get_orders(self, token):
        headers = {"Authorization": token} if token else {}
        return requests.get(RECEIVING_ORDERS_URL, headers=headers)

