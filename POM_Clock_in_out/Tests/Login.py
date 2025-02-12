import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time
from POM_Clock_in_out.Pages.Login_Page import Login_page
from POM_Clock_in_out.Pages.Employee_Dashboard import Employee_Dashboard_Page
import HtmlTestRunner

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_driver_path = "C:/Users/ADMIN/PycharmProjects/clock_in_out/Drivers/chromedriver-win64/chromedriver.exe"
        service = Service(chrome_driver_path)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://44.204.48.219/")

        login_page = Login_page(driver)
        login_page.enter_username("LORAIT00030")
        login_page.enter_password("Qy9!Jt2z")
        login_page.click_login()

        dashboard_page = Employee_Dashboard_Page(driver)

        employee_name = dashboard_page.get_employee_name()
        print(f"Logged in as: {employee_name}")
        dashboard_page.open_profile_menu()
        dashboard_page.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\ADMIN\\PycharmProjects\\clock_in_out\\Reports"))

