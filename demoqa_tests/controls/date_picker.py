from enum import Enum

from selene import have
from selene.core.entity import Element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selene.support.shared import browser


class Month(Enum):
    January = 'January'
    February = 'February'
    March = 'March'
    April = 'April'
    May = 'May'
    June = 'June'
    July = 'July'
    August = 'August'
    September = 'September'
    October = 'October'
    November = 'November'
    December = 'December'


class DatePicker:

    def __init__(self, element: Element):
        self.element = element

    def set_date_direct(self, date: str):
        self.element.set_value(date)
        self.element.click()
        actions = ActionChains(browser.driver)
        actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
        self.element.type(date)
        self.element.press_enter()

    def set_date_from_picker(self, day: int, month: Month, year: str):
        self.element.click()
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month.value)).click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(year)).click()
        if day >= 10:
            browser.element(f'.react-datepicker__day--0{day}').click()
        else:
            browser.element(f'.react-datepicker__day--00{day}').click()

