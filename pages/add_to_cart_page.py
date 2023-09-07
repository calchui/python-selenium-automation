from selenium.webdriver.common.by import By
from pages.base_page import Page


class AddToCart(Page):

    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    CLICK_FIRST_IMAGE = (By.CSS_SELECTOR, 'img[src*="media-amazon.com/images/I/71id0DdTtNL"]')
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    NO_THANKS = (By.ID, 'attachSiNoCoverage')
    CLICK_ON_CART = (By.CSS_SELECTOR, '[href="/gp/cart/view.html?ref_=nav_cart"]')
    CART = (By.ID, 'nav-cart-count')
    SUBTOTAL_TEXT = (By.ID, 'sc-subtotal-label-activecart')


    def click_cart_icon(self, CART):
        self.click(*self.CART)


    def click_on_search_bar(self, text):
        self.input_text('shelves', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    # def type_in_shelves(self, type_in_shelves):

    def click_on_shelves(self, CLICK_FIRST_IMAGE):
        # context.driver.find_element(By.CSS_SELECTOR, 'https://m.media-amazon.com/images/I/71iMQhPtT7L._AC_UL400_.jpg').click()
        self.click(*self.CLICK_FIRST_IMAGE)


    def add_to_cart(self, ADD_TO_CART):
        self.click(*self.ADD_TO_CART)


    def no_thanks(self, NO_THANKS):
        self.click(*self.NO_THANKS)


    def click_on_cart(self, CLICK_ON_CART):
        self.click(*self.CLICK_ON_CART)


    def verify_subtotal(self, expected_text):
        actual_result = self.find_element(*self.SUBTOTAL_TEXT).text
        print(actual_text)
        print(expected_text)
        assert expected_text == actual_text, f'Error, expected {expected_text} did not match actual {actual_text}'
