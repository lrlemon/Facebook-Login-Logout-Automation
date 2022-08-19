from FacebookAutomation.Locators.locators import Locators

class LoginPage():
    def __init__(self,driver):
        self.driver=driver

        self.username_textbox_xpath=Locators.username_textbox_xpath
        self.password_textbox_xpath=Locators.password_textbox_xpath
        self.login_button_name=Locators.login_button_name

    def enter_username(self,username):
        self.driver.find_element(*self.username_textbox_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_textbox_xpath).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.login_button_name).click()