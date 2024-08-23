from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.view_product = page.locator('.choose > .nav > li > a').first
        self.search_product = page.locator('#search_product')
        self.search_btn = page.locator('#submit_search')
        self.search_res_title = page.get_by_role("heading", name="Searched Products")

    def click_view_product(self):
        self.view_product.click()

    def search_product_by_name(self, product_name):
        self.search_product.fill(product_name)
        self.search_btn.click()
