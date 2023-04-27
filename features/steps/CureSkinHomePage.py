from selenium.webdriver.common.by import By
from behave import given, when, then


TERMS_SERVICE = (By.CSS_SELECTOR,'a[href="/policies/terms-of-service"]')
EMAIL_TEXT = (By.CSS_SELECTOR, '#ContactFooter-email')

@given('Open main page')
def open_main_page(context):
    context.driver.get('https://shop.cureskin.com/')


@when('From page footer, click "Terms of Service"')
def terms_of_service(context):
   context.app.main_cure_skin_page.click_on_terms_page()


@then('Verify Terms page opened')
def terms_of_service_opened(context):
    context.app.terms_of_service_cure_skin.terms_of_service_opened()


# #@when('From page footer, in email field enter {VK}')
# def enter_wrong_email(context):
#     pass
#
#
# @then('Verify error message displays')
# def error_message_displays(context):
#     pass