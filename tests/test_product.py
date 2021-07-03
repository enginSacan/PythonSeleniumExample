import allure
from cosmetic_page import CosmeticPage

@allure.title("This test checking add favorite a product in parfum section")
@allure.step        
def test_cosmetic_page(set_env):
    cosmetic = CosmeticPage(set_env)
    assert cosmetic.choose_fav_product_in_parfum("Lacoste") == True