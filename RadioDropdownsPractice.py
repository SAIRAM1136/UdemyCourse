import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# service_obj=Service("chrome path.exe")
# driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#driver.implicitly_wait(5)

#Radio Button handling
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radio_buttons))

for radio in radio_buttons:
    if radio.get_attribute("value") == "radio2":
        radio.click()

#Dropdown handling by typing on search
driver.find_element(By.ID, "autocomplete").send_keys("ind")
time.sleep(2)

drop_down = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")
print(len(drop_down))

for drop in drop_down:
    if drop.text == "India":
        drop.click()

time.sleep(2)


#drop down handling by selecting the option inside it

drop_list = Select(driver.find_element(By.XPATH, "dropdown-class-example"))
drop_list.select_by_value("option2")
#drop_list.select_by_visible_text("Option2")

