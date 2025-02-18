import self
from selenium.webdriver.common.by import By
from POM_Clock_in_out.Locators.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Rest_password_valid_credentials:
    def __init__(self, driver):
        self.driver = driver
    def click_reset_password(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,Locators.Rest_Password_click))).click()

    def rest_empolyee_id(self,Rest_Employee_ID ):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.Rest_Employee_ID))).send_keys(Rest_Employee_ID)


    def old_password(self, Rest_Old_Password):

        self.driver.find_element(By.ID, Locators.Rest_Old_Password).send_keys(Rest_Old_Password)

    def new_password(self,Rest_New_Password ):

        self.driver.find_element(By.ID,Locators.Rest_New_Password).send_keys(Rest_New_Password)

    def confirm_password(self,Rest_Confirm_Password):

        self.driver.find_element(By.ID, Locators.Rest_Confirm_Password).send_keys(Rest_Confirm_Password)


    def reset_password_submit(self):

        self.driver.find_element(By.XPATH, Locators.Rest_Submit_button_xpath).click()

    def validate_login_success(self, expected_title):
        print(f"Expected Title: {expected_title}")
        actual_title = self.driver.title
        print(f"Actual Title: {actual_title}")
        assert expected_title in actual_title, f"Login failed: Expected '{expected_title}' in '{actual_title}'"

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)