import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome() #launching chrome browser
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/") #we application
driver.maximize_window() #window maximizing
driver.implicitly_wait(2) #wait for web elements to load

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber") #giving the item partial name in the search box
time.sleep(2) #waiting to appear all the items

items = driver.find_elements(By.XPATH, "//div[@class='products']/div") #it captures all lists found by giving keyword
count = len(items)  #length
print(count) #it prints the count
assert count > 0 #validation
for item in items:
    item.find_element(By.XPATH, "div/button").click() #it clicks the add to cart button for all the items listed by given keyword

driver.find_element(By.XPATH, "//img[@alt='Cart']").click() #it will click on cart symbol
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click() #proceed to checkout
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy") #coupon code

wait=WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoBtn"))).click() #applying the coupon code

driver.find_element(By.XPATH, "//button[text()='Place Order']").click() #it clicks on the place order button

country_list = Select(driver.find_element(By.XPATH, "//select[@style='width: 200px;']")) #it will choose the country from the dropdown
country_list.select_by_value("India")

driver.find_element(By.XPATH, "//input[@type='checkbox']").click() #agreeing terms and conditions
driver.find_element(By.XPATH, "//button[text()='Proceed']").click() #it will click on proceed to place order


