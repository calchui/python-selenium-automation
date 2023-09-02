from selenium.webdriver.common.by import By
from pages.base_page import Page



class CartIsEmpty(Page):
    CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "[class='a-row sc-your-amazon-cart-is-empty']")

    def verify_empty_cart_result(self, expected_text):
        # expected_result = 'Your Amazon Cart is empty'
        actual_text = self.find_element(*self.CART_IS_EMPTY_TEXT).text
        print(actual_text)
        print(expected_text)
        assert actual_text == expected_text, f'Error, expected {expected_text} did not match actual {actual_text}'
