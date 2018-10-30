import json
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from pages.homePage import HomePage
from pages.loginPage import LoginPage
import configparser
import HtmlTestRunner


def parse_config(self, header, parameter):
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')
    return config.get(header, parameter)


def read_json(self, data_source):
    with open(data_source) as datafile:
        data = json.load(datafile)
        return data


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test01_login_valid(self):
        driver = self.driver
        data = read_json(self, "configuration/config.json")
        driver.get(data['CREDENTIALS']['URL'])
        login = LoginPage(driver)
        login.enter_username(data['CREDENTIALS']['USERNAME'][1])
        login.enter_password(data['CREDENTIALS']['PASSWORD'][1])
        login.click_login_button()
        homepage = HomePage(driver)
        homepage.click_logout_button()
        time.sleep(2)

    def test02_login_invalid(self):
        driver = self.driver
        driver.get(parse_config(self, 'Credentials', 'TEST_URL'))
        login = LoginPage(driver)
        login.enter_username(parse_config(self, 'Credentials', 'USERNAME'))
        login.enter_password(parse_config(self, 'Credentials', 'PASSWORD'))
        login.click_login_button()
        homepage = HomePage(driver)
        try:
            homepage.click_logout_button()
        except NoSuchElementException:
            print("Login Failed")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports"))
