from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.tryforfree_button_xpath = "//body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]"
        self.getademo_button_xpath = "//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[2]"
        self.login_button_linktxt = "Login"

    def click_tryforfree(self):
        self.driver.find_element(By.XPATH, self.tryforfree_button_xpath).click()

    def click_login(self):
        self.driver.find_element(By.LINK_TEXT, self.login_button_linktxt).click()
