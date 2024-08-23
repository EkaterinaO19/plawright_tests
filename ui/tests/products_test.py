import pytest
import allure


@pytest.mark.products
@allure.feature('Products')
@allure.story('Products Feature')
@allure.title('Product card')
@allure.severity(allure.severity_level.CRITICAL)
def test_navigation_tot_product_card(main_page, products_page, product_page):
    main_page.products_link.click()

    products_page.click_view_product()

    product_page.verify_title_has_text()
    product_page.verify_price_has_text()
    product_page.verify_quantity_has_text()
