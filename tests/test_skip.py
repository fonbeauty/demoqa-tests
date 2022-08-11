import allure
import pytest


@allure.feature('Простые тесты')
@allure.story('Пропущенные тесты')
@pytest.mark.skip
def test_skip1():
    with allure.step('Пропущенный тест 1'):
        pass


@allure.feature('Простые тесты')
@allure.story('Пропущенные тесты')
@pytest.mark.skip
def test_skip2():
    with allure.step('Пропущенный тест 2'):
        pass

