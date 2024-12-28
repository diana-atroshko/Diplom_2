import pytest

from data import EXISTED_PAYLOAD
from methods.create_user_methods import CreateUser
from methods.login_user_methods import LoginUser


@pytest.fixture(scope="function")
def user_fixture():
    user_methods = CreateUser()
    payload = user_methods.generate_user_data()
    response = user_methods.create_user(payload)
    assert response.status_code == 200, "Failed to create user"
    return payload

@pytest.fixture(scope="module")
def existing_user_fixture():
    login_user = LoginUser()
    token = login_user.get_token(EXISTED_PAYLOAD["email"], EXISTED_PAYLOAD["password"])
    assert token is not None, "Failed to get token"
    return token