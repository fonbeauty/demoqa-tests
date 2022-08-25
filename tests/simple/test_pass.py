import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def assert_h1(browser: WebDriver):
    browser.find_element(By.CSS_SELECTOR, 'h1').text == 'Sign in to GitHub'


def test_desktop_browser(browser: WebDriver):
    width = browser.get_window_size().get("width")
    height = browser.get_window_size().get("height")
    if width//height >= 1:
        browser.get('https://github.com/')
        browser.find_element(By.CSS_SELECTOR, 'a[href="/login"').click()
        # time.sleep(2)
    else:
        pytest.skip('Это разрешение экрана не для десктопной версии')
    assert_h1(browser)


def test_mobile_browser(browser: WebDriver):
    width = browser.get_window_size().get("width")
    height = browser.get_window_size().get("height")
    if width//height < 1:
        browser.get('https://github.com/')
        browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Toggle navigation"').click()
        browser.find_element(By.CSS_SELECTOR, 'a[href="/login"').click()
        # time.sleep(2)
    else:
        pytest.skip('Это разрешение экрана не для мобильной версии')
    assert_h1(browser)


@pytest.mark.parametrize("browser", [(1000, 1000)], indirect=True)
def test_indirect_size(browser: WebDriver):
    browser.get('https://github.com/')
    browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Toggle navigation"').click()
    browser.find_element(By.CSS_SELECTOR, 'a[href="/login"').click()
    # time.sleep(2)
    assert_h1(browser)
