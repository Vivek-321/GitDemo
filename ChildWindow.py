from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(5)


driver.find_element(By.LINK_TEXT, "Click Here").click()
WindowOpened = driver.window_handles

driver.switch_to.window(WindowOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

driver.switch_to.window(WindowOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text