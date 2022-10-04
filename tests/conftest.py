import pytest

from dotenv import load_dotenv

from utils.requests_helper import BaseSession

REQRES_BASE_URL = 'https://reqres.in/api'


def pytest_configure():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def reqres_session() -> BaseSession:
    return BaseSession(base_url=REQRES_BASE_URL)



