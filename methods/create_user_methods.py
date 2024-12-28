import string
import random
import requests
import allure
from data import CREATE_USER_URL


class CreateUser:

    @allure.step("Генерация случайной строки")
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @allure.step("Генерация данных пользователя")
    def generate_user_data(self):
        email = f'{self.generate_random_string(8)}@yandex.ru'
        password = self.generate_random_string(8)
        name = self.generate_random_string(8)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    @allure.step("Создание пользователя")
    def create_user(self, payload=None):
        if payload is None:
            payload = self.generate_user_data()

        response = requests.post(CREATE_USER_URL, json=payload)
        return response