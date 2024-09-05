from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

action = ActionChains(driver)
# action.context_click()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()