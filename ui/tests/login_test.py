import pytest
import allure
from faker import Faker

fake = Faker()

@pytest.mark.registration
def test_register_successful(main_page, login_page,sign_up_form_page, sign_up_page_two):
    name = fake.name()
    email = fake.email()
    password = '123456'

    main_page.click_login_btn()
    login_page.fill_username_input(name)
    login_page.fill_email_input_signup(email)
    login_page.signup()

    sign_up_form_page.check_gender()
    sign_up_form_page.fill_password(password)
    sign_up_form_page.select_days('1')
    sign_up_form_page.select_month("1")
    sign_up_form_page.select_year('1999')
    sign_up_form_page.fill_first_name('Alex')
    sign_up_form_page.fill_last_name('Hill')
    sign_up_form_page.fill_address("Washington")
    sign_up_form_page.fill_city('Seattle')
    sign_up_form_page.fill_state('Washington')
    sign_up_form_page.fill_zip('123456')
    sign_up_form_page.fill_number('89999999999')
    sign_up_form_page.click_create()

    account_text = sign_up_page_two.verify_account_created()
    assert "ACCOUNT CREATED!" in account_text, "Account creation was not successful."
    return email

@pytest.mark.login
@allure.feature('Login')
@allure.story('Login Feature')
@allure.title('Авторизаиця с корректными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(login_page, main_page, register_user):
    email, password, name = register_user

    main_page.click_login_btn()
    main_page.click_logout()
    login_page.fill_email_input_login(email)
    login_page.fill_password_login(password)
    login_page.login()

    assert main_page.loggedin_msg


@pytest.mark.login
@allure.feature('Login')
@allure.story('Login Feature')
@allure.title('Авторизаиця с некорректными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(login_page, main_page, register_user):

    main_page.click_login_btn()
    main_page.click_logout()
    login_page.fill_email_input_login('uncorrect@gmail.com')
    login_page.fill_password_login('000000')
    login_page.login()

    assert login_page.err_msg
