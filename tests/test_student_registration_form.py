from selene import have, command
from selene.support.shared import browser
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tags_input import TagsInput
from demoqa_tests.controls.date_picker import DatePicker, Month

from demoqa_tests.utils.file import resource


def given_student_registration_form_opened():
    browser.open('/automation-practice-form')
    (
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
            .with_(timeout=10)
            .should(have.size_greater_than_or_equal(1))
            .perform(command.js.remove)
    )


def test_register_student():
    given_student_registration_form_opened()

    # WHEN
    browser.element('#firstName').type('Harry')
    browser.element('#lastName').type('Potter')
    browser.element('#userEmail').type('theboywholived@hogwarts.edu')

    gender = browser.element('#genterWrapper')
    gender.all('.custom-radio').element_by(have.exact_text('Male')).click()

    browser.element('#userNumber').type('1234567890')

    date_birth = DatePicker(browser.element('#dateOfBirthInput'))
    date_birth.set_date_from_picker(6, Month.January, '1988')
    '''
    set date direct
    date_birth.set_date_direct('6 Jul 1988')
    '''

    subjects = TagsInput(browser.element('#subjectsInput'))

    subjects.autocomplete('Chem', 'Chemistry')
    subjects.type('Maths')

    browser.all('.custom-checkbox')
    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    browser.element('#uploadPicture').send_keys(
        resource('Bilbo_B.jpeg')
    )

    browser.element(
        '#currentAddress'
    ).type('4 Privet Drive').perform(command.js.scroll_into_view)

    state_dropdown = Dropdown(browser.element('#state'))
    city_dropdown = Dropdown(browser.element('#city'))

    state_dropdown.select('Uttar Pradesh')
    city_dropdown.autocomplete('Lucknow')

    subjects.type('Physics')

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )

    results = Table()

    results.cells_of_row(1).should(have.exact_text('Student Name Harry Potter'))
    results.cells_of_row(2).should(have.exact_text('Student Email theboywholived@hogwarts.edu'))
    results.cells_of_row(3).should(have.exact_text('Gender Male'))
    results.cells_of_row(4).should(have.exact_text('Mobile 1234567890'))
    results.cells_of_row(5).should(have.exact_text('Date of Birth 06 January,1988'))
    results.cells_of_row(6).should(have.exact_text('Subjects Chemistry, Maths, Physics'))
    results.cells_of_row(7).should(have.exact_text('Hobbies Reading, Music'))
    results.cells_of_row(8).should(have.exact_text('Picture Bilbo_B.jpeg'))
    results.cells_of_row(9).should(have.exact_text('Address 4 Privet Drive'))
    results.cells_of_row(10).should(have.exact_text('State and City Uttar Pradesh Lucknow'))
