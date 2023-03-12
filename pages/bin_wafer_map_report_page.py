import time
import logging
import allure
from allure_commons.types import AttachmentType
from allure_commons._allure import attach

import canvas__getdata_script
from Utilities import yaml_reader
from config.web import WebConfigurations
from config.driver_manager import WebDriverManager
from Helpers.generics import GenericMethods
from Utilities.log import Logger
from Elements.login import LoginElements
from Elements.reports_elements import ReportsElements

reports_elements = ReportsElements()
manage_driver = WebDriverManager()
web_conf = WebConfigurations()
helpers = GenericMethods()
login_elements = LoginElements()


class BinWaferMapPage:
    log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    def verifying_data(self, context):
        try:
            self.log.logger.info("Verification of Bin Wafer Map report")
            reports_elements.soft_bin = reports_elements.soft_bin
            reports_elements.is_selected = reports_elements.is_selected
            reports_elements.x_axis = reports_elements.x_axis
            reports_elements.y_axis = reports_elements.y_axis
            attach(str(reports_elements.soft_bin), name="Verification of Bin Wafer Map report - Done"
                   , attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Verification of Bin Wafer Map report - Done")
        except Exception as e:
            attach(str(e.soft_bin), name="Error in verification of Bin Wafer Map report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e
        except AssertionError as e:
            attach(str(e.soft_bin), name="Assertion error in verification of Bin Wafer Map report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

    def verify_canvas(self, context):
        try:
            canvas = helpers.wait_for_visibility_of_element(context, reports_elements.canvas_exists, "xpath")
            assert canvas.is_displayed() is True
            self.log.logger.info("Verifying the canvas")
            allure.attach(context.driver.get_screenshot_as_png(), name="Dashboard", attachment_type=AttachmentType.PNG)
        except Exception as e:
            attach(str(e.soft_bin), name="Error in verifying the canvas"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e
        except AssertionError as e:
            attach(str(e.soft_bin), name="Assertion error in verifying the canvas"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

    def verify_data(self, context):
        try:
            canvas = canvas__getdata_script.ScrapData()
            canvas.scrap_method()
        except Exception as e:
            attach(str(e.soft_bin), name="Error in verifying the canvas data"
               , attachment_type=AttachmentType.TEXT)
            assert False, e
        except AssertionError as e:
            attach(str(e.soft_bin), name="Assertion error in verifying the canvas data"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

    def generate_report(self, context):
        try:
            self.log.logger.info("Generating the report")
            # waiting for the content saving then generate the report
            helpers.click_element(context, reports_elements.generate_report_btn)
            self.log.logger.info("Generating the report - Done")
        except Exception as e:
            attach(str(e), name="Error in generating the report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e
        except AssertionError as e:
            attach(str(e), name="Assertion error in generating the report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

    def verify_selection_criteria(self, context):
        try:
            self.log.logger.info("Selection criteria window appeared - Successful")
            allure.attach(context.driver.get_screenshot_as_png(), name="Selection criteria", attachment_type=AttachmentType.PNG)
        except Exception as e:
            attach(str(e.soft_bin), name="Error in selection criteria window appeared"
               , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as e:
            attach(str(e.soft_bin), name="Assertion error in selection criteria window appeared"
               , attachment_type=AttachmentType.TEXT)
            assert False, e

