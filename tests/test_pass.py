import allure


@allure.feature('Простые тесты')
@allure.story('Успешные тесты')
def test_pass1():
    with allure.step('Успешный тест 1'):
        pass


@allure.feature('Простые тесты')
@allure.story('Успешные тесты')
def test_pass2():
    with allure.step('Успешный тест 2'):
        pass


@allure.feature('Простые тесты')
@allure.story('Успешные тесты')
def test_pass3():
    with allure.step('Успешный тест 3'):
        pass


@allure.feature('Простые тесты')
@allure.story('Успешные тесты')
def test_pass4():
    with allure.step('Успешный тест 4'):
        pass