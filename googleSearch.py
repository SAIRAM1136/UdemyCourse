import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('headless')
chrome_options.add_argument('--ignore cookies')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").click()
