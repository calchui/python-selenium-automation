from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RTN_ORDERS_BTN = (By.ID, '#nav-orders')



#           SEARCH BAR FOR AMAZON
    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)



#           RETURN AND ORDERS FOR AMAZON
    def returns_orders_page(self):
        self.click(*self.RTN_ORDERS_BTN)

