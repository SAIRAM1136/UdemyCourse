import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firstName='Sai'
lastName='Ram'
Email= "abc@gmail.com"
CurrentAddress = "Hyderabad"
PerAddress = CurrentAddress

driver = webdriver.Chrome()
driver.get("https://demoqa.com")
driver.implicitly_wait(5)

wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/elements']"))).click()

# #TextBox Code
driver.find_element(By.XPATH, "//span[text()='Text Box']").click()
driver.find_element(By.ID, "userName").send_keys(firstName)
driver.find_element(By.ID, "userEmail").send_keys(Email)
driver.find_element(By.ID, "currentAddress").send_keys(CurrentAddress)
driver.find_element(By.ID, "permanentAddress").send_keys(PerAddress)
# driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID, 'submit'))).click()

details = driver.find_element(By.CSS_SELECTOR, ".col-md-12").text
print(details)
assert "Hyderabad" in details,"Address Not found"

# #CHECKBOX
driver.find_element(By.XPATH, "//span[text()='Check Box']").click()
driver.find_element(By.CSS_SELECTOR, ".rc-tree-switcher_close").click()
driver.find_element(By.XPATH, "//span[@aria-label='Select Home']").click()
message = driver.find_element(By.XPATH, "//div[@id='result']").text
print(message)

# # #RADIOBUTTON
driver.find_element(By.XPATH, "//span[text()='Radio Button']").click()
driver.find_element(By.CSS_SELECTOR, "#yesRadio").click()

toggle_Message = driver.find_element(By.CSS_SELECTOR, ".mt-3").text
print(toggle_Message)

#WEB TABLES
driver.find_element(By.XPATH, "//span[text()='Web Tables']").click()
driver.find_element(By.ID, "addNewRecordButton").click()

driver.find_element(By.ID, "firstName").send_keys(firstName)
driver.find_element(By.ID, "lastName").send_keys(lastName)
driver.find_element(By.ID, "userEmail").send_keys(Email)
driver.find_element(By.ID, "age").send_keys("25")
driver.find_element(By.ID, "salary").send_keys("50000")
driver.find_element(By.ID, "department").send_keys("QA")
driver.find_element(By.ID, "submit").click()

driver.find_element(By.ID, "searchBox").click()
driver.find_element(By.ID, "searchBox").send_keys("Kierra")

driver.find_element(By.ID, "edit-record-3").click()
driver.find_element(By.ID, "salary").clear()
driver.find_element(By.ID, "salary").send_keys("80000")
driver.find_element(By.ID, "submit").click()
driver.find_element(By.ID, "searchBox").clear()

# #BUTTONS
driver.find_element(By.XPATH, "//span[text()='Buttons']").click()
actions = ActionChains(driver)
actions.double_click(driver.find_element(By.XPATH, "//button[text()='Double Click Me']")).perform()
actions.context_click(driver.find_element(By.ID, "rightClickBtn")).perform()
# actions.click(driver.find_element(By.ID, "eNJvs")).perform()

#LINKS
driver.find_element(By.XPATH, "//span[text()='Links']").click()
driver.find_element(By.LINK_TEXT, "Bad Request").click()
Link_message = driver.find_element(By.XPATH, "//p[@id='linkResponse']").text
print(Link_message)


time.sleep(5)
