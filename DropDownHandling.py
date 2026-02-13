import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# service_obj=Service("chrome path.exe")
# driver = webdriver.Chrome(service=service_obj)

# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//input[@minlength='2']").send_keys("Practice page")
# driver.find_element(By.NAME, "email").send_keys("abc123@gmail.com")
# driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
# driver.find_element(By.XPATH, "//input[@ID='exampleCheck1']").click() #dynamic xpath
#
# #static dropdown selection :
#     #statis dropdown means having the some certain options in the dropdown
#
# dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")
# time.sleep(1)
# dropdown.select_by_index(0)

#Dynamic dropdown selection :
    #Dynamic dropdown means having n number of options in the dropdown

driver.get("https://rahulshettyacademy.com/dropdownsPractise/") #launched the web page
driver.maximize_window() # Maximized the window

driver.find_element(By.ID, "autosuggest").send_keys("ind") #given first 3 letters of the country name to get suggestions in the dropdown
time.sleep(1) #waiting for 2 seconds to get all countries listed

countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a") #given the common xpath for all the countries which are sent as suggestions in the dropdown
print(len(countries)) #printed total length

for country in countries: # to click on the specific country we used for loop and added if condition
    if country.text == "India": # if the text in the dropdown is India
        country.click()  #that need to click
        break #after matching the expected need to break the loop

# print(driver.find_element(By.ID, "autosuggest").text)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"




time.sleep(2)
