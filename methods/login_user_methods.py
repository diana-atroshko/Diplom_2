import allure
import requests
from data import Url,EXISTED_PAYLOAD


class LoginUser:

    @allure.step("Авторизация пользователя")
    def login_user(self, payload= None):

        if payload is None:
            email = EXISTED_PAYLOAD['email']
            password = EXISTED_PAYLOAD['password']
            payload = {
                "email": email,
                "password": password
            }

        return requests.post(Url.LOGIN_URL, json=payload)

    @allure.step("Получение токена пользователя")
    def get_token(self, email, password):

        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Url.LOGIN_URL, json=payload)

        if response.status_code == 200:
            return response.json().get('accessToken')
        else:
            raise Exception("Login failed: " + response.text)