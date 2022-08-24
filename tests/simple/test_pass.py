import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_browser(browser: WebDriver):
    browser.find_element(By.CSS_SELECTOR, 'a[href="/login"').click()
    time.sleep(2)