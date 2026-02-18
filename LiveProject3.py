from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//a[text()='Shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    name = product.find_element(By.XPATH, "div/h4/a").text #to get text for all products
    if name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()  # if conditions matches it will click the product

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]").click()
driver.find_element(By.ID, 'country').send_keys('ind')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'India')]"))).click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in success_message

driver.get_screenshot_as_file("Screenshot.png")