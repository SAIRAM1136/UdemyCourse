import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# service_obj=Service("chrome path.exe")
# driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.ID, "userPassword").send_keys("1234")
driver.find_element(By.ID, "confirmPassword").send_keys("1234")
driver.find_element(By.XPATH, "//button[contains(text(),'Save New Password')]").click()


#To find the xpath from the parent to child transverse
# driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("<PASSWORD>")
# driver.find_element(By.XPATH, "//button(text='Save New password')").click()






time.sleep(5)