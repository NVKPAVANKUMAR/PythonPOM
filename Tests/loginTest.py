import json
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from pages.Moodle_Sandbox_homePage import MoodleHomePage
from pages.Moolde_Sandbox_loginPage import MoodleLoginPage
import configparser
import configuration.config as config_data
from xml.etree import ElementTree as ET


def parse_config(header, parameter):
    conf = configparser.ConfigParser()
    conf.read('configuration/config.ini')
    return conf.get(header, parameter)


def read_json(data_source):
    with open(data_source) as datafile:
        data = json.load(datafile)
        return data


def parse_xml_config(key):
    tree = ET.parse('configuration/config.xml')
    root = tree.getroot()
    return root.findall(".//{}".format(key))[0].text


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(executable_path='Drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    #  parsing data via JSON
    def test01_login_valid(self):
        driver = self.driver
        data = read_json("configuration/config.json")
        driver.get(data['CREDENTIALS']['URL'])
        login_page = LoginPage(driver)
        login_page.enter_username(data['CREDENTIALS']['USERNAME'][1])
        login_page.enter_password(data['CREDENTIALS']['PASSWORD'][1])
        login_page.click_login_button()
        homepage = HomePage(driver)
        try:
            homepage.click_logout_button()
        except NoSuchElementException:
            print("Login Failed")

    #  parsing data via .ini
    def test02_login_invalid(self):
        driver = self.driver
        driver.get(parse_config('Credentials', 'TEST_URL'))
        login_page = LoginPage(driver)
        login_page.enter_username(parse_config('Credentials', 'USERNAME'))
        login_page.enter_password(parse_config('Credentials', 'PASSWORD'))
        login_page.click_login_button()
        homepage = HomePage(driver)
        try:
            homepage.click_logout_button()
        except NoSuchElementException:
            print("Login Failed")

    #  parsing data via built-in data structure
    def test03_login_moodle_sandbox(self):
        driver = self.driver
        driver.get(config_data.CREDENTIALS['url'])
        login_page = MoodleLoginPage(driver)
        login_page.enter_username(config_data.CREDENTIALS['username'])
        login_page.enter_password(config_data.CREDENTIALS['password'])
        login_page.click_login_button()
        homepage = MoodleHomePage(driver)
        try:
            homepage.click_logout_button()
        except NoSuchElementException:
            print("Login Failed")

    #  parsing data via xml
    def test04_login_moodle_sandbox_invalid(self):
        driver = self.driver
        driver.get(parse_xml_config('url'))
        login_page = MoodleLoginPage(driver)
        login_page.enter_username(parse_xml_config('username'))
        login_page.enter_password(parse_xml_config('password'))
        login_page.click_login_button()
        homepage = MoodleHomePage(driver)
        try:
            homepage.click_logout_button()
        except NoSuchElementException:
            print("Login Failed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
