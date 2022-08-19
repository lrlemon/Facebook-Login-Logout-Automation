import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from FacebookAutomation.Pages.logInPage import LoginPage
class BasePage(unittest.TestCase):
    driver: WebDriver=None

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\Program Files\DRIVERS\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.facebook.com/")
        time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        print("pass")
        cls.driver.close()

if __name__=='__main__':
    unittest.main()