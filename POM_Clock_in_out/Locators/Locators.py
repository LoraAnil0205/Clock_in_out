class Locators:

    #Login_page_Locators
    username_Textbox_id = "id_username"
    password_Textbox_id = "id_password"
    login_button_xpath = "//button[@type='submit']"
    logout_button_icon_xpath = "//i[@class='fas fa-user profile-icon']"
    logout_confirm_button_xpath ="//button[@type='submit']"

    #Rest_Password_valid_credentials
    Rest_Password_click ="//a[@class='reset-password']"
    Rest_Employee_ID="//input[@name='employee_id']"
    Rest_Old_Password="id_old_password"
    Rest_New_Password="id_new_password"
    Rest_Confirm_Password="id_confirm_password"
    Rest_Submit_button_xpath="//button[@type='submit']"

    #Employee_Dashboard_Page
    Clock_In_button_xpath ="//button[normalize-space()='Clock In']"
    Clock_Out_button_xpath ="//button[normalize-space()='Clock Out']"

    #Manager_Dashboard_page
    Manager_Dashboard_Page="//div[@class='table-container']//tr[1]//th"
    employeeDropdownID ="//select[@id='employee_id']"
    aasert ="//div[@class='table-container']//tr//th"
    monthDropdownID = "monthDropdownID"
    dateDropdownID = "dateDropdownID"
    tableRows = "//table[@id='dataTable']//tr"
    select_drop_down="employee_id"
    aasert_emplist="//select[@onchange='this.form.submit()']//option"
    employee_record="//table"


    #Logout_Page
    Logout_employee_id_xpath="//div[@class='dashboard-header']"
