from selenium.webdriver.common.by import By
from pages.base_page import Page

class AmazonCart(Page):
    CART_ICON = (By.ID, 'nav-cart-count')
    CART_EMPTY = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2")

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def verify_text_inside_shopping_cart(self, expected_text):
        self.verify_text(expected_text, *self.CART_EMPTY)
