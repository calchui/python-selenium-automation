from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, 'h1.a-spacing-small')

    def verify_sign_in_result(self, expected_text):
        #expected_text = "Sign in"
        actual_text = self.find_element(*self.SIGN_IN).text
        print(actual_text)
        print(expected_text)
        assert actual_text == expected_text, f'Error, expected {expected_text} did not match actual {actual_text}'
