from config.setup import init_driver
from selenium import webdriver
from pages.login import *
from pages.buzz import *
from pages.admin import *
from config.locator import LocLogin
from time import sleep

from dotenv import load_dotenv
import os

load_dotenv()
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
url = os.environ.get('URL')

#driver = init_driver()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)


login= Login(driver)
buzz = Buzz(driver)
admin = Admin(driver)
add_user= Add(driver)

#Login
login.input_username(username='Admin')
login.input_password(password='admin123')
login.click_login()


#Post Status
buzz.click_buzz()
buzz.input_status(input='HVAD HEDDER DU?')
buzz.click_post()

#Search User
admin.admin_menu()
admin.admin_username(admin_username='Admin')
admin.admin_user_role()
admin.admin_admin()
admin.admin_status()
admin.admin_enabled()
admin.admin_search()
sleep(3)

#Add User
add_user.admin_add()
add_user.add_user_role()
add_user.add_role_admin()
add_user.add_status()
add_user.add_status_enabled()
add_user.add_employee_name(add_employee_name='Ravi M B')
sleep(3)
add_user.click_employee_name()
add_user.add_username(add_username='Nurfa')
add_user.add_password(add_password='ABCdef123')
add_user.add_confirm_password(add_confirm_password='ABCdef123')
add_user.hide_menu()
driver.execute_script("window.scrollTo(0, 100)")
add_user.add_save()
sleep(10)
