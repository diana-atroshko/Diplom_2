import allure

from data import EXISTED_PAYLOAD
from methods.changing_user_data_methods import UserProfile
from methods.create_user_methods import CreateUser
import pytest
from methods.login_user_methods import LoginUser

@allure.epic("Управление профилем пользователя")
@allure.description("Тесты для управления профилями пользователей, включая создание, получение и обновление.")
class TestUserProfile:
    @classmethod
    def setup_class(cls):
        cls.user_methods = CreateUser()
        cls.login_user = LoginUser()
        cls.profile_methods = UserProfile()


    @allure.step("Тест получения информации о пользователе с авторизацией")
    def test_get_user_info_with_authorization(self,user_fixture):
        payload = user_fixture  # Используем созданного пользователя
        login_response = self.login_user.login_user(payload)
        assert login_response.status_code == 200, "Failed to login"
        token = self.login_user.get_token(payload["email"], payload["password"])

        response = self.profile_methods.get_user_info(token)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json()["user"]["email"] == payload["email"]
        assert response.json()["user"]["name"] == payload["name"]

    @allure.step("Тест обновления информации о пользователе с авторизацией")
    def test_update_user_info_with_authorization(self,user_fixture):
        payload = user_fixture  # Используем созданного пользователя
        login_response = self.login_user.login_user(payload)
        assert login_response.status_code == 200, "Failed to login"
        token = self.login_user.get_token(payload["email"], payload["password"])
        new_email = f'{self.user_methods.generate_random_string(8)}@yandex.ru'
        new_name = self.user_methods.generate_random_string(8)
        response = self.profile_methods.update_user_info(token, new_email, new_name)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json()["user"]["email"] == new_email
        assert response.json()["user"]["name"] == new_name

    @allure.step("Тест обновления информации о пользователе без авторизации")
    def test_update_user_info_without_authorization(self):
        response = self.profile_methods.update_user_info("", "new_email@yandex.ru", "NewName")
        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": "You should be authorised"
        }

    @allure.step("Тест обновления информации с уже существующим email")
    def test_update_with_existing_email(self,user_fixture):
        payload = user_fixture
        token = self.login_user.get_token(payload["email"], payload["password"])
        existing_email = EXISTED_PAYLOAD["email"]
        response = self.profile_methods.update_user_info(token, existing_email)
        assert response.status_code == 403
        assert response.json() == {
            "success": False,
            "message": "User with such email already exists"
        }