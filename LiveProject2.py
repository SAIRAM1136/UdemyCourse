import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)

items = driver.find_elements(By.XPATH, "//div[@class='products']/div") #it captures all lists found by giving keyword
count = len(items)
print(count)
assert count > 0
for item in items:
    item.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

wait=WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoBtn"))).click()

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

country_list = Select(driver.find_element(By.XPATH, "//select[@style='width: 200px;']"))
country_list.select_by_value("India")

driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()


time.sleep(8)