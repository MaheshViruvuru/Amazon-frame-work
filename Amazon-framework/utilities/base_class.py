import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')


class BasePage:

    def is_element_present(self, element, timeout=3):
        time.sleep(timeout)
        return element.is_displayed()
