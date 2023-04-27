from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.amazon_cart import AmazonCart
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.main_page_cure_skin import MainCureSkinPage
from pages.terms_of_service_cure_skin import TermsOfServise

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.amazon_cart = AmazonCart(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.main_cure_skin_page = MainCureSkinPage(self.driver)
        self.terms_of_service_cure_skin = TermsOfServise(self.driver)


        # self.search_results_page = SearchResultsPage(self.driver).