from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_selene_github(browser_management):
    browser.open('https://github.com')
    search_input = browser.element('.header-search-input')
    search_input.click()
    search_input.send_keys('eroshenkoam/allure-example')
    search_input.submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()

    browser.element(by.link_text('С Новым Годом (2022)')).should(be.visible)