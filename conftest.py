from _pytest.fixtures import pytestconfig
from selenium import webdriver
import pytest
from Variables import Variables


driver = None

@pytest.fixture(scope='session')
def set_env(browser):
    print("Initiating Chrome driver")
    print("-----------------------------------------")
    print("Test Suite is started")
    if  browser in "chrome":
        driver = webdriver.Chrome()
    elif browser in "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.set_page_load_timeout(10)
    driver.get(Variables.base_url)
    driver.maximize_window()
    
    yield driver
    if driver is not None:
        print("-----------------------------------------")
        print("Test Suite is finished")
        driver.close()
        driver.quit()

@pytest.fixture(autouse=True)
def teardown(request):
    yield
    if request.session.testsfailed > 0:
        driver.save_screenshot(request.node.name+"_failure.png") 
        driver.get(Variables.base_url)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store")

@pytest.fixture(scope='session')
def browser(request):
    browser_value = request.config.option.browser
    if browser_value is None:
        pytest.skip()
    return browser_value
