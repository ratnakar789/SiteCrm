from selenium.webdriver.common.by import  By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, 'user_name')
        self.password_input = (By.ID, 'username_password')
        self.login_button = (By.ID, 'bigbutton')



    def login(self,username,password):
        self.driver.find_element(*self.username_input).clear() #"*" use for unpacking
        self.driver.find_element(*self.username_input).send_keys('will')
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys('will')
        self.driver.find_element(*self.login_button).click()
