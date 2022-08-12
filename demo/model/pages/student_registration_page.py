from selene import command, have
from selene.support.shared import browser
from demo import utils
from demo.data import User
from demo.model.controls import dropdown
from demo.model.controls.tags_input import TagsInput


class StudentRegistrationForm:

    def set_first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    def set_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def set_subjects(self, subjects: list[str]):
        for value in subjects:
            TagsInput(browser.element('#subjectsInput')).add_by_click(value)
        return self

    def set_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def set_gender(self, gender):
        browser.element('#genterWrapper').all('.custom-radio').element_by(have.exact_text(gender)).click()
        return self

    def set_hobbies(self, sports, reading, music):
        if sports:
            browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
        if reading:
            browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
        if music:
            browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()
        return self

    def set_mobile_number(self, mobile_number):
        browser.element('#userNumber').type(mobile_number)
        return self

    def set_avatar(self, avatar):
        browser.element('#uploadPicture').send_keys(utils.paths.resource(avatar))
        return self

    def set_address(self, address):
        browser.element('#currentAddress').type(address).perform(command.js.scroll_into_view)
        return self

    def set_state(self, state):
        dropdown.autocomplete(browser.element('#state'), option=state)
        return self

    def set_city(self, city):
        dropdown.autocomplete(browser.element('#city'), option=city)
        return self

    def set_date(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month)).click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(str(year))).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)

    def fill_form(self, user: User):
        self.set_first_name(user.first_name)
        self.set_last_name(user.last_name)
        self.set_subjects(user.subjects)
        self.set_email(user.email)
        self.set_gender(user.gender)
        self.set_hobbies(sports=user.hobbi_sports, reading=user.hobbi_reading, music=user.hobbi_music)
        self.set_mobile_number(user.mobile_number)
        self.set_avatar(user.picture)
        self.set_address(user.address)
        self.set_state(user.state)
        self.set_city(user.city)
        self.set_date(year=user.birthday_year, month=user.birthday_month, day=user.birthday_day)
        return self
