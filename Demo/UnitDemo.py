import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        self.driver.get("https://www.google.ca/")
        x = self.driver.title
        self.driver.find_element(By.NAME, "q").send_keys("Itachi")
        time.sleep(0.2)
        print(x)
        self.assertEqual(x, "Google")
        self.driver.find_element(By.NAME, "btnK").click()
        time.sleep(0.2)
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Itachi - Google Search")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/SeleniumP/Test/Reports", verbosity=2))