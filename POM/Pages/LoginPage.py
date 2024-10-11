from selenium import webdriver
from selenium.webdriver.common.by import By

def fetch_cred():
    f = open('D:/SeleniumP/Test/POM/registered_emails.txt', 'r')
    cred = f.readlines()[-1]
    email = cred.split('::')[0]
    passw = cred.split('::')[1]
    f.close()
    return email, passw

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_id = "email"
        self.password_textbox_id = "password"
        self.login_button_xpath = "//button[contains(text(),'Login')]"

    def fill_login(self):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(fetch_cred()[0])
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(fetch_cred()[1])

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
