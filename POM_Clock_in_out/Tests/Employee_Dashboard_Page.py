import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from POM_Clock_in_out.Pages.Employee_Dashboard_Page.EDP_Clock_in_valid_inputs import EDP_Clock_in_valid
from POM_Clock_in_out.Pages.Login_Page.Login_Valid_credentials import Login_valid
from POM_Clock_in_out.Pages.Employee_Dashboard_Page.EDP_Clock_out_After_Clock_in import EDP_Clock_out_After_Clock_in
from POM_Clock_in_out.Pages.Employee_Dashboard_Page.EDP_Clock_in_out_Time_Date import EDP_Clock_in_out_Time_Date
from POM_Clock_in_out.Pages.Employee_Dashboard_Page.EDP_ReLogin_visible_Time_Date import EDP_relogin_visible_Time_Date
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


    def test1_EDP_Clock_in_valid_inputs(self):
        driver = self.driver
        EDP_Clock_in = EDP_Clock_in_valid(driver)
        login_page = Login_valid(driver)
        login_page.enter_username("DUMMY007")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        EDP_Clock_in.Employee_Clock_in()
        EDP_Clock_in.take_screenshot("EDP_Clock_in_valid_inputs.png")
        EDP_Clock_in.EDP_Clock_in("Clock Out: Not clocked out yet")
        time.sleep(3)



    def test2_EDP_Clock_out_after_clock_in(self):
        driver = self.driver
        EDP_Clock_out=EDP_Clock_out_After_Clock_in(driver)
        login_page = Login_valid(driver)
        login_page.enter_username("DUMMY007")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        EDP_Clock_out.Employee_Clock_out()
        EDP_Clock_out.take_screenshot("EDP_Clock_out_after_clock_in.png")
        EDP_Clock_out.EDP_Clock_OUT("Clock Out")
        time.sleep(3)

    def test3_EDP_Clock_in_out_Time_Date(self):
        driver = self.driver
        Clock_in_out_Time_Date=EDP_Clock_in_out_Time_Date(driver)
        login_page = Login_valid(driver)
        login_page.enter_username("DUMMY006")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        Clock_in_out_Time_Date.EDP_Clock_in_out_Time_Date("Clock Out")
        time.sleep(3)
    def test4_EDP_relogin_visible_Time_Date(self):
        driver = self.driver
        relogin_visible_Time_Date=EDP_relogin_visible_Time_Date(driver)
        login_page = Login_valid(driver)
        login_page.enter_username("DUMMY006")
        login_page.enter_password("Lora@1234")
        login_page.click_login()
        relogin_visible_Time_Date.EDP_Clock_in_out_Relogin_Time_Date("Clock Out")
        time.sleep(3)

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





