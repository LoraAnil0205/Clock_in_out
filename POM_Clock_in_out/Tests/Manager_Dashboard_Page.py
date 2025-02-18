import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

from POM_Clock_in_out.Pages.Login_Page.Login_Valid_credentials import Login_valid
from POM_Clock_in_out.Pages.Manager_Dashboard_Page.Manager_Dashboard_Login import Manager_Dashboard_Login
from POM_Clock_in_out.Pages.Manager_Dashboard_Page.filter_Employee import ManagerDashboardFilterEmployee
from POM_Clock_in_out.Pages.Employee_Dashboard_Page.EDP_Clock_in_valid_inputs import EDP_Clock_in_valid
import HtmlTestRunner
from POM_Clock_in_out.Pages.Manager_Dashboard_Page.Empolyee_Record import ManagerDashboard_Employee_Record
from POM_Clock_in_out.Pages.Manager_Dashboard_Page.dashboard_displays_after_clockin import ManagerDashboardFilterEmployee

class FilterTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        chrome_driver_path = "C:/Users/ADMIN/PycharmProjects/clock_in_out/Drivers/chromedriver-win64/chromedriver.exe"
        service = Service(chrome_driver_path)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://44.204.48.219/")

    def test_Manager_Dashboard_Filter_Employee(self):
        driver = self.driver
        login_page = Login_valid(driver)
        manager_dashboard = Manager_Dashboard_Login(driver)
        filter_employee = ManagerDashboardFilterEmployee(driver)
        login_page.enter_username("DUMMYHEAD")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        filter_employee.filter_employee_by_id()
        time.sleep(4)
        filter_employee.validate_emp_list1("-- Select Employee --")


    def test_Manager_Dashboard_Employee_Record(self):
       driver = self.driver
       login_page = Login_valid(driver)
       employee_record = ManagerDashboard_Employee_Record(driver)
       login_page.enter_username("DUMMYHEAD")
       login_page.enter_password("Lora@1234")
       login_page.click_login()
       employee_record.Employee_Record()
       time.sleep(2)
       employee_record.Employee_dropdown_id()
       time.sleep(2)
       employee_record.empolyee_record_list("LORAIT00030")


    def test_Manager_Dashboard_displays_after_clockin(self):
        driver = self.driver
        login_page = Login_valid(driver)
        manager_dashboard = Manager_Dashboard_Login(driver)
        filter_employee = ManagerDashboardFilterEmployee(driver)
        records = ManagerDashboard_Employee_Record(driver)
        clockin = EDP_Clock_in_valid(driver)
        login_page.enter_username("DUMMY003")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        clockin.Employee_Clock_in()
        login_page.Logout_icon_button()
        login_page.Logout_link_button()
        time.sleep(2)
        login_page.enter_username("DUMMYHEAD")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        time.sleep(2)
        filter_employee.Employee_dispalys()
        time.sleep(4)
        filter_employee.Employee_dropdown_id_dispalys()
        time.sleep(2)
        filter_employee.empolyee_record_lists("DUMMY003")















    @classmethod
    def tearDown(cls):
       cls.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="C:\\Users\\ADMIN\\PycharmProjects\\clock_in_out\\Reports",
            report_title="Filter Test Report"
        )
    )
