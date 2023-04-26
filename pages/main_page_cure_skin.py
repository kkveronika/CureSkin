from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainCureSkinPage(Page):
    TERMS_SERVICE = (By.CSS_SELECTOR, 'a[href="/policies/terms-of-service"]')

    def click_on_terms_page(self):
        self.click(*self.TERMS_SERVICE)
