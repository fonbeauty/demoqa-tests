import os

from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = os.getenv('base_url', 'https://demoqa.com')
    browser.config.browser_name = os.getenv('browser_name', 'chrome')
    browser.config.hold_browser_open = os.getenv('hold_browser_open', 'False')
    browser.config.timeout = float(os.getenv('timeout', '3'))