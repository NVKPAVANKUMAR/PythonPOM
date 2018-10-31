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
        cls.driver = webdriver.Chrome(executable_path='Drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test01_login_valid(self):
        driver = self.driver
        data = read_json(self, "configuration/config.json")
        driver.get(data['CREDENTIALS']['URL'])
        login_page = LoginPage(driver)
        login_page.enter_username(data['CREDENTIALS']['USERNAME'][1])
        login_page.enter_password(data['CREDENTIALS']['PASSWORD'][1])
        login_page.click_login_button()
        homepage = HomePage(driver)
        homepage.click_logout_button()


    def test02_login_invalid(self):
        driver = self.driver
        driver.get(parse_config(self, 'Credentials', 'TEST_URL'))
        login_page = LoginPage(driver)
        login_page.enter_username(parse_config(self, 'Credentials', 'USERNAME'))
        login_page.enter_password(parse_config(self, 'Credentials', 'PASSWORD'))
        login_page.click_login_button()
        homepage = HomePage(driver)
        try:
            homepage.click_logout_button()
        except NoSuchElementException:
            print("Login Failed")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        loader.loadTestsFromTestCase(LoginTest)))
    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports', verbosity=2)
    runner.run(suite)
