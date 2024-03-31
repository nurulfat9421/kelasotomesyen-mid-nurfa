from selenium.webdriver.common.by import By
from config.locator import LocBuzz

class Buzz:
    def __init__(self, driver):
        self.driver=driver
    
    def click_buzz(self):
        self.driver.find_element(By.XPATH, LocBuzz.buzz_click).click()

    def input_status(self, input):
        self.driver.find_element(By.TAG_NAME, LocBuzz.buzz_input).send_keys(input)

    def click_post(self):
        self.driver.find_element(By.XPATH, LocBuzz.buzz_submit).click()