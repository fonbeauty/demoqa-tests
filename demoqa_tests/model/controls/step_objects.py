from selene import have
from selene.support.shared import browser
from demoqa_tests import utils

class StepObjectsWithFluent:

    def set_sports_checkbox(self):
        browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
        return self

    def set_reading_checkbox(self):
        browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
        return self

    def set_musik_checkbox(self):
        browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()
        return self

    def fill_phone_number(self):
        browser.element('#userNumber').type('1234567890')
        return self

    def select_student_avatar_photo(self):
        browser.element('#uploadPicture').send_keys(utils.paths.resource('Bilbo_B.jpeg'))
        return self
