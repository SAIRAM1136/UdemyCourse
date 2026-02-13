import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# service_obj=Service("chrome path.exe")
# driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)

radio=driver.find_elements(By.XPATH, "//input[@name='radioButton']")
print(len(radio))

for i in radio:
    if i.get_attribute("value") == "radio2":
        i.click()

driver.find_element(By.ID, "autocomplete").send_keys("Am")

wait = WebDriverWait(driver, 10)
countries = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='ui-menu-item']/div")))
for country in countries:
    print(country.text)

    if country.text.strip() == 'Cameroon':
        country.click()
        break

drop_list = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
drop_list.select_by_value("option3")
time.sleep(2)

check_box=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(check_box))

for i in check_box:
    if i.get_attribute("value") == "option2":
        i.click()

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Sai")
# driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
# driver.switch_to.alert.accept()

driver.find_element(By.ID, "confirmbtn").click()
time.sleep(5)
driver.switch_to.alert.dismiss()

