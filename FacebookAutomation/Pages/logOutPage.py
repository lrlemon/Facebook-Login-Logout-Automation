from FacebookAutomation.Locators.locators import Locators

class LogOutPage():
    def __init__(self,driver) -> object:
        self.driver=driver

        self.profile_link_xpath=Locators.profile_link_xpath
        self.logOut_link_xpath=Locators.logOut_link_xpath

    def click_profile_link(self):
        self.driver.find_element(*self.profile_link_xpath).click()

    def click_logout_link(self):
        self.driver.find_element(*self.logOut_link_xpath).click()