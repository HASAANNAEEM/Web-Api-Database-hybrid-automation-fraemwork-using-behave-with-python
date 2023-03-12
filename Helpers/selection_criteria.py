import time
import logging
from selenium.webdriver.common.by import By
from Utilities.log import Logger
from Helpers.generics import GenericMethods
from Elements.create_policy import CreatePolicyElements

web_elements = CreatePolicyElements()
generic_helper = GenericMethods()


class SelectionCriteriaHelper:
    log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    def selecting_lot_name_from_selection_criteria(self, context, table_name, lot_names):
        for lot_name in lot_names:
            self.log.logger.info("Selecting data from " + lot_name)
            generic_helper.verify_element_displayed(context, web_elements.SearchLotNameInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchLotNameInputField)
            generic_helper.input_element(context, web_elements.SearchLotNameInputField, lot_name)
            # generic_helper.click_element(context, web_elements.LotTable)
            context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, lot_name)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.click_element(context, by_locator)

            self.log.logger.info("Selection for the " + lot_name + " : Done")

    def selecting_wafer_name_from_selection_criteria(self, context, table_name,  wafer_names):
        for wafer_name in wafer_names:
            self.log.logger.info("Selecting data from " + wafer_name)
            generic_helper.verify_element_displayed(context, web_elements.SearchWaferNameInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchWaferNameInputField)
            generic_helper.input_element(context, web_elements.SearchWaferNameInputField, wafer_name)
            check_box = CreatePolicyElements.wafer_checkbox_input_field % (table_name, wafer_name)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Selection for the " + wafer_name + " : Done")

    def selecting_test_parameters_from_selection_criteria(self, context, table_name, test_parameters):

        for test_parameter in test_parameters:
            self.log.logger.info("Selecting data from " + test_parameter)
            generic_helper.verify_element_displayed(context, web_elements.SearchTestParameterNameInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchTestParameterNameInputField)
            generic_helper.input_element(context, web_elements.SearchTestParameterNameInputField, test_parameter)
            try:
                generic_helper.click_element(context, web_elements.TestParameterTable)
            except Exception as e:
                self.log.logger.warning("Clicking test parameter table")
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, test_parameter)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.verify_element_enable(context, by_locator)
            if "One" in test_parameters:
                generic_helper.click_element(context, by_locator)
                break
            self.log.logger.info("Selection for the " + test_parameter + " : Done")

    def selecting_specific_test_parameters_from_selection_criteria(self, context, table_name,  test_parameter):
        self.log.logger.info("Selecting data from " + test_parameter)
        generic_helper.verify_element_displayed(context, web_elements.SearchTestParameterNameInputField)
        generic_helper.verify_element_enable(context, web_elements.SearchTestParameterNameInputField)
        generic_helper.input_element(context, web_elements.SearchTestParameterNameInputField, test_parameter)
        check_box = CreatePolicyElements.checkbox_input_field % (table_name, test_parameter)
        by_locator = (By.XPATH, check_box)
        generic_helper.verify_element_displayed(context, by_locator)
        generic_helper.verify_element_enable(context, by_locator)
        generic_helper.click_element(context, by_locator)
        self.log.logger.info("Selection for the " + test_parameter + " : Done")

    def verify_lot_name_from_selection_criteria(self, context, table_name,  lot_names):
        for lot_name in lot_names:
            self.log.logger.info("Verify data from " + lot_name)
            generic_helper.verify_element_displayed(context, web_elements.SearchLotNameInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchLotNameInputField)
            generic_helper.input_element(context, web_elements.SearchLotNameInputField, lot_name)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, lot_name)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            self.log.logger.info("Verified data from " + lot_name)

    def verify_wafer_name_from_selection_criteria(self, context, table_name, wafer_names):
        for wafer_name in wafer_names:
            self.log.logger.info("Verify data from " + wafer_name)
            generic_helper.verify_element_displayed(context, web_elements.SearchWaferNameInputField)
            generic_helper.input_element(context, web_elements.SearchWaferNameInputField, wafer_name)
            check_box = CreatePolicyElements.wafer_checkbox_input_field % (table_name, wafer_name)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            self.log.logger.info("Verified for the " + wafer_name+ " : Done")

    def verify_test_parameters_from_selection_criteria(self, context, table_name,  test_parameters):
        for test_parameter in test_parameters:
            self.log.logger.info("Verify data from " + test_parameter)
            generic_helper.verify_element_displayed(context, web_elements.SearchTestParameterNameInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchTestParameterNameInputField)
            generic_helper.input_element(context, web_elements.SearchTestParameterNameInputField, test_parameter)
            try:
                generic_helper.click_element(context, web_elements.TestParameterTable)
            except Exception as e:
                self.log.logger.warn("Clicking test parameter table")
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, test_parameter)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            self.log.logger.info("Verified for the " + test_parameter + " : Done")

    def verify_work_center_from_selection_criteria(self, context, table_name, work_centers):
        for work_center in work_centers:
            self.log.logger.info("Verify data from " + work_center)
            generic_helper.verify_element_displayed(context, web_elements.SearchWorkCenterInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchWorkCenterInputField)
            generic_helper.input_element(context, web_elements.SearchWorkCenterInputField, work_center)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, work_center)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            self.log.logger.info("Verified data from " + work_center)

    def verify_device_from_selection_criteria(self, context, table_name, devices):
        for device in devices:
            self.log.logger.info("Verify data from " + device)
            generic_helper.verify_element_displayed(context, web_elements.SearchDeviceInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchDeviceInputField)
            generic_helper.input_element(context, web_elements.SearchDeviceInputField, device)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, device)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            self.log.logger.info("Verified data from " + device)

    def verify_test_program_from_selection_criteria(self, context, table_name, test_programs):
        for test_program in test_programs:
            self.log.logger.info("Verify data from " + test_program)
            generic_helper.verify_element_displayed(context, web_elements.SearchTestProgramInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchTestProgramInputField)
            generic_helper.input_element(context, web_elements.SearchTestProgramInputField, test_program)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, test_program)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            self.log.logger.info("Verified data from " + test_program)

    def verify_test_program_revision_from_selection_criteria(self, context, table_name, test_program_revisions):
        for test_program_revision in test_program_revisions:
            self.log.logger.info("Verify data from " + test_program_revision)
            generic_helper.verify_element_displayed(context, web_elements.SearchTestProgramRevisionInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchTestProgramRevisionInputField)
            generic_helper.input_element(context, web_elements.SearchTestProgramRevisionInputField,
                                         test_program_revision)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, test_program_revision)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            self.log.logger.info("Verified data from " + test_program_revision)

    def selecting_facility_from_selection_criteria(self, context, table_name,  facility_name):
        self.log.logger.info("Selecting data from " + facility_name)
        generic_helper.verify_element_displayed(context, web_elements.SearchFacilityNameInputField)
        generic_helper.verify_element_enable(context, web_elements.SearchFacilityNameInputField)
        generic_helper.input_element(context, web_elements.SearchFacilityNameInputField, facility_name)
        check_box = CreatePolicyElements.checkbox_input_field % (table_name, facility_name)
        by_locator = (By.XPATH, check_box)
        generic_helper.verify_element_displayed(context, by_locator)
        generic_helper.verify_element_enable(context, by_locator)
        generic_helper.click_element(context, by_locator)
        self.log.logger.info("Selection for the " + facility_name + " : Done")

    def selecting_work_center_from_selection_criteria(self, context, table_name,  work_centers):
        for work_center in work_centers:
            self.log.logger.info("Verify data from " + work_center)
            generic_helper.verify_element_displayed(context, web_elements.SearchWorkCenterInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchWorkCenterInputField)
            generic_helper.input_element(context, web_elements.SearchWorkCenterInputField, work_center)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, work_center)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Verified data from " + work_center)

    def selecting_device_from_selection_criteria(self, context, table_name, devices):
        for device in devices:
            self.log.logger.info("Verify data from " + device)
            generic_helper.verify_element_displayed(context, web_elements.SearchDeviceInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchDeviceInputField)
            generic_helper.input_element(context, web_elements.SearchDeviceInputField, device)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, device)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Verified data from " + device)

    def selecting_test_program_from_selection_criteria(self, context, table_name, test_programs):
        for test_program in test_programs:
            self.log.logger.info("Verify data from " + test_program)
            generic_helper.verify_element_displayed(context, web_elements.SearchTestProgramInputField)
            generic_helper.verify_element_enable(context, web_elements.SearchTestProgramInputField)
            generic_helper.input_element(context, web_elements.SearchTestProgramInputField, test_program)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, test_program)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Verified data from " + test_program)

    def selecting_test_program_revision_from_selection_criteria(self, context, table_name, test_program_revisions):
        for test_program_revision in test_program_revisions:
            self.log.logger.info("Verify data from " + test_program_revision)
            generic_helper.verify_element_displayed(context, web_elements.SearchTestProgramRevisionInputField)
            generic_helper.input_element(context, web_elements.SearchTestProgramRevisionInputField,
                                         test_program_revision)
            check_box = CreatePolicyElements.checkbox_input_field % (table_name, test_program_revision)
            by_locator = (By.XPATH, check_box)
            generic_helper.verify_element_enable(context, by_locator)
            generic_helper.verify_element_displayed(context, by_locator)
            generic_helper.click_element(context, by_locator)
            self.log.logger.info("Verified data from " + test_program_revision)

    def verify_facility_name_from_selection_criteria(self, context, table_name, facility_name):
        self.log.logger.info("Verify data from " + facility_name)
        generic_helper.verify_element_displayed(context, web_elements.SearchFacilityNameInputField)
        generic_helper.verify_element_enable(context, web_elements.SearchFacilityNameInputField)
        generic_helper.input_element(context, web_elements.SearchFacilityNameInputField, facility_name)
        check_box_xpath = CreatePolicyElements.checkbox_input_field % (table_name, facility_name)
        by_locator = (By.XPATH, check_box_xpath)
        generic_helper.verify_element_enable(context, by_locator)
        generic_helper.verify_element_displayed(context, by_locator)
        self.log.logger.info("Verified data from " + facility_name)

