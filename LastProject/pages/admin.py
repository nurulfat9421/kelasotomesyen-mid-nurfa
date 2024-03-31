from selenium.webdriver.common.by import By
from config.locator import SearchUser
from config.locator import AddUser
from selenium import webdriver


class Admin:
    def __init__(self, driver):
        self.driver=driver
    
    def admin_menu(self):
        self.driver.find_element(By.XPATH, SearchUser.admin_menu).click()

    def admin_username(self, admin_username):
        self.driver.find_element(By.XPATH, SearchUser.admin_username).send_keys(admin_username)

    def admin_user_role(self):
        self.driver.find_element(By.XPATH, SearchUser.admin_user_role).click()

    def admin_admin(self):
        self.driver.find_element(By.XPATH, SearchUser.admin_admin).click()
    def admin_status(self):
        self.driver.find_element(By.XPATH, SearchUser.admin_status).click()
    def admin_enabled(self):
        self.driver.find_element(By.XPATH, SearchUser.admin_enabled).click()
    def admin_search(self):
        self.driver.find_element(By.XPATH, SearchUser.admin_search).click()

class Add:
    def __init__(self, driver):
        self.driver=driver

    def admin_add(self):
        self.driver.find_element(By.XPATH, AddUser.admin_add).click()

    def add_user_role(self):
        self.driver.find_element(By.XPATH, AddUser.add_user_role).click()

    def add_role_admin(self):
        self.driver.find_element(By.XPATH, AddUser.add_role_admin).click()

    def add_status(self):
        self.driver.find_element(By.XPATH, AddUser.add_status).click()

    def add_status_enabled(self):
        self.driver.find_element(By.XPATH, AddUser.add_status_enabled).click()
    
    def add_employee_name(self, add_employee_name):
        self.driver.find_element(By.XPATH, AddUser.add_employee_name).send_keys(add_employee_name)

    def click_employee_name(self):
        self.driver.find_element(By.XPATH, AddUser.click_employee_name).click()

    def add_username(self, add_username):
        self.driver.find_element(By.XPATH, AddUser.add_username).send_keys(add_username)

    def add_password(self, add_password):
        self.driver.find_element(By.XPATH, AddUser.add_password).send_keys(add_password)

    def add_confirm_password(self, add_confirm_password):
        self.driver.find_element(By.XPATH, AddUser.add_confirm_password).send_keys(add_confirm_password)

    def hide_menu(self):
        self.driver.find_element(By.XPATH, AddUser.hide_menu).click()

    def add_save(self):
        self.driver.find_element(By.XPATH, AddUser.add_save).click()