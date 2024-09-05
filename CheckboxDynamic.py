from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# For Checkbox
options = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for option in options:
    if option.get_attribute("value") == "option3":
        option.click()
        assert option.is_selected()
        break


# For radio button
Radiobuttons = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
# alternet Xpath = '//div/fieldset/label/input' --> 6 elements found
# alternet CSS = '.radioButoon' --> 6 elements found
print(len(Radiobuttons))
for button in Radiobuttons:
    if button.get_attribute("value") == "radio2":
        button.click()
        assert button.is_selected()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(3)