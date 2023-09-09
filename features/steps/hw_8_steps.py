from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


@given('Open Amazon T&C page')
def open_amazon_t_c_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.app.amazon_privacy_notice.store_original_window()


@when('Click on Amazon Privacy Notice link')
def click_on_link(context):
    context.app.amazon_privacy_notice.click_on_link()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.app.amazon_privacy_notice.switch_to_new_window()


@then('Verify Amazon Privacy Notice page is opened')
def verify_page_opened(context):
    context.app.amazon_privacy_notice.verify_page_opened()


@then('User can close new window and switch back to original')
def return_to_original_window(context):
    context.app.amazon_privacy_notice.switch_to_window(context.original_window)