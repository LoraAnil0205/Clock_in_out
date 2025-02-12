from selenium.webdriver.common.by import By
from POM_Clock_in_out.Locators.Locators import Locators

class Employee_Dashboard_Page:

    def __init__(self, driver):
        self.driver = driver

    def open_profile_menu(self):

        self.driver.find_element(By.XPATH, Locators.profile_icon).click()

    def get_employee_name(self):

        try:
            return self.driver.find_element(By.XPATH, Locators.employee_name).text
        except:
            return "Employee name not found"

    def logout(self):

        self.driver.find_element(By.XPATH, Locators.log_out).click()
