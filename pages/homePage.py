import time
from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(Locators.logout_button).click()
