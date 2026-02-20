import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("prefs", {"credentials_enable_service": False,
                                          "profile.password_manager_enabled": False,
                                          "profile.password_manager_leak_detection": False})

options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
a = driver.title
print(a)
assert "Swag Labs" in a

items = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
print(len(items))

for item in items:
    item.click()
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()
driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()
driver.find_element(By.XPATH, "//a[text()='Logout']").click()

assert "saucedemo" in driver.current_url

















time.sleep(5)


