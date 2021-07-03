from selenium.common.exceptions import NoSuchElementException
from BasePage import BasePage
from selenium.webdriver.common.by import By

from base_element import BaseElement
from Variables import Variables

class CosmeticPage(BasePage):
    @property
    def cosmetic_tab(self):
        locator = (By.XPATH, Variables.cosmetic_tab_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def parfum_tab(self):
        locator = (By.XPATH, Variables.parfum_tab_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def search_box(self):
        locator = (By.XPATH, Variables.search_box_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    
    @property
    def search_button(self):
        locator = (By.ID, Variables.search_button_id)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    @property
    def favorite_button(self):
        locator = (By.XPATH, Variables.favorite_button_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    
    @property
    def product_name(self):
        locator = (By.XPATH, Variables.product_name_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def favorites_page(self):
        locator = (By.XPATH, Variables.favorites_list_page_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    
    @property
    def add_favorite_button(self):
        locator = (By.ID, Variables.add_favorite_btn_id)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    
    @property
    def favorites_list(self):
        locator = (By.XPATH, Variables.favorites_list_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    
    @property
    def fav_product_name(self):
        locator = (By.XPATH, Variables.fav_product_name_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    
    @property
    def pop_up_confirm(self):
        locator = (By.XPATH, Variables.confirm_popup_btn_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    def choose_fav_product_in_parfum(self,product):
        try:
            self.driver.get(Variables.base_url)
            self.cosmetic_tab.click()
            self.parfum_tab.click()
            self.search_box.input_text(product)
            self.search_button.click()
            search_results = self.driver.find_elements_by_xpath(Variables.search_results_xpath)
            search_results[6].click()
            product_name_txt = self.product_name.text
            self.favorite_button.click()
            self.add_favorite_button.click()
            self.pop_up_confirm.click()
            self.favorites_page.click()
            self.favorites_list.click()
            fav_product_name_txt = self.fav_product_name.text
            if product_name_txt in fav_product_name_txt:
                return True
            return False
        except NoSuchElementException as e:
            print("Automation cannot be add product to favorite") 
            print(format(e))



