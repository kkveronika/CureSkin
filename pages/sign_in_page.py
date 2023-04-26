from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    RETURNS_AND_ORDERS = (By.ID, 'nav-orders')
    SIGN_IN_TEXT = (By.CSS_SELECTOR, 'h1.a-spacing-small')

    def click_returns_and_orders(self):
        self.click(*self.RETURNS_AND_ORDERS)
    def verify_sing_in_page_is_opened(self, expected_text):
        self.verify_text(expected_text, *self.SIGN_IN_TEXT)