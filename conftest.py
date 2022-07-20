import pytest
import os
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # os.environ['WDM_SSL_VERIFY'] = '0'
    ChromeDriverManager(version='98.0.4758.102', cache_valid_range=100).install()
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
