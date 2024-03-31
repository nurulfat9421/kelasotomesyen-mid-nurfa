
class LocLogin:
    login_username = 'username'
    login_password = 'password'
    login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

class LocBuzz:
    buzz_click = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]'
    buzz_input = 'textarea'
    buzz_submit = '//button[@type="submit"]'

class SearchUser:
    admin_menu = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]'
    admin_username = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
    admin_user_role= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div'
    admin_admin = '//*[contains(text(),"Admin")]'
    
    admin_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div'
    admin_enabled = '//*[contains(text(),"Enabled")]'
    admin_search = '//button[@type="submit"]'

class AddUser:
    admin_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    add_user_role =  '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div'
    add_role_admin = '//*[contains(text(),"Admin")]'
    add_employee_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input'
    click_employee_name = '//*[contains(text(),"Ravi M B")]'
    add_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div'
    add_status_enabled = '//*[contains(text(),"Enabled")]'
    add_username = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input'
    add_password = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'
    add_confirm_password = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'
    hide_menu = '//button[@type="button"]'
    add_save = '//button[@type="submit"]'
