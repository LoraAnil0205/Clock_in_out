from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class for dropdown handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM_Clock_in_out.Locators.Locators import Locators


class ManagerDashboardFilterEmployee:
    def __init__(self, driver):
        self.driver = driver


    def Employee_dispalys(self):

         employee_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.select_drop_down)))
         employee_dropdown.click()

    def Employee_dropdown_id_dispalys(self):
         select = Select(self.driver.find_element(By.ID, Locators.select_drop_down))
         select.select_by_value("DUMMY003")

    def empolyee_record_lists(self, expected_text):
        print(f"Expected Text: {expected_text}")
        elements = self.driver.find_elements(By.XPATH, Locators.employee_record)
        employee_list = [element.text for element in elements]
        print("Employee List:")
        for emp in employee_list:
            print(emp)
        assert any(expected_text in emp for emp in
                   employee_list), f"Validation failed: Expected '{expected_text}' in the employee list."

