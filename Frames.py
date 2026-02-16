import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe") #automation webpage for practice purpose
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//button[contains(@class,'tox-notification__dismiss')]").click()

driver.switch_to.frame("mce_0_ifr")
time.sleep(2)
driver.find_element(By.ID, "tinymce").click()
driver.find_element(By.XPATH, "//p[contains(text(), 'Your content goes here.')]").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am automating frames")

time.sleep(2)


