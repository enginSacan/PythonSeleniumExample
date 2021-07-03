from BasePage import BasePage
import allure
from login_page import LoginPage
from Variables import Variables

@allure.title("This test checking login with facebook")
@allure.step        
def test_sign_up(set_env):
    login = LoginPage(set_env)
    assert login.log_in_with_facebook() == True
