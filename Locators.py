#["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]
# syntax for Xpath
#     //tag[@attribute = 'value']

# syntax for CSS selectors:
#     tag[attribute= 'value']


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# service_obj=Service("chrome path.exe")
# driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@minlength='2']").send_keys("Practice page")
driver.find_element(By.NAME, "email").send_keys("abc123@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.XPATH, "//input[@ID='exampleCheck1']").click() #dynamic xpath
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.NAME,"bday").send_keys("16/07/1995")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success!" in message


time.sleep(5)

