from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RTN_ORDERS_BTN = (By.ID, '#nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, 'a-row sc-your-amazon-cart-is-empty')
    LANG_SELECTION = (By.CSS_SELECTOR, '.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="#switch-lang=es_US"]')

#    #*****  HW 9 Problem 2 *****
    NEW_ARRIVALS = (By.CSS_SELECTOR, '[href="/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6"]')
    DEALS = (By.CSS_SELECTOR, "a[href*='/s?i=fashion-women']")

#    #*****  HW 9 Problem 1 *****
    DEPT_SELECTION = (By.ID, 'searchDropdownBox')
    SUB_HEADER_DEPT = (By.CSS_SELECTOR, "#nav-subnav[data-category='baby-products']")


#           SEARCH BAR FOR AMAZON
    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


#           RETURN AND ORDERS FOR AMAZON
    def click_orders(self):
        self.click(*self.RTN_ORDERS_BTN)


    def click_empty_cart(self):
        self.click(*self.CART_IS_EMPTY_TEXT)


    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(*self.SIGNIN_BTN)


    def hover_lang(self):
        actions = ActionChains(self.driver)
        lang = self.find_element(*self.LANG_SELECTION)
        actions.move_to_element(lang)
        actions.perform()

    def hover_new_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(new_arrivals)
        actions.perform()


# *****  HW 9 Problem 1 *****
    def select_dept(self):
        dept_selection = self.find_element(*self.DEPT_SELECTION)
        select = Select(dept_selection)
        select.select_by_value('search-alias=baby-products')


    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(*self.SIGNIN_BTN)


    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)


    def verify_new_arrivals(self):
        self.wait_for_element_appear(*self.DEALS)


#*****  HW 9 Problem 1 *****
    def verify_dept_selected(self):
        self.wait_for_element_appear(*self.SUB_HEADER_DEPT)



