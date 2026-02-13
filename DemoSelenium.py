import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#if the chrome version is too old need to use below code
# service_obj = Service("chromepath")
# driver= webdriver.Chrome(service=service_obj)


#driver is object of the chrome class
driver = webdriver.Chrome()
driver.get("http://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

















time.sleep(2)