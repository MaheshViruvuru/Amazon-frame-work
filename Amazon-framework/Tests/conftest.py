import pytest
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')


@pytest.fixture()
def navigate_to_amazon(request):
    """Fixture to navigate to amazon web page"""
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
