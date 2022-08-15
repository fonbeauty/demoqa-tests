import allure
from selene import have

from demoqa.model.application_manager import app
from selene.support.shared import browser
from demoqa.data import User
from utils import attach


@allure.feature('Регистрация студента')
@allure.story('Заполнение формы данных регистрации студента')
def test_register_student(browser_management, add_allure_attach):
    with allure.step('Подготовка данных студента'):
        app.given_student_registration_form_opened()
        harry_potter = User(
            first_name='Harry',
            last_name='Potter',
            subjects=['Chemistry', 'Maths', 'Physics'],
            email='theboywholived@hogwarts.edu',
            gender='Male',
            mobile_number='1234567890',
            birthday_year=1980,
            birthday_month='July',
            birthday_day=31,
            hobbi_sports=True,
            hobbi_reading=True,
            hobbi_music=True,
            picture='Bilbo_B.jpeg',
            address='4 Privet Drive',
            state='Uttar Pradesh',
            city='Lucknow'
        )

    with allure.step('Заполнение данных студента'):
        app.form.fill_form(harry_potter)
        app.form.submit()

    with allure.step('Проверка данных на модальном окне'):
        app.results.should_have_row_with_exact_texts('Student Name', 'Harry Potter')

        app.results.table.cells_of_row(1).should(have.exact_texts('Student Name', 'Harry Potter'))
        app.results.table.cells_of_row(2).should(have.exact_texts('Student Email', 'theboywholived@hogwarts.edu'))
        app.results.table.cells_of_row(3).should(have.exact_texts('Gender', 'Male'))
        app.results.table.cells_of_row(4).should(have.exact_texts('Mobile', '1234567890'))
        app.results.table.cells_of_row(5).should(have.exact_texts('Date of Birth', '31 July,1980'))
        app.results.table.cells_of_row(6).should(have.exact_texts('Subjects', 'Chemistry, Maths, Physics'))
        app.results.table.cells_of_row(7).should(have.exact_texts('Hobbies', 'Sports, Reading, Music'))
        app.results.table.cells_of_row(8).should(have.exact_texts('Picture', 'Bilbo_B.jpeg'))
        app.results.table.cells_of_row(9).should(have.exact_texts('Address', '4 Privet Drive'))
        app.results.table.cells_of_row(10).should(have.exact_texts('State and City', 'Uttar Pradesh Lucknow'))

    # attach.add_html(browser)
    # attach.add_logs(browser)
    # attach.add_screenshot(browser)
    # attach.add_video(browser)



