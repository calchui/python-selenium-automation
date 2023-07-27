from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\edc_p\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.find_element(By. ID, ('nav-search-submit-button'))

driver.find_element(By.ID, ('nav-cart-count'))

#By XPATH
#Tag and attributes
driver.find_element(By. XPATH, ("//input[@aria-label='Search Amazon']"))
driver.find_element(By. XPATH, ("//a[@class='nav-a  ' and @data-csa-c-id='nav_cs_2']"))

#Multiple Attributes
driver.find_element(By. XPATH, ("//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")

#By XPATH, Text
driver.find_element(By. XPATH, ("//a[text()='Best Sellers']")
driver.find_element(By. XPATH, ("//a[text()='Best Sellers' and @class='nav-a  ']"))

#Any tag = *
driver.find_element(By. XPATH, ("//*[text()='Best Sellers' and @class='nav-a  ']"))

#Contains:
        #Original form
driver.find_element(By.XPATH, ("//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
        #TO
driver.find_element(By.XPATH, ("//a[contains( @href, 'nav_cs_bestsellers' )]")
        # also can do it for Text
driver.find_element(By. XPATH, ("//a[contains(text(), 'Best Seller') and @class ='nav-a   ']"))
