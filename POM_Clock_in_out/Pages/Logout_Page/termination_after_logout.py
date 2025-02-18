from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class for dropdown handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM_Clock_in_out.Locators.Locators import Locators


class termination_after_logout:
    def __init__(self, driver):
        self.driver = driver


