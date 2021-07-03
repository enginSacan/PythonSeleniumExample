from selenium import webdriver
import pytest
from Variables import Variables

driver = webdriver.Chrome()

@pytest.fixture(scope='session')
def set_env():
    print("Initiating Chrome driver")
    print("-----------------------------------------")
    print("Test Suite is started")
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