from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    BABY_DEPARTMENT = (By. CSS_SELECTOR, '.nav-a[aria-label="Baby"]')

    def verify_selected_department(self):
        self.wait_for_element_appear(*self.BABY_DEPARTMENT)
