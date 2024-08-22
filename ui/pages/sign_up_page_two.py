from playwright.sync_api import Page


class SignupPageTwo:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('h2.title.text-center[data-qa="account-created"]')

    def verify_account_created(self):
        return self.title.inner_text()
