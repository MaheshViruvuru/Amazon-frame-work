import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


@pytest.fixture(scope='class')
def navigate_to_amazon(request):
    """Fixture to navigate to amazon web page"""
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
