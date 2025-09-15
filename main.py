from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

MAIL="student@test.com"
PASSWORD="password123"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

ans=driver.find_element(By.XPATH,value='//*[@id="login-button"]')
ans.click()

email_imput=driver.find_element(By.XPATH,value='//*[@id="email-input"]')
email_imput.send_keys(MAIL)

password_input=driver.find_element(By.XPATH,value='//*[@id="password-input"]')
password_input.send_keys(PASSWORD)

login_1=driver.find_element(By.XPATH,value='//*[@id="submit-button"]')
login_1.click()

time.sleep(2)

# Switch to alert if it appears
try:
    alert = driver.switch_to.alert
    print("Alert says:", alert.text)   # optional
    alert.accept()                     # press OK instead of dismiss
except:
    print("No alert appeared")

time.sleep(2)

book_class=driver.find_element(By.XPATH,value='//*[@id="book-button-hiit-2025-09-04-1900"]')
book_class.click()
