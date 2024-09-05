from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title)
