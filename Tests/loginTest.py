import time
import unittest
from selenium import webdriver
from pages.homePage import HomePage
from pages.loginPage import LoginPage
import configparser
import HtmlTestRunner


def parse_config(self, header, parameter):
    config = configparser.ConfigParser()
    config.read("C:/Users/npava/PycharmProjects/PythonPOM/Conf/config.ini")
    return config.get(header, parameter)


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:\\Users\\npava\\PycharmProjects\\PythonPOM\\Drivers\\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://demo.silverstripe.org/Security/login?BackURL=%2Fadmin%2Fpages%2F")
        login = LoginPage(driver)
        login.enter_username(parse_config(self, 'Credentials', 'USERNAME'))
        login.enter_password(parse_config(self, 'Credentials', 'PASSWORD'))
        login.click_login_button()
        homepage = HomePage(driver)
        homepage.click_logout_button()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/npava/PycharmProjects/PythonPOM/Reports"))
