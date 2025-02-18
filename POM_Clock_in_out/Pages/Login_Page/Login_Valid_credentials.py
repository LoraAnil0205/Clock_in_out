from selenium.webdriver.common.by import By
from POM_Clock_in_out.Locators.Locators import Locators

class Login_valid:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):

        self.driver.find_element(By.ID,Locators.username_Textbox_id).send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(By.ID, Locators.password_Textbox_id).send_keys(password)

    def click_login(self):

        self.driver.find_element(By.XPATH, Locators.login_button_xpath).click()
    def Logout_icon_button(self):

        self.driver.find_element(By.XPATH,Locators.logout_button_icon_xpath).click()

    def Logout_link_button(self):

        self.driver.find_element(By.XPATH,Locators.login_button_xpath).click()


    def validate_login_success(self, expected_title):
        print(f"Expected Title: {expected_title}")
        actual_title = self.driver.title
        print(f"Actual Title: {actual_title}")
        assert expected_title in actual_title, f"Login failed: Expected '{expected_title}' in '{actual_title}'"

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)