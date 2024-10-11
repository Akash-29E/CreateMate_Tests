import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CO = Options()
# CO.add_argument("--headless=new")
driver = webdriver.Chrome(options=CO)

driver.set_page_load_timeout(10)

driver.get("https://staging.pdf-createmate.de/")

driver.find_element(By.LINK_TEXT, "Login").click()
print(driver.title)
time.sleep(2)
# driver.find_element(By.NAME, "btnK").click()
# time.sleep(0.2)
# print(driver.title)
# time.sleep(2)

driver.close()
driver.quit()

print("Test Complete")