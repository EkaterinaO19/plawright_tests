import pytest
import requests
from playwright.sync_api import sync_playwright, BrowserContext, Page

from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.sign_up_form_page import SignupFormPage
from ui.pages.sign_up_page_two import SignupPageTwo
from faker import Faker


fake = Faker()

BASE_URL = "https://automationexercise.com/"


# @pytest.fixture(scope="function")
# def cleanup_user_account():
#     def delete_account(user_email, user_password):
#         url = "https://automationexercise.com/api/deleteAccount"
#         params = {
#             'email': user_email,
#             'password': user_password
#         }
#         response = requests.delete(url, params=params)
#         if response.status_code == 200:
#             print("Account deleted successfully!")
#         else:
#             print(f"Failed to delete account. Status code: {response.status_code}, Response: {response.text}")
#
#     # Replace these with the credentials you are using in the test
#     user_email = 'standard_user@gmail.com'
#     user_password = '123456'
#     delete_account(user_email, user_password)


@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    page.goto(BASE_URL)
    return page


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture
def main_page(page: Page):
    return MainPage(page)


@pytest.fixture
def sign_up_form_page(page: Page):
    return SignupFormPage(page)


@pytest.fixture
def sign_up_page_two(page: Page):
    return SignupPageTwo(page)


@pytest.fixture
def register_user(main_page, login_page, sign_up_form_page, sign_up_page_two):
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

    return email, password, name
