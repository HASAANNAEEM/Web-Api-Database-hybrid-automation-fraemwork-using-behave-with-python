# import log
import logging
import time

from selenium.webdriver.common.by import By

from Utilities.log import Logger
from Helpers.generics import GenericMethods
from Elements.create_policy import CreatePolicyElements

web_elements = CreatePolicyElements()
generic_helper = GenericMethods()


class ReportsHelper:
    log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    def selecting_facility_name_from_selection_criteria(self, context, facility_name):
        self.log.logger.info("Selecting data from " + facility_name)
        generic_helper.verify_element_displayed(context, web_elements.SearchFacilityNameInputField)
        generic_helper.verify_element_enable(context, web_elements.SearchFacilityNameInputField)
        generic_helper.input_element(context, web_elements.SearchFacilityNameInputField, facility_name)
        generic_helper.verify_element_displayed(context, web_elements.FacilityScroll)
        generic_helper.verify_element_enable(context, web_elements.FacilityScroll)
        generic_helper.scroll_to_element(context, web_elements.FacilityScroll)
        check_box = "//td[text()='" + facility_name + "']//..//span[@class='dx-checkbox-icon']"
        by_locator = (By.XPATH, check_box)
        generic_helper.verify_element_displayed(context, by_locator)
        generic_helper.verify_element_enable(context, by_locator)
        generic_helper.scroll_to_element(context, by_locator)
        generic_helper.click_element(context, by_locator)
        self.log.logger.info("Selection for the " + facility_name + " : Done")

    def selecting_lot_name_from_selection_criteria(self, context, lot_name):
        self.log.logger.info("Selecting data from " + lot_name)
        generic_helper.verify_element_displayed(context, web_elements.SearchLotNameInputField)
        generic_helper.verify_element_enable(context, web_elements.SearchLotNameInputField)
        generic_helper.input_element(context, web_elements.SearchLotNameInputField, lot_name)
        context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        check_box = "(//td[text()='" + lot_name + "']//..//span[@class='dx-checkbox-icon'])[3] | (//td[text()='" + lot_name + "']//..//span[@class='dx-checkbox-icon'])[1]"
        by_locator = (By.XPATH, check_box)
        generic_helper.verify_element_enable(context, by_locator)
        generic_helper.click_element(context, by_locator)

        self.log.logger.info("Selection for the " + lot_name + " : Done")

    def selecting_wafer_name_from_selection_criteria(self, context, wafer_name):
        self.log.logger.info("Selecting data from " + wafer_name)
        generic_helper.click_element(context, web_elements.WaferTable)
        check_box = "(//td[text()='" + wafer_name + "']//..//span[@class='dx-checkbox-icon'])[3]"
        element = context.driver.find_element_by_xpath(check_box)
        element.click()
        self.log.logger.info("Selection for the " + wafer_name + " : Done")

    def selecting_test_parameters_from_selection_criteria(self, context, test_parameter):
        self.log.logger.info("Selecting data from " + test_parameter)
        generic_helper.verify_element_displayed(context, web_elements.SearchTestParameterNameInputField)
        generic_helper.verify_element_enable(context, web_elements.SearchTestParameterNameInputField)
        generic_helper.input_element(context, web_elements.SearchTestParameterNameInputField, test_parameter)
        # generic_helper.click_element(context, web_elements.TestParameterTable)
        check_box = "(//td[contains(text(),'" + test_parameter + "')]//..//span[@class='dx-checkbox-icon'])[3] | (//td[contains(text(),'" + test_parameter + "')]//..//span[@class='dx-checkbox-icon'])[1]"
        by_locator = (By.XPATH, check_box)
        # generic_helper.verify_element_displayed(context, by_locator)
        # generic_helper.verify_element_enable(context, by_locator)
        generic_helper.click_element(context, by_locator)
        self.log.logger.info("Selection for the " + test_parameter + " : Done")

    def selecting_facility_from_selection_criteria(self, context, facility_name):

        self.log.logger.info("Selecting data from " + facility_name)
        generic_helper.verify_element_displayed(context, web_elements.SearchFacilityNameInputField)
        generic_helper.verify_element_enable(context, web_elements.SearchFacilityNameInputField)
        generic_helper.input_element(context, web_elements.SearchFacilityNameInputField, facility_name)
        check_box = "//td[text()='" + facility_name + "']//..//span[@class='dx-checkbox-icon']"
        by_locator = (By.XPATH, check_box)
        generic_helper.verify_element_displayed(context, by_locator)
        generic_helper.verify_element_enable(context, by_locator)
        generic_helper.click_element(context, by_locator)
        self.log.logger.info("Selection for the " + facility_name + " : Done")

    def selecting_work_center_from_selection_criteria(self, context, work_centers):
        for work_center in work_centers:
            self.log.logger.info("Verify data from " + work_center)
            generic_helper.verify_element_displayed(context, web_elements.SearchWorkCenterInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchWorkCenterInputField)
            generic_helper.input_element(context, web_elements.SearchWorkCenterInputField, work_center)
            check_box = "//td[text()='" + work_center + "']//..//span[@class='dx-checkbox-icon']"
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Verified data from " + work_center)

    def selecting_device_from_selection_criteria(self, context, devices):
        for device in devices:
            self.log.logger.info("Verify data from " + device)
            generic_helper.verify_element_displayed(context, web_elements.SearchDeviceInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchDeviceInputField)
            generic_helper.input_element(context, web_elements.SearchDeviceInputField, device)
            check_box = "//td[text()='" + device + "']//..//span[@class='dx-checkbox-icon']"
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Verified data from " + device)

    def selecting_test_program_from_selection_criteria(self, context, test_programs):
        for test_program in test_programs:
            self.log.logger.info("Verify data from " + test_program)
            generic_helper.verify_element_displayed(context, web_elements.SearchTestProgramInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchTestProgramInputField)
            generic_helper.input_element(context, web_elements.SearchTestProgramInputField, test_program)
            check_box = "//td[text()='" + test_program + "']//..//span[@class='dx-checkbox-icon']"
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Verified data from " + test_program)

    def selecting_test_program_revision_from_selection_criteria(self, context, test_program_revisions):
        for test_program_revision in test_program_revisions:
            self.log.logger.info("Verify data from " + test_program_revision)
            generic_helper.verify_element_displayed(context, web_elements.SearchTestProgramRevisionInputField)
            generic_helper.input_element(context, web_elements.SearchTestProgramRevisionInputField,
                                         test_program_revision)
            check_box = "//td[text()='" + test_program_revision + "']//..//span[@class='dx-checkbox-icon']"
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Verified data from " + test_program_revision)

    def verify_automatically_selected_table_vale(self, context, value):
        self.log.logger.info("verify " + value + " is selected")
        locator = "//*[text()='" + value + "']//..//..//..//..//tr[@class='highlight dx-row dx-data-row dx-column-lines']"
        by_locator = (By.XPATH, locator)
        generic_helper.verify_element_displayed(context, by_locator)
        self.log.logger.info("verified " + value + " is selected")
