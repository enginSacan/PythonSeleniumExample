import allure
from footer import FooterPage

@allure.title("This test checking the links at the footer in different pages")
@allure.step        
def test_cosmetic_page(set_env):
    footer = FooterPage(set_env)
    assert footer.get_footer_links() == True
    assert footer.go_to_brands_check_links() == True