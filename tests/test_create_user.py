import pytest
import allure
from data import EXISTED_PAYLOAD
from methods.create_user_methods import CreateUser

@allure.epic("Управление пользователями")
@allure.description("Тесты для создания пользователя, включая валидацию и обработку ошибок.")
class TestCreateUser:
    def setup_method(self):
        self.create_user_methods = CreateUser()

    @allure.step("Тест создания уникального пользователя")
    def test_create_unique_user(self):
        response = self.create_user_methods.create_user()
        assert response.status_code == 200
        assert response.json() is not None

    @allure.step("Тест создания уже зарегистрированного пользователя")
    def test_create_already_registered_user(self):
        response = self.create_user_methods.create_user(EXISTED_PAYLOAD)
        assert response.status_code == 403
        assert response.json() == {
            "success": False,
            "message": "User already exists"
        }

    @pytest.mark.parametrize("field", ["email", "password", "name"])
    @allure.step("Тест создания пользователя с отсутствующим полем {field}")
    def test_create_user_missing_field(self, field):
        payload = EXISTED_PAYLOAD.copy()  # Создаем копию, чтобы не изменять оригинал
        del payload[field]
        response = self.create_user_methods.create_user(payload)
        assert response.status_code == 403
