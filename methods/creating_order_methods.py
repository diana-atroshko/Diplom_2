import requests
import allure
from data import CREATE_ORDER_URL


class CreatingOrder:
    @allure.step("Создание заказа")
    def create_order(self, token, ingredients):
        headers = {"Authorization": token} if token else {}
        payload = {"ingredients": ingredients}
        return requests.post(CREATE_ORDER_URL, json=payload, headers=headers)


