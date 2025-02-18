from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class for dropdown handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM_Clock_in_out.Locators.Locators import Locators


class logout_employee_id :
    def __init__(self, driver):
        self.driver = driver


    def  logout_employee_id_is_valid(self, expected_text):
            print(f"Expected Text: {expected_text}")
            element = self.driver.find_element(By.XPATH,Locators.Logout_employee_id_xpath)
            actual_text = element.text
            print(f"Actual Text: {actual_text}")
            assert expected_text in actual_text, f"Login failed: Expected '{expected_text}' in '{actual_text}'"
