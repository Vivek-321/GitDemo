from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Vivek"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
Alert = driver.switch_to.alert
alertText = Alert.text
assert name in alertText
print(alertText)
Alert.accept()
# Alert.dismiss()



time.sleep(3)
