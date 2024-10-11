from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_id = "email"
        self.verifyemail_button_xpath = "//button[contains(text(),'Verify email')]"

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).clear()
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)
        f = open('D:/SeleniumP/Test/POM/sign_ups.txt', 'a+')
        f.write('\n' + email)
        f.close()

    def click_verifyemail(self):
        self.driver.find_element(By.XPATH, self.verifyemail_button_xpath).click()