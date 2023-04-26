from selenium.webdriver.common.by import By
from pages.base_page import Page


class TermsOfServise(Page):
    TERMS_SERVICE_TEXT = (By.CSS_SELECTOR, '.shopify-policy__title')

    def terms_of_service_opened(self):
        self.wait_for_element_appear(*self.TERMS_SERVICE_TEXT)
