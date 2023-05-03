from selenium import webdriver
from app.application import Application
from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# import allure
# from allure_commons.types import AttachmentType
# from selenium.webdriver.support.events import EventFiringWebDriver
# from selenium.webdriver.chrome.service import Service
from support.logger import logger, MyListener
from selenium.webdriver.support.ui import WebDriverWait

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
    #options = FirefoxOptions()
    #options.headless = True
    #options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #context.driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
    ##################################

    bs_user = 'veronikakarpova_xPJfUg'
    bs_key = 'fPkNqWvMVpZaoUqg7VzN'

    # desired_cap = {
    #     'browserName': 'Chrome',
    #     'bstack:options': {
    #         'os': 'OS X',
    #         'osVersion': 'Big Sur'
    #        # 'sessionName': test_name
    #     }
    # }
    desired_cap = {
        'bstack:options': {
            "os": "OS X",
            "osVersion": "Ventura",
            "browserVersion": "latest",
            "local": "false",
            "seleniumVersion": "3.10.0",
        },
        "browserName": "Firefox",
    }

    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
       #  print('\nStep failed: ', step)
       logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()


# for browerstack ###
#     # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings


################ from documentation #################
#     userName: veronikakarpova_xPJfUg
#     accessKey: fPkNqWvMVpZaoUqg7VzN
#     framework: behave
#     platforms:
#     - os: Windows
#     osVersion: 11
#     browserName: Chrome
#     browserVersion: 103.0
#     - os: Windows
#     osVersion: 10
#     browserName: Firefox
#     browserVersion: 102.0
#     - os: OS X
#     osVersion: Big Sur
#     browserName: Safari
#     browserVersion: 14.1
#     browserstackLocal: true
#     url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#     context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)



