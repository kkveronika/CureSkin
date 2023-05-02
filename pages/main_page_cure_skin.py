from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainCureSkinPage(Page):
    TERMS_SERVICE = (By.CSS_SELECTOR, 'a[href="/policies/terms-of-service"]')
    EMAIL_TEXT = (By.CSS_SELECTOR, '#ContactFooter-email')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.button.button--arrow.field__button.animate-arrow')
    def click_on_terms_page(self):
        self.click(*self.TERMS_SERVICE)


    def enter_email(self):
        self.input_text(text, *self.EMAIL_TEXT)


    def click_search_button(self):
        self.click(*self.SEARCH_BUTTON)


    def error_message_displays(self):
        self.wait_for_element_appear