import allure
import requests
from data import CHANGING_USER_DATA_URL


class UserProfile:
    @allure.step("Получение информации о пользователе")
    def get_user_info(self, token):
        headers = {"Authorization": token}
        return requests.get(CHANGING_USER_DATA_URL, headers=headers)

    @allure.step("Обновление информации о пользователе")
    def update_user_info(self, token, email=None, name=None):
        headers = {"Authorization": token}
        payload = {}
        if email:
            payload["email"] = email
        if name:
            payload["name"] = name
        return requests.patch(CHANGING_USER_DATA_URL, json=payload, headers=headers)
    