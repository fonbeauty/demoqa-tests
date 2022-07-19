import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_lambda_steps(browser_management):
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    search_input = browser.element('.header-search-input')
    with allure.step('Ищем репозиторий'):
        search_input.click()
        search_input.send_keys('eroshenkoam/allure-example')
        search_input.submit()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с названием "С Новым Годом (2022)"'):
        browser.element(by.link_text('С Новым Годом (2022)')).should(be.visible)