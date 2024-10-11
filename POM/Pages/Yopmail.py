from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def mailid():
    f = open('D:/SeleniumP/Test/POM/sign_ups.txt', 'r')
    a = f.readlines()[-1]
    b = a.split('+')[0]
    c = a.split('@')[-1]
    d = b + '@' + c
    f.close()
    return d


def addmregmail_list():
    f = open('D:/SeleniumP/Test/POM/sign_ups.txt', 'r')
    a = f.readlines()[-1]
    f.close()
    b = open('D:/SeleniumP/Test/POM/verified_emails.txt', 'a+')
    b.write('\n' + a)
    b.close()


class Yopmail:

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_xpath = "//input[@id='login']"
        self.confirmmail_button_xpath = "/html/body/main/div/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a"

    def open_mailbox(self):
        x = mailid()
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(x)
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(Keys.RETURN)

    def click_confirmmail(self):
        self.driver.switch_to.frame("ifmail")
        self.driver.find_element(By.XPATH, self.confirmmail_button_xpath).click()
        addmregmail_list()

