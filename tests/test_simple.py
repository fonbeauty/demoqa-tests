import allure


@allure.feature('Простые тесты')
@allure.story('Выполнение простого теста 1')
def test_simple1():
    with allure.step('Простой тест 1'):
        pass


@allure.feature('Простые тесты')
@allure.story('Выполнение простого теста 2')
def test_simple2():
    with allure.step('Простой тест 2'):
        pass


@allure.feature('Простые тесты')
@allure.story('Выполнение простого теста 3')
def test_simple3():
    with allure.step('Простой тест 3'):
        pass
