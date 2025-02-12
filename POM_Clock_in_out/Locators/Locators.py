class Locators:

    #Login_page_Locators
    username_Textbox_id = "id_username"
    password_Textbox_id = "id_password"
    login_button_xpath = "//button[@type='submit']"

    #Employee_Dashboard_Locators
    profile_icon = "//i[@class='fas fa-user profile-icon']"
    employee_name = "//div[@class='dashboard-header']/h1"
    log_out = "//button[contains(text(), 'Logout')]"
