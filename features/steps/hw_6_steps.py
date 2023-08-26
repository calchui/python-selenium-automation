from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page



RTN_ORDERS_BTN = (By.ID, '#nav-orders')
SIGN_IN = (By.CSS_SELECTOR, "h1[class*='a-spacing-small']")


@when('Click Amazon Orders link')
def returns_orders_page(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify Sign In page is opened')
def verify_sign_in_result(context):
    expected_result = 'Sign in'
        #actual_result = self.find_element(*self.SIGN_IN).text
        #assert expected_result == actual_result, \
        #    f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.signin_page.verify_sign_in_result(expected_result)

