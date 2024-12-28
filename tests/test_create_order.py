import allure
from data import ingredient1, ingredient2
import pytest
from methods.creating_order_methods import CreatingOrder

@allure.epic("Управление заказами")
@allure.description("Тесты для создания заказов, с авторизацией и без и валидацию ингредиентов.")
class TestCreateOrder:
    @classmethod
    def setup_class(cls):
        cls.order_methods = CreatingOrder()

    @allure.step("Тест создания заказа с авторизацией")
    def test_create_order_with_authorization(self,existing_user_fixture):
        ingredients = [ingredient1, ingredient2]
        response = self.order_methods.create_order(existing_user_fixture, ingredients)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.step("Тест создания заказа без авторизации")
    def test_create_order_without_authorization(self):
        ingredients = [ingredient1, ingredient2]
        response = self.order_methods.create_order(None, ingredients)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.step("Тест создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self,existing_user_fixture):
        response = self.order_methods.create_order(existing_user_fixture, [])
        assert response.status_code == 400
        assert response.json() == {"success": False, "message": "Ingredient ids must be provided"}

    @allure.step("Тест создания заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient(self,existing_user_fixture):
        ingredients = ["invalid_hash_ingredient"]
        response = self.order_methods.create_order(existing_user_fixture, ingredients)
        assert response.status_code == 500