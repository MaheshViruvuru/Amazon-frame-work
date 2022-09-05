import pytest
from Pageobjects.amazon_home_page import AmazonHomePage
from utilities.base_class import BasePage


@pytest.mark.usefixtures('navigate_to_amazon')
class TestAmazonHomePage:
    def test_navigate_amazon_home_page(self):
        amazon_home_page = AmazonHomePage(self.driver)
        amazon_logo = amazon_home_page.get_amazon_logo()
        assert amazon_logo.is_displayed(), "Amazon logo is not displayed"
        print("Log in successful")
        assert amazon_home_page.get_all_headers_menu_list(), "Unable to get menu headers"

    def test_home_page_navigation_belt(self):
        amazon_home_page = AmazonHomePage(self.driver)
        assert amazon_home_page.check_home_page_navigation_belt(), "Home page navigation belt is not as expected"

    def test_check_change_language_drop_down(self):
        amazon_home_page = AmazonHomePage(self.driver)
        print(amazon_home_page.check_change_language_drop_down())
