from selenium.webdriver.common.by import By
from POM_Clock_in_out.Locators.Locators import Locators

class  Login_Both_fields_empty :
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):

        self.driver.find_element(By.ID,Locators.username_Textbox_id).send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(By.ID, Locators.password_Textbox_id).send_keys(password)

    def click_login(self):

        self.driver.find_element(By.XPATH, Locators.login_button_xpath).click()

    from selenium.webdriver.common.by import By

    def validate_login_success(self, expected_text):
        print(f"Expected Text: {expected_text}")
        element = self.driver.find_element(By.XPATH, "//div[@class='password-links']")
        actual_text = element.text
        print(f"Actual Text: {actual_text}")
        assert expected_text in actual_text, f"Login failed: Expected '{expected_text}' in '{actual_text}'"



    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)