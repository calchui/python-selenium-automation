from behave import given, when, then
from selenium.webdriver.common.by import By



CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "[class='a-row sc-your-amazon-cart-is-empty']")

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
CLICK_FIRST_IMAGE = (By.CSS_SELECTOR, 'img[src*="media-amazon.com/images/I/71id0DdTtNL"]')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
NO_THANKS = (By.ID, 'attachSiNoCoverage')
CLICK_ON_CART = (By.CSS_SELECTOR, '[href="/gp/cart/view.html?ref_=nav_cart"]')
CART = (By.ID, 'nav-cart-count')
SUBTOTAL_TEXT = (By.ID, 'sc-subtotal-label-activecart')

@when('Click Cart Icon')
def search_on_amazon(context):
    # context.driver.find_element(By.ID, 'nav-cart-count').click()
    context.app.add_to_cart_page.click_cart_icon(CART)



@then('Verify Amazon Cart is Empty Text')
def verify_empty_cart_result(context):
    expected_text = 'Your Amazon Cart is empty'
    context.app.cart_is_empty_page.verify_empty_cart_result(expected_text)


    # actual_result = context.driver.find_element(*self.cart_is_empty_text).text
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    # print('Test Passed')


@when('Click on Search Bar')
def click_on_search_bar(context):
    context.app.add_to_cart_page.click_on_search_bar(SEARCH_FIELD)
    # context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('shelves')
    # context.driver.find_element(By.ID, 'nav-search-submit-button').click()


# @then('Click Search')
# def type_in_shelves(context):
#     context.app.add_to_cart_page.type_in_shelves(SEARCH_BTN)


@then('Click on shelves')
def click_on_shelves(context):
    context.app.add_to_cart_page.click_on_shelves(CLICK_FIRST_IMAGE)
    # context.driver.find_element(By.CSS_SELECTOR, 'https://m.media-amazon.com/images/I/71iMQhPtT7L._AC_UL400_.jpg').click()
    # context.driver.find_element(By.CSS_SELECTOR, 'img[src*="media-amazon.com/images/I/71id0DdTtNL"]').click()


@then('Add to Cart')
def add_to_cart(context):
    # context.driver.find_element(By.ID, 'add-to-cart-button').click()
    context.app.add_to_cart_page.add_to_cart(ADD_TO_CART)

@then('Click No Thanks')
def no_thanks(context):
    # context.driver.find_element(By.ID, 'attachSiNoCoverage').click()
    context.app.add_to_cart_page.no_thanks(NO_THANKS)

@then('Click on Cart')
def click_on_cart(context):
    # context.driver.find_element(By.CSS_SELECTOR, '[href="/gp/cart/view.html?ref_=nav_cart"]').click()
    context.app.add_to_cart_page.click_on_cart(CLICK_ON_CART)


@then('Verify Shelves in Cart')
def verify_subtotal(context):
    expected_text = 'Subtotal (1 item)'
    context.app.add_to_cart_page.verify_search_result(expected_text)


    # actual_result = context.driver.find_element(By.ID, 'sc-subtotal-label-activecart').text
    # assert expected_result in actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    # print('Test Passed')



