import os
import pytest

from selenium import webdriver
from dotenv import load_dotenv


def pytest_configure():
    load_dotenv()


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(os.getenv('CHROME_DRIVER_PATH'))
    driver.get('https://github.com/')

    yield driver

    driver.quit()
