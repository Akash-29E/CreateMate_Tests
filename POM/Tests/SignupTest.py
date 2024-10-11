from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
from datetime import datetime
from POM.Pages.HomePage import HomePage
from POM.Pages.RegisterPage import RegisterPage


class SignupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_signup(self):
        driver = self.driver
        mys = datetime.now().strftime("%d%m%M%S")
        mail_id = "paula_mail+" + mys + "@yopmail.com"
        homepage = HomePage(driver)
        registerpage = RegisterPage(driver)

        driver.get("https://staging.pdf-createmate.de/")
        homepage.click_tryforfree()
        registerpage.enter_email(mail_id)
        registerpage.click_verifyemail()
        # self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]").click()
        # self.driver.find_element(By.ID, "email").send_keys(mail_id)
        # self.driver.find_element(By.XPATH, "//button[contains(text(),'Verify email')]").click()
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete!")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/SeleniumP/Test/Reports", verbosity=2))





