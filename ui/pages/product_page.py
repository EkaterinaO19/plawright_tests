from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".product-information > h2")
        self.price = page.locator('.product-information > span > span')
        self.quantity = page.locator('#quantity')

        self.name = page.locator('#name')
        self.email = page.locator('#email')
        self.review = page.locator('#review')

    def verify_title_has_text(self):
        title_text = self.title.text_content()
        assert title_text and title_text.strip(), "Title does not have text."

    def verify_price_has_text(self):
        price_text = self.price.text_content()
        assert price_text and price_text.strip(), "Price does not have text."

    def verify_quantity_has_text(self):
        quantity_value = self.quantity.get_attribute('value')
        assert quantity_value and quantity_value.strip(), "Quantity does not have a value."