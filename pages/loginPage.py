from Locators.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, usn):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(usn)

    def enter_password(self, pwd):
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(pwd)

    def click_login_button(self):
        self.driver.find_element_by_id(Locators.login_button_id).click()
