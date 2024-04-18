from QualityLaboratoryTestTask.python.ui.pages.Main_Page import Main_Page
from QualityLaboratoryTestTask.tests.ui.configuration.conftest import driver


class Tests:
    def test_1(self, driver):
        base_page = Main_Page(driver)
        name = base_page.generate_random_name()
        mail = base_page.generate_random_email()
        address1 = base_page.generate_random_address()
        address2 = base_page.generate_random_address()
        base_page.fill_field("Full Name", name)
        base_page.fill_field("Email", mail)
        base_page.fill_field("Current Address", address1)
        base_page.fill_field("Permanent Address", address2)
        base_page.wait(2)
        base_page.click_button("Submit")
        base_page.check_field_is_filled_value("name", name)
        base_page.check_field_is_filled_value("email", mail)
        base_page.check_field_is_filled_value("currentAddress", address1)
        base_page.check_field_is_filled_value("permanentAddress", address2)
