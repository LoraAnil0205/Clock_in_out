from POM_Clock_in_out.Pages.Logout_Page.redirect_to_the_login_page import logout_page
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from POM_Clock_in_out.Pages.Login_Page.Login_Valid_credentials import Login_valid
import HtmlTestRunner
from POM_Clock_in_out.Pages.Logout_Page.termination_after_logout import termination_after_logout
from POM_Clock_in_out.Pages.Logout_Page.Logout_Employee_ID_is_valid import  logout_employee_id


class FilterTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        chrome_driver_path = "C:/Users/ADMIN/PycharmProjects/clock_in_out/Drivers/chromedriver-win64/chromedriver.exe"
        service = Service(chrome_driver_path)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://44.204.48.219/")



    def test_Logout(self):
        driver = self.driver
        login_page = Login_valid(driver)
        login_page.enter_username("DUMMY003")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        login_page.Logout_icon_button()
        login_page.Logout_link_button()
        login_page.enter_username("DUMMY003")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        login_page.validate_login_success("Employee Dashboard")


    def test_termination_after_logout(self):
        driver = self.driver
        logout_page = termination_after_logout(driver)
        login_page = Login_valid(driver)
        login_page.enter_username("DUMMY003")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        login_page.Logout_icon_button()
        login_page.Logout_link_button()
        time.sleep(3)
        driver.back()
        login_page.take_screenshot("termination_after_logout.png")
        login_page.validate_login_success("Employee Dashboard")


    def test_Logout_Employee_ID_is_valid(self):
        driver = self.driver
        logout_page = logout_employee_id(driver)
        logout= logout_employee_id(driver)
        login_page = Login_valid(driver)
        login_page.enter_username("DUMMY003")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        logout.logout_employee_id_is_valid("Welcome, dummy3")
















    @classmethod
    def tearDown(cls):
      cls.driver.quit()





if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="C:\\Users\\ADMIN\\PycharmProjects\\clock_in_out\\Reports",
            report_title="Login Test Report"
        )
    )

