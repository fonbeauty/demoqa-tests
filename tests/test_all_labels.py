import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure_commons.types import Severity


def test_dynamic_labels(browser_management):
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'bilbo')
    allure.dynamic.feature('Проверки репозитория')
    allure.dynamic.story('Проверки элементов')
    allure.dynamic.link('https://github.com', name='Testing')

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


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'bilbo')
@allure.feature('Проверки репозитория')
@allure.story('Проверки элементов')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels(browser_management):
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