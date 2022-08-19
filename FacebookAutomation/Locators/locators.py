from selenium.webdriver.common.by import By


class Locators():
    #login page
    username_textbox_xpath=(By.XPATH,"//input[@type='text']")
    password_textbox_xpath=(By.XPATH,"//*[@id='pass']")
    login_button_name=(By.NAME,"login")

    #logout page
    profile_link_xpath = (By.XPATH, "((//div[@class='alzwoclg om3e55n1'])[1]/div)[1]")
    logOut_link_xpath = (By.XPATH, "//span[contains(text(), 'Log Out')]")


    #Find friends
    find_friends_link_xpath=(By.XPATH,"//span[@class='b6ax4al1 lq84ybu9 hf30pyar om3e55n1']")
    search_link_xpath=(By.XPATH,"// input[ @ dir = 'ltr']")
