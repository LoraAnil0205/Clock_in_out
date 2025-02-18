import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from POM_Clock_in_out.Pages.Login_Page.Login_Valid_credentials import Login_valid
from POM_Clock_in_out.Pages.Login_Page.Login_Invalid_credentials import Login_Invalid
from POM_Clock_in_out.Pages.Login_Page.Login_Both_fields_empty import Login_Both_fields_empty
import HtmlTestRunner


class LoginTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        chrome_driver_path = "C:/Users/ADMIN/PycharmProjects/clock_in_out/Drivers/chromedriver-win64/chromedriver.exe"
        service = Service(chrome_driver_path)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://44.204.48.219/")

    def test1_login_valid_Credentials(self):
        driver = self.driver
        login_page = Login_valid(driver)
        login_page.enter_username("LORAIT00030")
        login_page.enter_password("Qy9!Jt2z")
        login_page.click_login()
        login_page.take_screenshot("Login_valid_Credentials.png")
        login_page.validate_login_success("Employee Dashboard")

    def test2_login_invalid_Credentials(self):
         driver = self.driver
         login_page = Login_Invalid(driver)
         login_page.enter_username("LORAIT00030")
         login_page.enter_password("12345667")
         login_page.click_login()
         login_page.take_screenshot("Login_invalid_Credentials.png")
         login_page.validate_login_success("Log in")

    def test3_login_both_fields_empty(self):
        driver = self.driver
        login_page = Login_Both_fields_empty(driver)
        login_page.click_login()
        login_page.take_screenshot("Login_both_fields_empty.png")
        login_page.validate_login_success("Reset Password?")









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






