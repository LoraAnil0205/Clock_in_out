from selenium.webdriver.common.by import By
from POM_Clock_in_out.Locators.Locators import Locators

class Manager_Dashboard_Login :
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


    def Manager_Dashboard(self, expected_text):
        print(f"Expected Text: {expected_text}")
        element = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Manager Dashboard']")
        actual_text = element.text
        print(f"Actual Text: {actual_text}")
        assert expected_text in actual_text, f"Login failed: Expected '{expected_text}' in '{actual_text}'"


    def Manager_Dashboard_contant(self, expected_text):
        print(f"Expected Text: {expected_text}")
        element = self.driver.find_element(By.XPATH,Locators.aasert)
        actual_text = element.text
        print(f"Actual Text: {actual_text}")
        assert expected_text in actual_text, f"Login failed: Expected '{expected_text}' in '{actual_text}'"




    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)