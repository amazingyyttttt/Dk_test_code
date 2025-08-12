import pytest

from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI


@pytest.fixture(scope="session")
def login_api() -> LoginAPI:
    return LoginAPI()


@pytest.fixture(scope="session")
def course_api() -> CourseAPI:
    return CourseAPI()


@pytest.fixture(scope="session")
def contract_api() -> ContractAPI:
    return ContractAPI()


@pytest.fixture(scope="session")
def uuid(login_api: LoginAPI) -> str:
    response = login_api.get_verify_code()
    return response.json().get("uuid")


@pytest.fixture(scope="session")
def token(login_api: LoginAPI, uuid: str) -> str:
    login_data = {
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        "uuid": uuid,
    }
    response = login_api.login(test_data=login_data)
    return response.json().get("token")


