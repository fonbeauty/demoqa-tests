import os
import pytest

from selenium import webdriver
from dotenv import load_dotenv


def pytest_configure():
    load_dotenv()


@pytest.fixture(params=[(1200, 900), (1024, 800), (400, 700), (500, 900)])
def browser(request):
    driver = webdriver.Chrome(os.getenv('CHROME_DRIVER_PATH'))
    driver.set_window_size(request.param[0], request.param[1])

    yield driver

    driver.quit()
