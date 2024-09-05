from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
# Max it will wait till 2 second

# Comparing Actual list with Expected list
Expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
Actual_list =[]
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)

print(count)
assert count > 0
for result in results:
    Actual_list.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert Expected_list == Actual_list

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()= 'PROCEED TO CHECKOUT']").click()
# time.sleep(2)

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum=0
for price in prices:
    sum = sum + int(price.text)
print(sum)
amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert amount == sum


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Explicit wait --> if any particular item is taking more time than explicit wait time , then
# for that particular item only wait time will be applied
wait = WebDriverWait(driver,10) 
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
# print(discountedAmount)
assert amount > discountedAmount
# time.sleep(5)