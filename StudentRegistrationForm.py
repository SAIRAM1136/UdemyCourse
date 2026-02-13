import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# service_obj=Service("chrome path.exe")
# driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()

name = "Sai Ram"
email = "sairam123@gmail.com"
mobile = "8976543201"
DOB = "16/09/1997"
Subjects= "English"
address = "Hyderabad"

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='gender']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile Number']").send_keys(mobile)
driver.find_element(By.XPATH, "//input[@id='dob']").send_keys(DOB)
driver.find_element(By.NAME, "subjects").send_keys(Subjects)
driver.find_element(By.XPATH, "//div[2]/input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//textarea[@id='picture']").send_keys(address)
state=Select(driver.find_element(By.ID, "state"))
state.select_by_value("NCR")
city=Select(driver.find_element(By.ID, "city"))
city.select_by_value("Agra")

time.sleep(2)

driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(2)

#//div/ul/li[1]/span[@class='plus']