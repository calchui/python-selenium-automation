from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\edc_p\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open website
driver.get('https://www.amazon.com/')


#*********************** Problem 1 *********************************

# Amazon Logo:
driver.find_element(By. CSS_SELECTOR, "[class='a-icon a-icon-logo']")

#Create Account:
driver.find_element((By. CSS_SELECTOR, "[class='a-spacing-small']")

# Your name: fill in box:
driver.find_element(By. CSS_SELECTOR, "[ID='ap_customer_name']")

# Email fill in box:
driver.find_element(By. CSS_SELECTOR, "[ID='ap_email']")

# Password fill in box:
driver.find_element(By. CSS_SELECTOR, "[ID='ap_password']")

#Passwords must be at least 6 characters:
driver.find_element(By. CSS_SELECTOR, "[class='a-alert-content']")

# Re-enter password fill in box:
driver.find_element(By. CSS_SELECTOR, "[ID='ap_password_check']")

# Continue button:
driver.find_element(By. CSS_SELECTOR, "[ID='continue']")

# Conditions of Use:
driver.find_element(By. CSS_SELECTOR, "[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")

# Privacy Notice:
driver.find_element(By. CSS_SELECTOR, "[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice']")

# Sign in button:
driver.find_element(By. CSS_SELECTOR, "[class='a-link-emphasis']")