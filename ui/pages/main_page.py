from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_btn = page.locator("a[href='/login']")
        self.logout_btn = page.get_by_text("Logout")
        self.loggedin_msg = page.locator("//li/a[contains(., 'Logged in as')]")
        self.products_link = page.locator('//li/a[contains(normalize-space(text()), "Products")]')
        self.cart_link = page.locator('//li/a[contains(normalize-space(text()), "Cart")]')
        self.test_cases = page.locator('//li/a[contains(normalize-space(text()), "Test Cases")]')
        self.video_tutorials_link = page.locator('//li/a[contains(normalize-space(text()), "Video Tutorials")]')
        self.contact_link = page.locator('//li/a[contains(normalize-space(text()), "Contact us")]')
        self.api_link = page.locator('//li/a[contains(normalize-space(text()), "API Testing")]')

        self.subscription_input = page.locator('#susbscribe_email')
        self.success_msg_subscribe = page.locator('#success-subscribe > .alert-success.alert')

    def click_login_btn(self):
        self.login_btn.click()

    def click_logout(self):
        self.logout_btn.click()

    def get_url(self):
        return self.page.url

    def fill_subscription_email(self, email):
        self.subscription_input.fill(email)
