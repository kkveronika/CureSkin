from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Header(Page):
    RETURNS_AND_ORDERS = (By.ID, 'nav-orders')
    DEPT_SELECTION = (By. CSS_SELECTOR, '.nav-search-dropdown')
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    NEW_ARRIVALS = (By.CSS_SELECTOR, '.nav-a.nav-hasArrow')
    WOMEN_DEALS = (By.CSS_SELECTOR, ".mm-merch-panel[href*='fashion-womens']")

    def returns_and_orders(self):
        self.click (*self.RETURNS_AND_ORDERS)

    def select_department_baby(self):
        department_dd = self.find_element(*self.DEPT_SELECTION)
        select = Select (department_dd)
        select.select_by_value("search-alias=baby-products")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)


    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def hover_over_options(self):
        new_arrival_options = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival_options)
        actions.perform()

    def verify_women_deals_shown(self):
        self.wait_for_element_appear(*self.WOMEN_DEALS)