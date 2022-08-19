import time

from FacebookAutomation.Pages.logInPage import LoginPage
from FacebookAutomation.Tests.baseTestPage import BasePage
from FacebookAutomation.Pages.homePage import HomePage


class Business(BasePage):
    def test_login_valid(self):
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username("01743208525")
        login.enter_password("********")
        time.sleep(3)
        login.click_login()
        time.sleep(10)




        '''
        b = HomePage(driver)
        b.check_search_link()
        time.sleep(10)
        '''
