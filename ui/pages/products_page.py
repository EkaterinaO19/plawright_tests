from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.view_product = page.locator('.choose > .nav > li > a').first

    def click_view_product(self):
        self.view_product.click()
