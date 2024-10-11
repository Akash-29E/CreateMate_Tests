from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
from datetime import datetime
from POM.Pages.Yopmail import Yopmail
from POM.Pages.RegisterPage import RegisterPage
from POM.Pages.RegisterDetails import RegisterDetails


class ConfirmMailTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_confirm(self):
        driver = self.driver
        yopmail = Yopmail(driver)
        registerdetails = RegisterDetails(driver)

        driver.get("https://yopmail.com/en/wm")
        original_window = driver.current_window_handle
        yopmail.open_mailbox()
        yopmail.click_confirmmail()
        time.sleep(2)
        driver.switch_to.window(original_window)
        time.sleep(2)
        driver.get("https://staging.pdf-createmate.de/register")
        registerdetails.enter_email()
        registerdetails.click_verifyemail()
        time.sleep(2)
        registerdetails.fill_form()
        registerdetails.click_register()
        time.sleep(9)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete!")


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/SeleniumP/Test/Reports", verbosity=2))





