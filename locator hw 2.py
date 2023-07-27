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

#********************* 3: CREATE TEST CASE FOR SIGN IN PAGE WHEN CLICKING ORDER ***************

# Click orders
driver.find_element(By. XPATH, ('//span[text()= "& Orders"]')).click()

# Verify if page is corrected

sign_in_result = 'Sign in'
actual_result = driver.find_element(By. XPATH, ("//h1[@class= 'a-spacing-small']")).text

assert sign_in_result == actual_result, f'Expected {sign_in_result} did not match actual {actual_result}'
print(f'{sign_in_result}: test case passed')


email_result = 'Email or mobile phone number'
actual_result = driver.find_element(By. XPATH, ("//label[@for='ap_email' and @class='a-form-label']")).text

assert email_result == actual_result, f'Expected {email_result} did not match actual {actual_result}'
print(f'{email_result}: test case passed')

create_acc_result = 'Create your Amazon account'
actual_result = driver.find_element(By. XPATH, ("//a[@ID= 'createAccountSubmit']")).text

assert create_acc_result == actual_result, f'Expected {create_acc_result} did not match actual {actual_result}'
print(f'{create_acc_result}: test case passed')


# #********************* 2: PRACTICE W/LOCATORS ************************************************
#
# # Amazon logo:
# driver.find_element(By. XPATH, ("//i[@class= 'a-icon a-icon-logo']"))
#
# # Email field
# driver.find_element(By. ID, ("//*[@ID= 'ap_email']"))
#
# # Continue button
# driver.find_element(By. ID, ("//input[@ID= 'continue']")
#
# # Conditions of use link
# driver.find_element(By. XPATH, ("//a[text()='Conditions of Use']"))
#
# # Privacy Notice link
# driver.find_element(By. XPATH, ("//a[text()='Privacy Notice']"))
#
# # Need help link
# driver.find_element(By. XPATH, ("//span[@class= 'a-expander-prompt']"))
#
# # Forgot your password link
# driver.find_element(By. XPATH, ("//a[@ID= 'auth-fpp-link-bottom']"))
#
# # Other issues with Sign-In link
# driver.find_element(By.ID, ("//a[@ID= 'ap-other-signin-issues-link']"))
#
# # Create your Amazon account button
# driver.find_element(By. ID, ("//a[@ID='createAccountSubmit']"))

