from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

# #***************************** Problem 1 *************************************

#              I have not used any sleep functions in any of my code.

#
# #***************************** Problem 2 *************************************

@given('Open Amazon {website_id} page')
def open_amazon_product(context, website_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{website_id}/')


@then('Verify colors in webpage')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage', 'Dark Indigo', 'Dark Wash']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)
        print(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
