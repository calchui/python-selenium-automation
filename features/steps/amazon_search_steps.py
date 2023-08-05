from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
#
#
# @when('Search for table')
# def search_on_amazon(context):
#     context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
#     context.driver.find_element(By.ID, 'nav-search-submit-button').click()
#
#
# @then('Verify search result is correct')
# def verify_search_result(context):
#     expected_result = '"table"'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')


# @when('Click Orders')
# def search_on_amazon(context):
#     context.driver.find_element(By.ID, 'nav-orders').click()
#
#
# @then('Verify sign in page opened')
# def verify_search_result(context):
#     expected_result = 'Sign in'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[class='a-spacing-small']").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')


# @when('Click Cart Icon')
# def search_on_amazon(context):
#     context.driver.find_element(By.ID, 'nav-cart-count').click()
#
#
# @then('Verify Amazon Cart is Empty')
# def verify_search_result(context):
#     expected_result = 'Your Amazon Cart is empty'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[class='a-row sc-your-amazon-cart-is-empty']").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')


@when('Search for shelves')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('shelves')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Click on shelves')
def click_on_shelves(context):
    # context.driver.find_element(By.CSS_SELECTOR, 'https://m.media-amazon.com/images/I/71iMQhPtT7L._AC_UL400_.jpg').click()
    context.driver.find_element(By.CSS_SELECTOR, 'img[src*="media-amazon.com/images/I/71iMQhPtT7L"]').click()

@then('Click No Thanks')
def add_to_cart(context):
    context.driver.find_element(By.ID, 'attachSiNoCoverage').click()


@then('Add to Cart')
def add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Click on Cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'attach-sidesheet-view-cart-button').click()


@then('Verify Shelves in Cart')
def verify_search_result(context):
    expected_result = 'Subtotal (1 item)'
    actual_result = context.driver.find_element(By.ID, 'sc-subtotal-label-buybox').text
    assert expected_result in actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    print('Test Passed')