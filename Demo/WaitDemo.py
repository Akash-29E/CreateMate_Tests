import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://www.google.com")
driver.find_element(By.NAME, "q").send_keys("Satoru Gojo")
driver.find_element(By.NAME, "btnK").click()

print("Test Complete")
driver.close()
driver.quit()