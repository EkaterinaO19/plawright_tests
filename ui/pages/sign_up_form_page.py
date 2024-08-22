from playwright.sync_api import Page, expect


class SignupFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.gender = page.get_by_label("Mr.")
        self.password = page.get_by_label("Password *")
        self.days = page.locator("#days")
        self.months = page.locator("#months")
        self.years = page.locator("#years")
        self.firstname = page.get_by_label("First name *")
        self.lastname = page.get_by_label("Last name *")
        self.address = page.get_by_label("Address * (Street address, P.")
        self.state = page.get_by_label("State *")
        self.city = page.get_by_label("City *")
        self.zip = page.locator("#zipcode")
        self.number = page.get_by_label("Mobile Number *")
        self.create_btn = page.get_by_role("button", name="Create Account")

    def check_gender(self):
        self.gender.check()

    def fill_password(self, password):
        self.password.fill(password)

    def select_days(self, day):
        self.days.select_option(day)

    def select_month(self, month):
        self.months.select_option(month)

    def select_year(self, year):
        self.years.select_option(year)

    def fill_first_name(self, name):
        self.firstname.fill(name)

    def fill_last_name(self, lastname):
        self.lastname.fill(lastname)

    def fill_address(self, address):
        self.address.fill(address)

    def fill_state(self, state):
        self.state.fill(state)

    def fill_city(self, city):
        self.city.fill(city)

    def fill_zip(self, zip):
        self.zip.fill(zip)

    def fill_number(self, number):
        self.number.fill(number)

    def click_create(self):
        self.create_btn.click()
