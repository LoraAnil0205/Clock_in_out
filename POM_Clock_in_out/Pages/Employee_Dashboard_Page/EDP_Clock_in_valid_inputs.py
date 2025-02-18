from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from POM_Clock_in_out.Locators.Locators import Locators

class EDP_Clock_in_valid :
    def __init__(self, driver):
        self.driver = driver

    def Employee_Clock_in(self):

          WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, Locators.Clock_In_button_xpath))).click()





    def EDP_Clock_in(self, expected_text):
        print(f"Expected Text: {expected_text}")
        element = self.driver.find_element(By.XPATH,"//p[normalize-space()='Clock Out: Not clocked out yet']")
        actual_text = element.text
        print(f"Actual Text: {actual_text}")
        assert expected_text in actual_text, f"Login failed: Expected '{expected_text}' in '{actual_text}'"



    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)
