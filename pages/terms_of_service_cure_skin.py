from selenium.webdriver.common.by import By
from pages.base_page import Page


class TermsOfServise(Page):
    TERMS_SERVICE_TEXT = (By.CSS_SELECTOR, '.shopify-policy__title')

    def terms_of_service_opened(self):
        expected_result = 'Terms of service'
        actual_result = self.wait_for_element_appear(*self.TERMS_SERVICE_TEXT).text
        assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
