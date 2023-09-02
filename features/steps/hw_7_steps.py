from behave import given, when, then
from selenium.webdriver.common.by import By



CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "[class='a-row sc-your-amazon-cart-is-empty']")


@when('Click Cart Icon')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@then('Verify Amazon Cart is Empty Text')
def verify_empty_cart_result(context):
    expected_text = 'Your Amazon Cart is empty'
    context.app.cart_is_empty_page.verify_empty_cart_result(expected_text)


    # actual_result = context.driver.find_element(*self.cart_is_empty_text).text
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    # print('Test Passed')