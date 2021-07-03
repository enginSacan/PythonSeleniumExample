class Variables:
    
    base_url = "https://www.n11.com/"
    
    # Facebook user password info
    user_text = "abc@abc.com"
    pass_text = "12345"

    # Login related paths for selenium (Try to get best locator even in xpath by using class, name or other attributes)
    login_button_xpath        = "//a[@class='btnSignIn']"
    login_with_facebook_xpath = "//div[@class='facebook_large medium facebookBtn  btnLogin']"
    facebook_user_name_id     = "email"
    facebook_password_id      = "pass"
    facebook_submit_xpath     = "//input[@name='login']"

    #n11 home page
    user_name_xpath         = "//a[@class='menuLink user']"
    n11_user_name           = "<username>"
    cosmetic_tab_xpath      = "//li[@class='catMenuItem']//a[@title='Kozmetik & Kişisel Bakım']" #"//span[@class='icon iconCosm']"
    parfum_tab_xpath        = "//li[@class='mainCat'][1]"
    confirm_popup_btn_xpath = "//span[@class='btn btnBlack confirm']"

    # category page
    search_box_xpath     = "//div[@class='filter-top-search']//input[@type='text']"
    search_button_id     = "allFilterSearchBtn"
    search_results_xpath = "//div[@class='itemize-img-holder']" 

    # product page
    favorite_button_xpath      = "//a[@class='addWishListBtn getWishList']"
    add_favorite_btn_id        = "addToFavouriteWishListBtn"
    favorites_list_page_xpath  = "//a[@class='icon iconFavorites']"
    favorites_list_xpath       = "//span[@class='icon-base heart-favorites-black']"
    product_name_xpath         = "//h1[@class='pro-title_main ']"
    fav_product_name_xpath     = "//h3[@itemprop='name']"

    # footer of the page
    all_links_at_footer_xpath = "//footer//div//a"
    brands_link_xpath         = "//a[@title='Markalar']"