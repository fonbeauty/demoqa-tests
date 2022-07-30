from selene import have, command
from selene.support.shared import browser
from demoqa_tests.data import User
from demoqa_tests.model.application_manager import ApplicationManager
from demoqa_tests.model.controls import dropdown
from demoqa_tests import utils
from demoqa_tests.model.controls.step_objects import StepObjectsWithFluent


# DATA MODEL
harry_potter = User(
    first_name='Harry',
    last_name='Potter',
    subjects=['Chemistry', 'Maths', 'Physics'],
    email='theboywholived@hogwarts.edu',
    gender='Male'
)


def test_register_student():
    app = ApplicationManager()
    step_object_with_fluent = StepObjectsWithFluent()

    app.given_student_registration_form_opened()

    # WHEN

    # APPLICATION MANAGER
    app.form.fill_form(harry_potter)

    # STEP OBJECT WITH FLUENT
    (
        step_object_with_fluent
            .set_sports_checkbox()
            .set_musik_checkbox()
            .set_reading_checkbox()
            .fill_phone_number()
            .select_student_avatar_photo()
    )

    # browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element(
        '.react-datepicker__month-select'
    ).all('option').element_by(have.exact_text('July')).click()
    browser.element(
        '.react-datepicker__year-select'
    ).all('option').element_by(have.exact_text('1980')).click()
    browser.element(f'.react-datepicker__day--0{31}').click()


    app.form.add_subjects('Chemistry', 'Maths', 'Physics')
    app.form.should_have_subjects('Chemistry', 'Maths', 'Physics')

    # browser.element('#uploadPicture').send_keys(
    #     utils.paths.resource('Bilbo_B.jpeg')
    # )

    browser.element(
        '#currentAddress'
    ).type('4 Privet Drive').perform(command.js.scroll_into_view)

    dropdown.autocomplete(browser.element('#state'), option='Uttar Pradesh')
    dropdown.autocomplete(browser.element('#city'), option='Lucknow')

    app.form.submit()

    # THEN
    app.results.should_have_row_with_exact_texts('Student Name', 'Harry Potter')

    app.results.table.cells_of_row(1).should(have.exact_texts('Student Name', 'Harry Potter'))
    app.results.table.cells_of_row(2).should(have.exact_texts('Student Email', 'theboywholived@hogwarts.edu'))
    app.results.table.cells_of_row(3).should(have.exact_texts('Gender', 'Male'))
    app.results.table.cells_of_row(4).should(have.exact_texts('Mobile', '1234567890'))
    app.results.table.cells_of_row(5).should(have.exact_texts('Date of Birth', '31 July,1980'))
    app.results.table.cells_of_row(6).should(have.exact_texts('Subjects', 'Chemistry, Maths, Physics'))
    app.results.table.cells_of_row(7).should(have.exact_texts('Hobbies', 'Sports, Music, Reading'))
    app.results.table.cells_of_row(8).should(have.exact_texts('Picture', 'Bilbo_B.jpeg'))
    app.results.table.cells_of_row(9).should(have.exact_texts('Address', '4 Privet Drive'))
    app.results.table.cells_of_row(10).should(have.exact_texts('State and City', 'Uttar Pradesh Lucknow'))
