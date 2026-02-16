import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#to get screenshot of the page
# driver.get_screenshot_as_file("screenshot.png")

#to scroll the page
# driver.execute_script("window.scrollBy(0,500);")
#driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

driver = webdriver.Chrome()
# service_obj=Service("chrome path.exe")
# driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/") #automation webpage for practice purpose
driver.maximize_window() #to maximize window
driver.implicitly_wait(10) #i added implicit wait here to get all web elements with 10s

radio=driver.find_elements(By.XPATH, "//input[@name='radioButton']") #it captures all radio buttons
print(len(radio)) #it prints the length

for i in radio: #this for loop to iterate all buttons
    if i.get_attribute("value") == "radio2": #if radio2 is the value
        i.click() #it will select

driver.find_element(By.ID, "autocomplete").send_keys("Am") # i am just giving partial name in the search box to get country list

wait = WebDriverWait(driver, 10) #Explicit wait i added
countries = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='ui-menu-item']/div"))) #it will show all the countries
for country in countries:
    print(country.text) #i added for loop to iterate all countries and to print text

    if country.text.strip() == 'Cameroon': #the given country name is matched in the above loop
        country.click() #it will go and select that break
        break #after getting the expected country the loop will break and come out

drop_list = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")) #i used select class to get all the elements in the dropdown
drop_list.select_by_value("option3") #if the value is option3 it will select
time.sleep(2)  #it will wait for 2 seconds

check_box=driver.find_elements(By.XPATH, "//input[@type='checkbox']") # this is get all the options for the checklists
print(len(check_box)) #it will print length of the check list

for i in check_box: #by using the forloop if the value is option2 then it will click
    if i.get_attribute("value") == "option2":
        i.click()


#Switch to window /tab
driver.find_element(By.ID,"openwindow").click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)
driver.switch_to.window(windows[0])

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Sai") #this is to write something in the search box
# driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
# driver.switch_to.alert.accept() #it will accept the alert

driver.find_element(By.ID, "confirmbtn").click() #this is get the pop up
time.sleep(5)
driver.switch_to.alert.dismiss() # it will dismiss the popup

#MouseOver
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
time.sleep(4)

#frames
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT, "Courses").click()
print(driver.title)
driver.find_element(By.XPATH, "//h2[contains(text(),'All-Access Membership')]").click()
print(driver.title)
time.sleep(5)

