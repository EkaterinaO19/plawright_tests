import pytest
import allure

@pytest.mark.menu
@allure.feature('Menu links')
@allure.story('Menu Feature')
@allure.title('Редирект на страницу products')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_products_page(main_page):
    main_page.products_link.click()
    assert main_page.get_url() == "https://automationexercise.com/products", "URL после нажатия на 'Products' не совпадает с ожидаемым."


@pytest.mark.menu
@allure.feature('Menu links')
@allure.story('Menu Feature')
@allure.title('Редирект на страницу Cart')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_cart_page(main_page):
    main_page.cart_link.click()
    assert main_page.get_url() == "https://automationexercise.com/view_cart", "URL после нажатия на 'Cart' не совпадает с ожидаемым."


@pytest.mark.menu
@allure.feature('Menu links')
@allure.story('Menu Feature')
@allure.title('Редирект на страницу test_cases')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_test_cases_page(main_page):
    main_page.test_cases.click()
    assert main_page.get_url() == "https://automationexercise.com/test_cases", "URL после нажатия на 'test_cases' не совпадает с ожидаемым."


@pytest.mark.menu
@allure.feature('Menu links')
@allure.story('Menu Feature')
@allure.title('Редирект на страницу api_list')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_test_cases_page(main_page):
    main_page.api_link.click()
    assert main_page.get_url() == "https://automationexercise.com/api_list", "URL после нажатия на 'api_list' не совпадает с ожидаемым."


@pytest.mark.menu
@allure.feature('Menu links')
@allure.story('Menu Feature')
@allure.title('Редирект на страницу video_tutorials')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_test_cases_page(main_page):
    main_page.video_tutorials_link.click()
    assert main_page.get_url() == "https://m.youtube.com/c/AutomationExercise", "URL после нажатия на 'video_tutorials' не совпадает с ожидаемым."



@pytest.mark.menu
@allure.feature('Menu links')
@allure.story('Menu Feature')
@allure.title('Редирект на страницу video_tutorials')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_video_tutorials_page(main_page):
    main_page.video_tutorials_link.click()
    assert main_page.get_url() == "https://www.youtube.com/c/AutomationExercise", "URL после нажатия на 'video_tutorials' не совпадает с ожидаемым."


@pytest.mark.menu
@allure.feature('Menu links')
@allure.story('Menu Feature')
@allure.title('Редирект на страницу contact_us')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_contact_us_page(main_page):
    main_page.contact_link.click()
    assert main_page.get_url() == "https://automationexercise.com/contact_us", "URL после нажатия на 'contact_us' не совпадает с ожидаемым."


