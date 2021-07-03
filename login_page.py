from selenium.common.exceptions import NoSuchElementException
from BasePage import BasePage
from selenium.webdriver.common.by import By

from base_element import BaseElement
from Variables import Variables

class LoginPage(BasePage):

    @property
    def face_user_input(self):
        locator = (By.ID, Variables.facebook_user_name_id)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    @property
    def face_password_input(self):
        locator = (By.ID, Variables.facebook_password_id)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    @property
    def n11_login_button(self):
        locator = (By.XPATH, Variables.login_button_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    @property
    def face_login_button(self):
        locator = (By.XPATH, Variables.login_with_facebook_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    @property
    def face_submit_button(self):
        locator = (By.XPATH, Variables.facebook_submit_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    @property
    def n11_user_name(self):
        locator = (By.XPATH, Variables.user_name_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    def log_in_with_facebook(self):
        try:
            self.n11_login_button.click()
            self.face_login_button.click()
            all_windows = self.driver.window_handles
            self.driver.switch_to.window(all_windows[-1])
            self.face_user_input.input_text(Variables.user_text)
            self.face_password_input.input_text(Variables.pass_text)
            self.face_submit_button.click()
            self.driver.switch_to.window(all_windows[0])
            if self.n11_user_name.text in Variables.n11_user_name:
                print("Facebook LogIn Successful.")
                return True
            return False
        except NoSuchElementException as e:
            print("Automation cannot be login with facebook.") 
            print(format(e))

    