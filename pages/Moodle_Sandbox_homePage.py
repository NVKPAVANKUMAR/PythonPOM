from Locators.locators import Locators
import time


class Moodle_HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        time.sleep(3)
        self.driver.find_element_by_id(Locators.admin_user_dropdown).click()
        self.driver.find_element_by_xpath(Locators.logout_option).click()
