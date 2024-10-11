from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
from datetime import datetime
from POM.Pages.HomePage import HomePage
from POM.Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_confirm(self):
        driver = self.driver
        homepage = HomePage(driver)
        loginpage = LoginPage(driver)

        driver.get("https://staging.pdf-createmate.de")
        homepage.click_login()
        time.sleep(1)
        loginpage.fill_login()
        loginpage.click_login()
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete!")


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/SeleniumP/Test/Reports", verbosity=2))





