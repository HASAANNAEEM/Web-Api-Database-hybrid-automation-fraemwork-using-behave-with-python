import time
import logging
from selenium.webdriver.common.by import By
from config.web import WebConfigurations
from config.driver_manager import WebDriverManager
from Helpers.generics import GenericMethods
from Utilities.log import Logger
from Elements.login import LoginElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
manage_driver = WebDriverManager()
web_conf = WebConfigurations()
helpers = GenericMethods()
login_elements = LoginElements()
from config.constants import Constants
from Utilities import yaml_reader
log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))


class LoginClass:
    file = "./Features/TestData/login.yml"

    def __init__(self):
        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))
        self.data = []

    # ********* Actions *********
    def open_website(self, context):
        try:
            self.log.logger.info("Login screen is displayed")
            browser = context.config.userdata['browser']
            context.driver = manage_driver.initialize_driver(context, browser)
            context.driver.maximize_window()
            context.driver.implicitly_wait(web_conf.implicit_wait)
            env = context.config.userdata['env']
            url = "https://"+env+".yieldwerx.com/"
            context.driver.get(url)
        except Exception as e:
            self.log.logger.error("Error login screen is displayed")
            attach(str(e), name="Error login screen is displayed"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error login screen is displayed")
            attach(str(ex), name="Assertion error login screen is displayed"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_credentials(self, context, credential):
        try:
            self.log.logger.info("Entering username and password for " + credential)
            platform = context.config.userdata['platform']
            # Reading data from yml file
            data = yaml_reader.data_reader_for_login(context, platform)
            user_name_input_field = (By.XPATH, login_elements.username_field)
            helpers.input_element(context, user_name_input_field, data["userName"])
            self.log.logger.info(data["password"])
            password_input_field = (By.XPATH, login_elements.password_field)
            helpers.input_element(context, password_input_field, data["password"])
        except Exception as e:
            self.log.logger.error("Error in entering username and password for " + credential)
            attach(str(e), name="Error in entering username and password for " + credential
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in entering username and password for " + credential)
            attach(str(ex), name="Assertion error in entering username and password for " + credential
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def hit_login(self, context):
        try:
            self.log.logger.info("Click the Login button")
            by_locator = (By.XPATH, login_elements.login_button)
            helpers.click_element(context, by_locator)
        except Exception as e:
            self.log.logger.error("Error in click the Login button")
            attach(str(e), name="Error in click the Login button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in click the Login button")
            attach(str(ex), name="Assertion error in click the Login button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_dashboard(self, context):
        try:
            self.log.logger.info("Verify the dashboard")
            dashboard_text = helpers.wait_for_visibility_of_element(context, login_elements.verification_text, "xpath")
            assert dashboard_text.is_displayed() is True
            self.log.logger.info("Login Successful")
        # allure.attach(context.driver.get_screenshot_as_png(), name="Dashboard", attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.log.logger.error("Error in verify the dashboard")
            attach(str(e), name="Error in verify the dashboard"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verify the dashboard")
            attach(str(ex), name="Assertion error in verify the dashboard"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def quit_browser(self, context):
        try:
            self.log.logger.info("Quit the browser")
            context.driver.quit()

        except Exception as e:
            self.log.logger.error("Error quit the browser")
            attach(str(e), name="Error quit the browser"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error quit the browser")
            attach(str(ex), name="Assertion error quit the browser"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex
