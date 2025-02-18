from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM_Clock_in_out.Locators.Locators import Locators


class ManagerDashboard_Employee_Record:
    def __init__(self, driver):
        self.driver = driver


    def Employee_Record(self):

         employee_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.select_drop_down)))
         employee_dropdown.click()

    def Employee_dropdown_id(self):
         select = Select(self.driver.find_element(By.ID, Locators.select_drop_down))
         select.select_by_value("LORAIT00030")





    def empolyee_record_list(self, expected_text):
        print(f"Expected Text: {expected_text}")
        elements = self.driver.find_elements(By.XPATH, Locators.employee_record)
        employee_list = [element.text for element in elements]
        print("Employee List:")
        for emp in employee_list:
            print(emp)
        assert any(expected_text in emp for emp in
                   employee_list), f"Validation failed: Expected '{expected_text}' in the employee list."


