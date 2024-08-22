from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Name")
        self.email_input_signup = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.sign_up_btn = page.get_by_role("button", name="Signup")

        self.email_input_login = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")

        self.err_msg = page.locator("//p[contains(text(), 'Your email or password is incorrect!')]")

    def fill_email_input_login(self, email):
        self.email_input_login.fill(email)

    def fill_password_login(self, password):
        self.password.fill(password)

    def login(self):
        self.login_btn.click()

    def fill_username_input(self, username):
        self.username_input.fill(username)

    def fill_email_input_signup(self, email):
        self.email_input_signup.fill(email)

    def signup(self):
        self.sign_up_btn.click()
