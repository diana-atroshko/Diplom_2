import allure
from methods.get_order_methods import Order


@allure.epic("Управление заказами")
@allure.description("Тесты для получения заказов конкретного пользователя: авторизованный пользователь и неавторизованный пользователь.")
class TestGetOrders:
    def setup_method(self, existing_user_fixture):
        self.order_methods = Order()
        self.token = existing_user_fixture

    @allure.step("Тест получения заказов авторизованным пользователем")
    def test_get_orders_authorized_user(self, existing_user_fixture):
        response = self.order_methods.get_orders(existing_user_fixture)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert isinstance(response.json().get("orders"), list)

    @allure.step("Тест получения заказов неавторизованным пользователем")
    def test_get_orders_unauthorized_user(self):
        response = self.order_methods.get_orders("")
        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": "You should be authorised"
        }