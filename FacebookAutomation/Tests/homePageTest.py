import time
from FacebookAutomation.Tests.baseTestPage import BasePage
from FacebookAutomation.Pages.homePage import HomePage
from FacebookAutomation.Tests.logInTest import Business


class Business2(BasePage):
    def test_home_page(self):
        driver = self.driver

        homepage = HomePage(driver)

        Business.test_login_valid(self)
        homepage.click_find_friends()
        time.sleep(3)
        homepage.check_search_link()
        time.sleep(3)