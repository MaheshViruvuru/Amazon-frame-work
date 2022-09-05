import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utilities.base_class import BasePage


class AmazonHomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    amazon_logo = (By.XPATH, '//a[@id="nav-logo-sprites"]')
    menu = (By.XPATH, '//a[@id="nav-hamburger-menu"]')
    menu_list = (By.XPATH, '//ul[@data-menu-id="1"]//div[@class="hmenu-item hmenu-title "]')
    select_your_location = (By.XPATH, '//div[@id="glow-ingress-block"]//span')
    nav_belt_search_bar = (By.XPATH, '//form[@id="nav-search-bar-form"]')
    choose_language_button = (By.XPATH, '//a[@aria-label="Choose a language for shopping."]')
    nav_to_sign_in_page = (By.XPATH, '(//a[@data-nav-role="signin"])[1]')
    nav_to_orders_page = (By.XPATH, '//a[@id="nav-orders"]')
    nav_to_cart = (By.XPATH, '//a[@id="nav-cart"]')
    languages_list = (By.XPATH, '//span[@class="nav-text"]//span[1]')

    def get_amazon_logo(self):
        return self.driver.find_element(*AmazonHomePage.amazon_logo)

    def get_all_headers_menu_list(self):
        headers = ['Trending', 'Digital Content And Devices', 'Shop By Department', 'Programs & Features', 'Help & Settings']

        self.driver.find_element(*AmazonHomePage.menu).click()
        headers_list_in_menu = self.driver.find_elements(*AmazonHomePage.menu_list)
        headers_list = []
        for header in headers_list_in_menu:
            headers_list.append(header.text)
        assert headers == headers_list, "menu headers are not as expected"
        return True

    def check_home_page_navigation_belt(self):
        select_location_block_texts = self.driver.find_elements(*AmazonHomePage.select_your_location)
        select_location_block_texts_list = ["Hello", "Select your address"]
        for i in range(len(select_location_block_texts)):
            assert select_location_block_texts[i].text == select_location_block_texts_list[i], \
                "Element mismatch"
        search_bar = self.driver.find_element(*AmazonHomePage.nav_belt_search_bar)
        choose_lang_button = self.driver.find_element(*AmazonHomePage.choose_language_button)
        sign_in_button = self.driver.find_element(*AmazonHomePage.nav_to_sign_in_page)
        orders_page_button = self.driver.find_element(*AmazonHomePage.nav_to_orders_page)
        cart_button = self.driver.find_element(*AmazonHomePage.nav_to_cart)
        assert self.is_element_present(search_bar), "Search bar is not present"
        assert self.is_element_present(sign_in_button), \
            "Navigate to sign in page button is not present"
        assert self.is_element_present(choose_lang_button), \
            "Navigate to choose language button is not present"
        assert self.is_element_present(orders_page_button), \
            "Navigate to orders page button is not present"
        assert self.is_element_present(cart_button), \
            "Navigate to cart page button is not present"

        return True

    def check_change_language_drop_down(self):
        time.sleep(15)
        actions = ActionChains(self.driver)
        choose_lang_button = self.driver.find_element(*AmazonHomePage.choose_language_button)
        actions.move_to_element(choose_lang_button)
        languages_list = self.driver.find_elements(*AmazonHomePage.languages_list)
        languages = []
        for language in languages_list:
            languages.append(language.text)
            if len(languages) >= 8:
                break

        return languages





