import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_decoreator_steps(browser_management):
    open_main_page('https://github.com')
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_text('С Новым Годом (2022)')


@allure.step('Открываем главную страницу')
def open_main_page(url: str):
    browser.open(url)


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    search_input = browser.element('.header-search-input')
    search_input.click()
    search_input.send_keys(repo)
    search_input.submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие Issue с названием {name}')
def should_see_issue_with_text(name: str):
    browser.element(by.link_text(name)).should(be.visible)