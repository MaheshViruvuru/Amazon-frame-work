import pytest
from selenium import webdriver
options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe', options=options)


@pytest.fixture(scope='class')
def navigate_to_amazon(request):
    """Fixture to navigate to amazon web page"""
    # driver.maximize_window()
    driver.get("https://www.amazon.in/")
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
