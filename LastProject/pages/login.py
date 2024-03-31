from selenium.webdriver.common.by import By
from config.locator import LocLogin

class Login:
    def __init__(self,driver):
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(By.NAME,LocLogin.login_username).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.NAME,LocLogin.login_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,LocLogin.login_button).click()