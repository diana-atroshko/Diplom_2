class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_ORDER_URL = f'{BASE_URL}/api/orders'
    CREATE_USER_URL = f'{BASE_URL}/api/auth/register'
    LOGIN_URL = f'{BASE_URL}/api/auth/login'
    CHANGING_USER_DATA_URL = f'{BASE_URL}/api/auth/user'
    RECEIVING_ORDERS_URL = f'{BASE_URL}/api/orders'


ingredient1 = "61c0c5a71d1f82001bdaaa6d"
ingredient2 = "61c0c5a71d1f82001bdaaa70"
EXISTED_PAYLOAD = {
            "email": "lotosmdiplom@yandex.ru",
            "password": "asdfghjk",
            "name": "lotos"
        }

AUTH_ERROR_RESPONSE = {
            "success": False,
            "message": "You should be authorised"
        }

EMAIL_ERROR_RESPONSE = {
            "success": False,
            "message": "User with such email already exists"
        }

INGR_ID_ERROR_RESPONSE = {"success": False, "message": "Ingredient ids must be provided"}
EXIST_USER_ERROR_RESPONSE = {
            "success": False,
            "message": "User already exists"
        }

LOGIN_ERROR_RESPONSE = {
            "success": False,
            "message": "email or password are incorrect"
        }