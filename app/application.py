from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.cart_is_empty_page import CartIsEmpty
from pages.bestsellers_page import BestsellersPage
from pages.add_to_cart_page import AddToCart
from pages.not_found_page import NotFoundPage
from pages.blog import Blog
from pages.amazon_privacy_notice import AmazonPrivacyNotice

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.cart_is_empty_page = CartIsEmpty(driver)
        self.add_to_cart_page = AddToCart(driver)
        self.bestsellers_page = BestsellersPage(driver)
        self.not_found_page = NotFoundPage(driver)
        self.blog = Blog(driver)
        self.amazon_privacy_notice = AmazonPrivacyNotice(driver)


