from selenium.webdriver.common.by import By
from pages.base_page import Page

class AmazonPrivacyNotice(Page):

    LINK = (By.CSS_SELECTOR, "[href='https://www.amazon.com/privacy']")

    def store_original_window(self):
        return self.get_current_window()


    def click_on_link(self):
        self.click(*self.LINK)


    def verify_page_opened(self):
        self.verify_partial_url('https://www.amazon.com/gp/help/customer/display')


