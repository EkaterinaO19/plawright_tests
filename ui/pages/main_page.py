from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_btn = page.locator("a[href='/login']")
        self.logout_btn = page.get_by_text("Logout")
        self.loggedin_msg = page.locator("//li/a[contains(., 'Logged in as')]")

    def click_login_btn(self):
        self.login_btn.click()

    def click_logout(self):
        self.logout_btn.click()
