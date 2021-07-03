from selenium.common.exceptions import NoSuchElementException
from base_element import BaseElement
from Variables import Variables
from BasePage import BasePage
from selenium.webdriver.common.by import By

class FooterPage(BasePage):

    @property
    def brands_link(self):
        locator = (By.XPATH, Variables.brands_link_xpath)
        return BaseElement(self.driver, by=locator[0], value=locator[1])
    
    

    def get_footer_links(self):
        try:
            links = self.driver.find_elements_by_xpath(Variables.all_links_at_footer_xpath)
            with open("linkList.txt", "w", encoding="utf-8") as file:
                for link in links:
                    if link.text in " ":
                        continue
                    file.write(link.text+"\n")
            file.close()
            return True
            
        except NoSuchElementException as e:
            print("Automation cannot get links name.") 
            print(format(e))
        
    def go_to_brands_check_links(self):
        try:
            brand_link_txts = []
            self.brands_link.click()
            brand_links = self.driver.find_elements_by_xpath(Variables.all_links_at_footer_xpath)
            with open("linkList.txt", "r", encoding="utf-8") as f:
                list_lines = f.readlines()
            f.close()
            set_list_lines = set(list_lines)
            for brand_link in brand_links:
                brand_link_txts.append(brand_link.text+"\n")
            set_brand_links = set(brand_link_txts)
            difference = set_list_lines.difference(set_brand_links)
            print ("Found: "+str(difference))
            if len(difference) == 0:
                return True
            return False

        except NoSuchElementException as e:
            print("Automation cannot get links name.") 
            print(format(e))