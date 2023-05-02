from selenium import webdriver
from app.application import Application
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def browser_init(context):
    """
    :param context: Behave context
    """
    # ######### CHROME #################
    # options = ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # context.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    # ##################################

    ########## FIREFOX################
    options = FirefoxOptions()
    #options.headless = True
    options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    context.driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
    ##################################


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

