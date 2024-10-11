import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.ca/")

driver.find_element(By.NAME, "q").send_keys("Jujutsu Kaisen")
time.sleep(0.2)
print(driver.title)
driver.find_element(By.NAME, "btnK").click()
time.sleep(0.2)
print(driver.title)

print("Test Complete")
driver.close()
driver.quit()