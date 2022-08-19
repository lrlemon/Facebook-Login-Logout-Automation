import time
from FacebookAutomation.Tests.baseTestPage import BasePage
from FacebookAutomation.Tests.logInTest import Business
from FacebookAutomation.Pages.logOutPage import LogOutPage
from FacebookAutomation.Tests.logInTest import Business

class Business1(BasePage):
    def test_logout_valid(self):
        driver = self.driver
        logout = LogOutPage(driver)

        Business.test_login_valid(self)

        logout.click_profile_link()
        time.sleep(3)
        logout.click_logout_link()
        time.sleep(3)


