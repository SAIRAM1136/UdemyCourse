import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/") #automation webpage for practice purpose
driver.maximize_window() #to maximize window
driver.implicitly_wait(4)

driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()

WebDriverWait(driver, 10).until((EC.number_of_windows_to_be(2)))

window=driver.window_handles
driver.switch_to.window(window[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
print(message)

var = message.split("at")[1].strip().split(" ")[0]
print(var)
driver.close()

driver.switch_to.window(window[0])

driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.XPATH, "//input[@id='terms']").click()
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)




