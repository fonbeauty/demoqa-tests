import os

from selene import have, command
from selene.support.shared import browser


class Student:
    first_name = 'Bilbo'
    last_name = 'Baggins'
    email = 'bilbo@demo.qa'
    sex = 'Male'
    phone = '8008008080'
    birthday = {'day': '22', 'month': 'September', 'year': '1937'}
    subject = 'English'
    hobby = 'Reading'
    address = 'Shire, Rivendell'
    state = 'NCR'
    city = 'Delhi'
    photo = 'Bilbo_B.jpeg'


expected_date_of_birthday = f'{Student.birthday.get("day")} ' \
                            f'{Student.birthday.get("month")},' \
                            f'{Student.birthday.get("year")}'


def open_student_registration_form():
    browser.open('/automation-practice-form')
    # (
    #     browser.all('[id^=google_ads][id$=container__]').with_(timeout=10)
    #         .should(have.size_greater_than_or_equal(2))
    #         .perform(command.js.remove)
    # )


def test_sign_up():
    open_student_registration_form()

    browser.element('#firstName').type(Student.first_name)
    browser.element('#lastName').type(Student.last_name)
    browser.element('#userEmail').type(Student.email)
    gender = browser.element('#genterWrapper')
    gender.all('.custom-radio').element_by(have.exact_text(Student.sex)).click()
    browser.element('#userNumber').type(Student.phone)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element(f'[value="{Student.birthday.get("year")}"]').click()
    browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(Student.birthday.get("year"))).click()
    browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(Student.birthday.get("month"))).click()
    browser.element(f'.react-datepicker__day--0{Student.birthday.get("day")}').click()
    browser.element('#subjectsInput').type(Student.subject).press_tab()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(Student.hobby)).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(f'../resources/{Student.photo}'))
    browser.element('#currentAddress').type(Student.address)
    browser.element('#state').element('input').type(Student.state).press_tab()
    browser.element('#city').element('input').type(Student.city).press_tab()
    browser.element('#submit').perform(command.js.click)

    result_table_row = browser.elements("table tr")
    result_table_row.element(1).should(have.text(f'{Student.first_name} {Student.last_name}'))
    result_table_row.element(2).should(have.text(Student.email))
    result_table_row.element(3).should(have.text(Student.sex))
    result_table_row.element(4).should(have.text(Student.phone))
    result_table_row.element(5).should(have.text(expected_date_of_birthday))
    result_table_row.element(6).should(have.text(Student.subject))
    result_table_row.element(7).should(have.text(Student.hobby))
    result_table_row.element(8).should(have.text(Student.photo))
    result_table_row.element(9).should(have.text(Student.address))
    result_table_row.element(10).should(have.text(f'{Student.state} {Student.city}'))