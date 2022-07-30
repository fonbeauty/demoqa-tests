from selene import command, have
from selene.support.shared import browser

from demoqa_tests.data import User
from demoqa_tests.model.controls import TagsInput


class StudentRegistrationForm:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.subjects = TagsInput.by_name('subjectsInput')
        self.submit_button = browser.element('#submit')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('#genterWrapper').all('.custom-radio')

    def add_subjects(self, *names):
        for name in names:
            self.subjects.add(name)
        return self

    def should_have_subjects(self, *names):
        self.subjects.should_have_texts(*names)
        return self

    def submit(self):
        self.submit_button.perform(command.js.click)

    def fill_form(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.exact_text(user.gender)).click()

        # self.subjects.autocomplete(*user.subjects)
        return self
