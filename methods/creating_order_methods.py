import requests
import allure
from data import Url


class CreatingOrder:
    @allure.step("Создание заказа")
    def create_order(self, token, ingredients):
        headers = {"Authorization": token} if token else {}
        payload = {"ingredients": ingredients}
        return requests.post(Url.CREATE_ORDER_URL, json=payload, headers=headers)


