import pytest
import allure
from faker import Faker

fake = Faker()


@pytest.mark.subscription
@allure.feature('Subscription')
@allure.story('Subscription Feature')
@allure.title('Check Subscription')
@allure.severity(allure.severity_level.CRITICAL)
def test_subscription_success(main_page):
    main_page.fill_subscription_email(fake.email())
    assert "You have been successfully subscribed!" in main_page.success_msg_subscribe.text_content(), "Subscription message not found or incorrect."