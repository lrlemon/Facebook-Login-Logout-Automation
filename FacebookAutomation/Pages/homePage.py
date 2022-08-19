from FacebookAutomation.Locators.locators import Locators
class HomePage():
    def __init__(self,driver):
        self.driver=driver

        self.find_friends_link_xpath=Locators.find_friends_link_xpath
        self.search_link_xpath=Locators.search_link_xpath
    def click_find_friends(self):
        self.driver.find_element(*self.find_friends_link_xpath).click()

    def check_search_link(self):
        search=self.driver.find_element(*self.search_link_xpath).is_enabled()
        print(search)
