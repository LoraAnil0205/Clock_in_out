import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import HtmlTestRunner
from POM_Clock_in_out.Pages.Reset_Password_Page.Rest_Password_Valid_credentials import Rest_password_valid_credentials
from POM_Clock_in_out.Pages.Login_Page.Login_Valid_credentials import Login_valid
from POM_Clock_in_out.Pages.Reset_Password_Page.Rest_Password_Page_Invalid_credentials import Rest_password_valid_credentials
from POM_Clock_in_out.Pages.Reset_Password_Page.Rest_Password_Both_fields_empty import Rest_password_Both_fileds_empty_credentials
from POM_Clock_in_out.Pages.Reset_Password_Page.Rest_password_Case_sensitivity_test import Rest_password_Rest_password_Case_sensitivity_credentials

class RestTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        chrome_driver_path = "C:/Users/ADMIN/PycharmProjects/clock_in_out/Drivers/chromedriver-win64/chromedriver.exe"
        service = Service(chrome_driver_path)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://44.204.48.219/")

    def test_1_Rest_Password_Valid_credentials(self):
        driver = self.driver
        login_page = Login_valid(driver)
        Rest_Password = Rest_password_valid_credentials(driver)
        Rest_Password.click_reset_password()
        Rest_Password.rest_empolyee_id("DUMMY004")
        Rest_Password.old_password("Lora@123")
        Rest_Password.new_password("Lora@1234")
        Rest_Password.confirm_password("Lora@1234")
        Rest_Password.reset_password_submit()
        Rest_Password.take_screenshot("Before_Rest_Password_Valid_credentials.png")
        login_page.enter_username("DUMMY004")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        time.sleep(2)
        login_page.validate_login_success("Employee Dashboard")
        Rest_Password.take_screenshot("After_Rest_Password_Valid_credentials.png")
        login_page.Logout_icon_button()
        login_page.Logout_link_button()

    def test_2_Rest_Password_Invalid_credentials(self):
        driver = self.driver
        Rest_Password = Rest_password_valid_credentials(driver)
        Rest_Password.click_reset_password()
        Rest_Password.rest_empolyee_id("DUMMY004")
        Rest_Password.old_password("Lora12")
        Rest_Password.new_password("Lora@123")
        Rest_Password.confirm_password("Lora@123")
        Rest_Password.reset_password_submit()
        Rest_Password.take_screenshot("Rest_Password_Invalid_credentials.png")
        Rest_Password.invalidate_Reset_success("The old password you entered is incorrect.")
        Rest_Password.reset_password_clear_employee_ID(driver)
        time.sleep(6)

        #invalid_Employee_ID
        Rest_Password.rest_empolyee_id("NEWEMP001")
        Rest_Password.old_password("Lora@123")
        Rest_Password.new_password("Lora@1234")
        Rest_Password.confirm_password("Lora@1234")
        Rest_Password.reset_password_submit()
        Rest_Password.take_screenshot("Rest_Password_Invalid_credentials.png")
        Rest_Password.invalidate_Reset_success("Employee ID does not exist")
        time.sleep(6)

        # invalid_password_conform_password
        Rest_Password.reset_password_clear_employee_ID(driver)
        Rest_Password.rest_empolyee_id("DUMMY004")
        Rest_Password.old_password("Lora@123")
        Rest_Password.new_password("Lora@1234")
        Rest_Password.confirm_password("Lora@12")
        Rest_Password.reset_password_submit()
        Rest_Password.take_screenshot("Rest_Password_Invalid_credentials.png")
        time.sleep(4)
        Rest_Password.invalidate_Reset_successsss( "New password and confirm password must match.")


    def test_3_Rest_Password_Both_fields_empty(self):
       driver = self.driver
       Rest_Password = Rest_password_Both_fileds_empty_credentials(driver)
       Rest_Password.click_reset_password()
       Rest_Password.rest_empolyee_id(" ")
       Rest_Password.old_password("")
       Rest_Password.new_password("")
       Rest_Password.confirm_password("")
       Rest_Password.reset_password_submit()
       Rest_Password.take_screenshot("Rest_Password_Both_fields_empty.png")
       Rest_Password.validate_login_success("Enter your details to reset your password")

    def test_4_Rest_password_Case_sensitivity_test(self):
        driver = self.driver
        Rest_Password = Rest_password_Rest_password_Case_sensitivity_credentials(driver)
        Rest_Password.click_reset_password()
        Rest_Password.rest_empolyee_id("dummy004")
        Rest_Password.old_password("Lora@123")
        Rest_Password.new_password("Lora@1234")
        Rest_Password.confirm_password("Lora@1234")
        Rest_Password.reset_password_submit()
        Rest_Password.take_screenshot("Rest_password_Case_sensitivity_test.png")
        Rest_Password.invalidate_Reset_success("Employee ID does not exist")


    def tearDown(cls):
        cls.driver.quit()




if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="C:\\Users\\ADMIN\\PycharmProjects\\clock_in_out\\Reports",
            report_title="Login Test Report"
        )
    )






