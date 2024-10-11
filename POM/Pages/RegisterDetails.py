from selenium import webdriver
from selenium.webdriver.common.by import By


def fetchconfirmedmail():
    f = open('D:/SeleniumP/Test/POM/verified_emails.txt', 'r')
    mail = f.readlines()[-1]
    fname = mail.split('_')[0]
    lname = (mail.split('_'))[1].split('+')[0]
    passw = "paula$" + (mail.split('+'))[1].split('@')[0]
    org = "paula" + (mail.split('+'))[1].split('@')[0] + " Corp"
    f.close()
    return mail, fname, lname, passw, org


def regmaillist_add(imail):
    f = open('D:/SeleniumP/Test/POM/registered_emails.txt', 'a+')
    f.write('\n' + imail)
    f.close()


class RegisterDetails:

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_id = "email"
        self.verifyemail_button_xpath = "//button[contains(text(),'Verify email')]"
        self.firstname_textbox_id = "first_name"
        self.lastname_textbox_id = "last_name"
        self.orgname_textbox_id = "organization_name"
        self.pass_textbox_id = "password"
        self.terms_checkbox_id = "terms"
        self.privacy_checkbox_id = "privacy"
        self.register_button_xpath = "//button[contains(text(),'Register')]"

    def enter_email(self):
        x = fetchconfirmedmail()[0]
        print(x)
        self.driver.find_element(By.ID, self.email_textbox_id).clear()
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(x)

    def click_verifyemail(self):
        self.driver.find_element(By.XPATH, self.verifyemail_button_xpath).click()

    def fill_form(self):
        self.driver.find_element(By.ID, self.firstname_textbox_id).send_keys(fetchconfirmedmail()[1])
        self.driver.find_element(By.ID, self.lastname_textbox_id).send_keys(fetchconfirmedmail()[2])
        self.driver.find_element(By.ID, self.orgname_textbox_id).send_keys(fetchconfirmedmail()[4])
        self.driver.find_element(By.ID, self.pass_textbox_id).send_keys(fetchconfirmedmail()[3])
        self.driver.find_element(By.ID, self.terms_checkbox_id).click()
        self.driver.find_element(By.ID, self.privacy_checkbox_id).click()

    def click_register(self):
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()
        regmaillist_add(fetchconfirmedmail()[0]+"::"+fetchconfirmedmail()[3])
