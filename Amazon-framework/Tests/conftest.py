import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
options = webdriver.ChromeOptions()
options.headless = True


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="amazon")


@pytest.fixture()
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture()
def get_url(request):
    _url = request.config.getoption("--url")
    return _url


@pytest.fixture()
def navigate_to_amazon(request, get_browser, get_url):
    """Fixture to navigate to amazon web page"""
    driver = None
    if get_browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        print("installed driver successfully")
    elif get_browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
        print("installed driver successfully")
    driver.maximize_window()
    driver.get(f"https://www.{get_url}.in/")
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
