import allure
import pytest
from faker import Faker


fake = Faker()


@pytest.mark.contact_form
@allure.feature('Contact form')
@allure.story('Contact form Feature')
@allure.title('Успешно отправленная Contact form')
@allure.severity(allure.severity_level.NORMAL)
def test_contact_form_success(main_page, contact_form_page):
    main_page.contact_link.click()
    contact_form_page.name.fill(fake.name())
    contact_form_page.email.fill(fake.email())
    contact_form_page.subject.fill(fake.text())
    contact_form_page.message.fill(fake.text())
    contact_form_page.upload_file()
    contact_form_page.submit_form()
    assert "Thank you for your message!" in contact_form_page.verify_success(), "Contact form was not sent successfully."
