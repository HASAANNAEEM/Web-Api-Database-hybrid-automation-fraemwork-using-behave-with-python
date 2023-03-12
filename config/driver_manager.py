from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import logging
from Utilities.log import Logger
from config.constants import Constants
driver = None
from selenium.webdriver.chrome.options import Options

class WebDriverManager:
    """Web Driver for the GUI based Testing """
    def __init__(self):
        self.data = []
        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    def initialize_driver(self, context, browser):
        self.log.logger.info("Initialize the driver")
        global driver
        options = Options()
        platform = context.config.userdata['platform']
        if "aws" in platform:
            options.add_argument("--headless")
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("window-size=1920,1080")
        if browser == 'chrome':
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
            # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif "IE" in browser:
            driver = webdriver.Ie(executable_path=IEDriverManager().install(), ie_options=options)
        elif "edge" in browser:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())

        else:
            raise ValueError('Browser ' + browser + ' is not supported')
        return driver


