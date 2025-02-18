from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class for dropdown handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM_Clock_in_out.Locators.Locators import Locators


class ManagerDashboardFilterEmployee:
    def __init__(self, driver):
        self.driver = driver



    def filter_employee_by_id(self):

        employee_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.select_drop_down)))
        employee_dropdown.click()


    def validate_emp_list1(self, expected_text):
        print(f"Expected Text: {expected_text}")
        elements = self.driver.find_elements(By.XPATH, Locators.aasert_emplist)
        employee_list = [element.text for element in elements]
        print("Employee List:")
        for emp in employee_list:
            print(emp)
        assert any(expected_text in emp for emp in
                   employee_list), f"Validation failed: Expected '{expected_text}' in the employee list."



    #     # Select the first employee (adjust index if necessary)
    #     select = Select(employee_dropdown)
    #     select.select_by_index(0)
    #
    #     # Verify filtered data
    #     self.verify_table_data()
    #
    # def filter_by_month(self):
    #     # Wait for the month filter dropdown and select a month
    #     month_dropdown = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, Locators.monthDropdownID)))
    #     select = Select(month_dropdown)
    #     select.select_by_index(1)  # Change index as needed
    #
    #     # Verify filtered data
    #     self.verify_table_data()
    #
    # def filter_by_date(self):
    #     # Wait for the date filter dropdown and select a date
    #     date_dropdown = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, Locators.dateDropdownID)))
    #     select = Select(date_dropdown)
    #     select.select_by_index(1)  # Change index as needed
    #
    #     # Verify filtered data
    #     self.verify_table_data()
    #
    # def verify_table_data(self):
    #     # Verify if the table rows are filtered correctly
    #     rows = self.driver.find_elements(By.XPATH, Locators.tableRows)
    #     if len(rows) > 1:  # Check if the data is populated
    #         print("Data is filtered correctly.")
    #     else:
    #         print("No data found after filtering.")
    #





