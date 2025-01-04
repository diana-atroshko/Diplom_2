from methods.login_user_methods import LoginUser
import allure

@allure.epic("Управление пользователями")
@allure.description("Тесты для авторизации пользователей")
class TestLoginUser:
    def setup_method(self):
        self.login_methods = LoginUser()

    @allure.step("Тест авторизации существующего пользователя")
    def test_login_existing_user(self):
        response = self.login_methods.login_user()
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json().get("accessToken") is not None

    @allure.step("Тест авторизации с некорректными учетными данными")
    def test_login_with_incorrect_credentials(self):
        payload = {
            "email": "wrong-email@yandex.ru",
            "password": "wrongpassword"}
        response = self.login_methods.login_user(payload)
        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": "email or password are incorrect"
        }

    @allure.step("Тест авторизации с отсутствующим полем")
    def test_login_missing_field(self):
        payload = {
            "email": "",
            "password": "somepassword"}
        response = self.login_methods.login_user(payload)
        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": "email or password are incorrect"
        }