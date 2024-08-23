import pytest
import allure


@pytest.mark.products
@allure.feature('Products')
@allure.story('Search Feature')
@allure.title('Product search')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_product(main_page, products_page):
    main_page.products_link.click()

    products_page.search_product_by_name('blue top')
    assert products_page.search_product
