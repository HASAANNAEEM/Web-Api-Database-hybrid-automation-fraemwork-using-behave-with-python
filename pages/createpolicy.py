import os
import logging
import allure
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from Utilities import bucket_file_download
from selenium.webdriver.common import keys
from datetime import datetime, timedelta
from pages.database import DatabaseManagement
from selenium.webdriver.common.by import By
import time
from Utilities import yaml_reader
from config.web import WebConfigurations
from config.driver_manager import WebDriverManager
from Helpers.generics import GenericMethods
from Helpers.reports import ReportsHelper
from Helpers.selection_criteria import SelectionCriteriaHelper
from Utilities.log import Logger
from Elements.create_policy import CreatePolicyElements
from config.constants import Constants

database = DatabaseManagement()
manage_driver = WebDriverManager()
web_conf = WebConfigurations()
helpers = GenericMethods()
current_time = datetime.now()
web_elements = CreatePolicyElements()
report_helper = ReportsHelper()
selection_criteria_helper = SelectionCriteriaHelper()


class PoliciesPage:
    def __init__(self):
        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    facility_name = {}
    test_parameter_name_list = {}
    work_center_list = {}
    device_list = {}
    test_program_list = {}
    test_program_revision_list = {}
    lot_list = {}
    wafer_list = {}
    # Test data file path
    file = "./TestData/policy.yml"
    exact_time = None
    future = None
    # Locators
    create_policy = '//button[text()="Create Policy"]'
    policy_name = '//input[@name="name"]'
    policy_version = '//input[@name="version"]'
    policy_desc = '//textarea[@name="purpose"]'
    policy_owner_email_input_field = "//input[@name = 'owner']"
    add_stage = '//div[@class=" dropdown-full dropdown"]//button[text()="Add Stage"]'
    policy_polling = '//span[contains(text(),"Polling Interval")]/parent::span/parent::div/div/div/input'
    view = '//button[contains(text(),"View")]'
    source_format = '//button[text()="ATDF"]'
    source_of_file = '//button[contains(text(),"Policy Step")]'
    policy_step_drop_down = (By.XPATH, "(//span[text()='Source'])[last()]//..//button")
    container = '//span[text()="Source Container"]/parent::div//div//input'
    ftp_address = '//span[text()="Ftp Address"]/parent::div//div//input'
    ftp_username = '//span[text()="Ftp Username"]/parent::div//div//input'
    ftp_password = '//span[text()="Ftp Password"]/parent::div//div//input'
    folder_to_transfer_files_from = '//span[text()="Folder to transfer files from"]/parent::div//div//input'
    type = '//span[text()="Type"]/parent::span/parent::div/div/div/div/button'
    start_time = '(//span[text()="Starts At"]/parent::span/parent::div/div/div//input)[2]'
    save_btn = '//*[text()="Save"]'
    success_alert_message = (By.XPATH, '//div[contains(@class,"toast--success")]//div[@role="alert"]')
    filter = '(//td[@aria-colindex="6" and @aria-label="Filter cell"]/div//div[2]//div//div//input)[last()]'
    step_intake_queue = (By.XPATH, "//a[contains(text(),'Step Intake')]")
    step_intake_queue_policy_name_input_field = (By.XPATH, "//div[contains(text(),'Policy Name')]//..//..//following-sibling::tr//td[3]//input")
    step_intake_queue_status = (By.XPATH, "(//table[contains(@class,'select-checkboxes')])[last()]//td[contains(@aria-colindex,'4')]//span")
    sort_start_time = '//div[text()="Start Time"]'
    success_msg = '//tr[@aria-rowindex="1"]//td//span[text()="SUCCESS"]'
    target_file = '(//tr[@aria-rowindex="1"]//td[@aria-colindex="4" and contains(text(),"s3://yw-temp-convert-files")])'
    source_file_location = '(//tr[@aria-rowindex="1"]//td[@aria-colindex="3"])'
    die_records = '//label[contains(text(),"Read PIR/PRR")]//input'
    read_die = '//h6[text()="Die Records"]/parent::div/div[2]/div'
    summary_records = '//h6[text()="Summary Records"]/parent::div/label/div/input'

    # Actions
    def click_on_option(self, context, text):
        try:
            self.log.logger.info("Clicked on loader policy")
            option = '(//span[text()=' + text + '])[last()]'
            locator = (By.XPATH, option)
            helpers.click_element(context, locator)
        except Exception as e:
            attach(str(e), name="Error in clicked on loader policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            attach(str(ex), name="Assertion error in clicked on loader policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_create_policy_button(self, context):
        try:
            self.log.logger.info("Verifying the create policy button")
            create_policy_button = helpers.wait_for_visibility_of_element(context, self.create_policy, "xpath")
            create_policy_button.is_displayed()
        except Exception as e:
            self.log.logger.error("Verifying the create policy button")
            attach(str(e), name="Error in verifying the create policy button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Verifying the create policy button")
            attach(str(ex), name="Assertion error in verifying the create policy button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_on_create_policy_btn(self, context):
        try:
            self.log.logger.info("Clicked on create policy button")
            create_policy_button = helpers.wait_for_visibility_of_element(context, self.create_policy, "xpath")
            create_policy_button.click()
        except Exception as e:
            self.log.logger.error("Clicked on create policy button")
            attach(str(e), name="Error in clicked on create policy button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Clicked on create policy button")
            attach(str(ex), name="Assertion error in clicked on create policy button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_policy_name(self, context, text):
        # Reading data from yml file
        try:
            self.log.logger.info("Entered policy name")
            data = yaml_reader.data_reader_with_file_path(context, text, self.file)
            name = helpers.wait_for_visibility_of_element(context, self.policy_name, "xpath")
            feature_name = context.feature.filename
            feature_name = feature_name.split(".")[0].split("/")[1]
            date_time = datetime.now()
            new_policy_name = data['policyName'] + "for" + feature_name + " " + str(date_time)
            Constants.new_policy_name = new_policy_name
            attach(str(new_policy_name), name="Modify policy name",
                   attachment_type=AttachmentType.TEXT)
            helpers.send_data_in_fields(context, name, new_policy_name)

        except Exception as e:
            self.log.logger.error("Entered policy name")
            attach(str(e), name="Error in entered policy name"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Entered policy name")
            attach(str(ex), name="Assertion error in entered policy name"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_policy_version(self, context, text):
        try:
            self.log.logger.info("Entered policy description")
            # Reading data from yml file
            data = yaml_reader.data_reader_with_file_path(context, text, self.file)
            self.log.logger.info("Entered policy version")
            version = helpers.wait_for_visibility_of_element(context, self.policy_version, "xpath")
            helpers.send_data_in_fields(context, version, data['policyDesc'])

        except Exception as e:
            self.log.logger.error("Error in entered policy version")
            attach(str(e), name="Error in entered policy version"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in entered policy version")
            attach(str(ex), name="Assertion error in entered policy version"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_policy_desc(self, context, text):
        try:
            self.log.logger.info("Entered policy description")
            # Reading data from yml file
            data = yaml_reader.data_reader_with_file_path(context, text, self.file)
            desc = helpers.wait_for_visibility_of_element(context, self.policy_desc, "xpath")
            helpers.send_data_in_fields(context, desc, data['policyDesc'])

        except Exception as e:
            self.log.logger.error("Error in entered policy description")
            attach(str(e), name="Error in entered policy description"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in entered policy description")
            attach(str(ex), name="Assertion error in entered policy description"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_policy_owner_email(self, context, text):
        try:
            self.log.logger.info("Entered policy owner email address")
            # Enter data into owner input field
            owner_input_field = helpers.wait_for_visibility_of_element(context, self.policy_owner_email_input_field,
                                                                       "xpath")
            helpers.send_data_in_fields(context, owner_input_field, text)

        except Exception as e:
            self.log.logger.error("Error in entered policy owner email address")
            attach(str(e), name="Error in entered policy owner email address"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in entered policy owner email address")
            attach(str(ex), name="Assertion error in entered policy owner email address"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_policy_polling(self, context, text):
        try:
            self.log.logger.info(" Enter policy polling ")
            # Reading data from yml file
            data = yaml_reader.data_reader_with_file_path(context, text, self.file)
            poll = helpers.wait_for_visibility_of_element(context, self.policy_polling, "xpath")
            helpers.send_data_in_fields(context, poll, data['policyPolling'])
        except Exception as e:
            self.log.logger.error("Error in enter policy polling")
            attach(str(e), name="Error in enter policy polling"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in enter policy polling")
            attach(str(ex), name="Assertion error in enter policy polling"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_add_stage_btn(self, context):
        try:
            self.log.logger.info("Click add stage button")
            by_locator = (By.XPATH, self.add_stage)
            helpers.scroll_to_element(context, by_locator)
            helpers.click_element_using_js(context, by_locator)
        except Exception as e:
            self.log.logger.error("Error in click add stage button")
            attach(str(e), name="Error in click add stage button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in click add stage button")
            attach(str(ex), name="Assertion error in click add stage button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def select_stage(self, context, text):
        try:
            self.log.logger.info("Select stage :" + text)
            stage = '//a[text()=' + text + ']'
            helpers.scroll_to_element_with_locator(context, stage)
            helpers.click_element_with_locator(context, stage)
            self.log.logger.info("Stage selected")
        except Exception as e:
            self.log.logger.error("Error in select stage :" + text)
            attach(str(e), name="Error in select stage :" + text
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion Error in select stage :" + text)
            attach(str(ex), name="Assertion error in select stage :" + text
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_view_button(self, context):
        try:
            self.log.logger.info("Click on view button")
            helpers.scroll_to_element_with_locator(context,  self.view)
            helpers.click_element_with_locator(context,  self.view)
        except Exception as e:
            self.log.logger.error("Error in click on view button")
            attach(str(e), name="Error in click on view button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in click on view button")
            attach(str(ex), name="Assertion error in click on view button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def select_source(self, context, text):
        try:
            self.log.logger.info("Select the source : " + text)
            helpers.scroll_to_element_with_locator(context, self.source_format)
            helpers.click_element_with_locator(context, self.source_format)
            # source_btn = helpers.wait_for_visibility_of_element(context, self.source_format, "xpath")
            # context.driver.execute_script("arguments[0].click();", source_btn)
            format_ = '//a[text()="' + text + '"]'
            helpers.scroll_to_element_with_locator(context, format_)
            helpers.click_element_with_locator(context, format_)
            # element = context.driver.find_element_by_xpath(format_)
            # context.driver.execute_script("arguments[0].scrollIntoView();", element)
            # context.driver.execute_script("arguments[0].click();", element)
            allure.attach(context.driver.get_screenshot_as_png(), name="Add_Stage", attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.log.logger.error("Error in select the source : " + text)
            attach(str(e), name="Error in select the source : " + text
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion Error in select the source : " + text)
            attach(str(ex), name="Assertion error in select the source : " + text
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def source_cloud(self, context, text):
        try:
            self.log.logger.info("Enter source cloud")
            helpers.scroll_to_element_with_locator(context, self.source_of_file)
            helpers.click_element_with_locator(context, self.source_of_file)
            # storage = helpers.wait_for_visibility_of_element(context, self.source_of_file, "xpath")
            # context.driver.execute_script("arguments[0].click();", storage)
            source = '//a[contains(text(),' + text + ')]'
            element = context.driver.find_element_by_xpath(source)
            context.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            self.log.logger.error("Error in enter source cloud")
            attach(str(e), name="Error in enter source cloud"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in enter source cloud")
            attach(str(ex), name="Assertion error in enter source cloud"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def select_policy_step(self, context, policy_step):
        try:
            self.log.logger.info("Select policy step")
            helpers.scroll_to_element(context, self.policy_step_drop_down)
            helpers.click_element(context, self.policy_step_drop_down)
            source = '//button[text()=' + policy_step + ']'
            element = context.driver.find_element_by_xpath(source)
            context.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            self.log.logger.error("Error in enter source cloud")
            attach(str(e), name="Error in enter source cloud"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in enter source cloud")
            attach(str(ex), name="Assertion error in enter source cloud"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_source_container(self, context, text):
        try:
            self.log.logger.info("Enter container name for policy")
            data = yaml_reader.data_reader_with_file_path(context, text, self.file)
            element = context.driver.find_element_by_xpath(self.container)
            self.log.logger.info("DATA " + data['container'])
            helpers.send_data_in_fields(context, element, data['container'])
        except Exception as e:
            self.log.logger.error("Error in enter container name for policy")
            attach(str(e), name="Error in enter container name for policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in enter container name for policy")
            attach(str(ex), name="Assertion error in enter container name for policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_source_ftp_address(self, context, text):
        data = yaml_reader.data_reader_with_file_path(context, text, self.file)
        element = context.driver.find_element_by_xpath(self.ftp_address)
        self.log.logger.info("DATA " + data['ftp_address'])
        helpers.send_data_in_fields(context, element, data['ftp_address'])

    def enter_data_ftp_username(self, context, text):
        data = yaml_reader.data_reader_with_file_path(context, text, self.file)
        element = context.driver.find_element_by_xpath(self.ftp_username)
        self.log.logger.info("DATA " + data['ftp_username'])
        helpers.send_data_in_fields(context, element, data['ftp_username'])

    def enter_data_ftp_password(self, context, text):
        data = yaml_reader.data_reader_with_file_path(context, text, self.file)
        element = context.driver.find_element_by_xpath(self.ftp_password)
        self.log.logger.info("DATA " + data['ftp_password'])
        helpers.send_data_in_fields(context, element, data['ftp_password'])

    def enter_data_folder_to_transfer_files_from(self, context, text):
        data = yaml_reader.data_reader_with_file_path(context, text, self.file)
        element = context.driver.find_element_by_xpath(self.folder_to_transfer_files_from)
        self.log.logger.info("DATA " + data['folder_to_transfer_files_from'])
        helpers.send_data_in_fields(context, element, data['folder_to_transfer_files_from'])

    def select_schedule_mode(self, context, text):
        try:
            self.log.logger.info("Schedule mode selected")
            helpers.scroll_to_element_with_locator(context, self.type)
            helpers.click_element_with_locator(context, self.type)
            schedule_mode = '//a[text()=' + text + ']'
            helpers.click_element_with_locator(context, schedule_mode)
        except Exception as e:
            self.log.logger.error("Error in schedule mode selected")
            attach(str(e), name="Error in schedule mode selected"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in schedule mode selected")
            attach(str(ex), name="Assertion error in schedule mode selected"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def select_time(self, context):
        self.log.logger.info("Select time for policy")
        try:
            # Get current date
            now = datetime.now()
            # For scheduling in future time
            now_plus_2m = now + timedelta(minutes=0.5)

            self.exact_time = now_plus_2m.strftime("%m/%d/%Y, %I:%M %p").lstrip("0").replace(" 0", " ").lstrip("0").replace("/0","/")
            self.log.logger.info("Schedule time in utc: " + self.exact_time)
            self.future = now_plus_2m.strftime("%m/%d/%Y|%I:%M|%p")
            self.log.logger.info("Scheduling in Future time:  " + self.future)
            new = self.future.split("|")
            # Start time input field
            element = context.driver.find_element_by_xpath(self.start_time)
            element.clear()
            by_locator = (By.XPATH, self.start_time)
            value = new[0] + ", " + new[1] + " " + new[2]
            element.send_keys(keys.Keys.CONTROL + "a")
            element.send_keys(keys.Keys.BACK_SPACE)
            helpers.input_element(context, by_locator, value)
        except Exception as e:
            self.log.logger.error("Error in select time for policy")
            attach(str(e), name="Error in select time for policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in select time for policy")
            attach(str(ex), name="Assertion error in select time for policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def enter_polling_time(self, context, policy_name):
        try:
            self.log.logger.info("Enter polling interval time")
            data = yaml_reader.data_reader_with_file_path(context, policy_name, self.file)
            by_locator = (By.XPATH, self.policy_polling)
            helpers.input_element(context, by_locator, data['polling'])
        except Exception as e:
            self.log.logger.error("Error in enter polling interval time")
            attach(str(e), name="Error in enter polling interval time"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in enter polling interval time")
            attach(str(ex), name="Assertion error in enter polling interval time"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def hit_save_btn(self, context):
        try:
            self.log.logger.info("Click on save button")
            element = context.driver.find_element_by_xpath(self.save_btn)
            element.click()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            attach(str(current_time), name="Start time after clicking save button"
                   , attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error("Error in click on save button")
            attach(str(e), name="Error in click on save button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in click on save button")
            attach(str(ex), name="AssertionError in click on save button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_alert_message_from_screen(self, context, message):
        try:
            self.log.logger.info("Verifying " + message + " alert message")
            web_element_text = helpers.get_element_text(context, self.success_alert_message)
            boolean = message in web_element_text
            self.log.logger.info(
                str(boolean) + " getting : " + web_element_text + " contain " + message + " alert message ")
            assert message in web_element_text, "Not getting :" + message + " alert message "
            self.log.logger.info("Policy Saved!!")
        except Exception as e:
            self.log.logger.error("Error in verifying " + message + " alert message")
            attach(str(e), name="Error in verifying " + message + " alert message"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verifying " + message + " alert message")
            attach(str(ex), name="Assertion error in verifying " + message + " alert message"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_on_data_intake(self, context, text):
        try:
            self.log.logger.info("Clicked on data intake queue")
            element = '//a[text()="' + text + '"]'
            data_queue = helpers.wait_for_visibility_of_element(context, element, "xpath")
            data_queue.click()
        except Exception as e:
            self.log.logger.error("Error in clicked on data intake queue")
            attach(str(e), name="Error in clicked on data intake queue"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on data intake queue")
            attach(str(ex), name="Assertion error in clicked on data intake queue"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_policy(self, context, text):
        self.log.logger.info("Verify policy from data intake queue")
        try:
            flag = 1
            while flag < 4:
                try:
                    context.driver.refresh()
                    time.sleep(1)
                    by_locator = (By.XPATH, self.filter)
                    helpers.input_element(context, by_locator, text)
                    element = '//td[text()="' + self.exact_time + '"]'
                    by_locator = (By.XPATH,  element)
                    exec_start_time = helpers.get_element_text(context, by_locator)
                    by_locator = (By.XPATH, self.success_msg)
                    status = helpers.verify_element_displayed(context, by_locator)
                    assert status, "Error in verify success status of policy from data intake queue"
                    current_time = datetime.now().strftime("%H:%M:%S")
                    self.log.logger.info("Getting success status at :" + str(current_time))
                    attach(str(current_time), name="Getting success status from data intake queue",
                           attachment_type=AttachmentType.TEXT)
                    self.log.logger.info("Verify policy is successfully executed")
                    if len(exec_start_time) > 0:
                        break
                except Exception as e:
                    flag = flag + 1
                    if flag == 3:
                        assert False, "Not getting success status from data intake queue"

        except Exception as e:
            self.log.logger.error("Error in verify policy from data intake queue")
            attach(str(e), name="Error in verify policy from data intake queue"
                   , attachment_type=AttachmentType.TEXT)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.log.logger.info("Getting failure status at :" + str(current_time))
            attach(str(current_time), name="Getting failure status from data intake queue",
                   attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion Error in verify policy from data intake queue")
            attach(str(ex), name="Assertion in verify policy from data intake queue"
                   , attachment_type=AttachmentType.TEXT)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.log.logger.info("Getting failure status at :" + str(current_time))
            attach(str(current_time), name="Getting failure status from data intake queue",
                   attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_policy_from_step_intake_view(self, context, expected_status):
        self.log.logger.info("Verify policy from step intake queue")
        status = ""
        try:
            while True:
                now_time = datetime.now()
                future_time = datetime.strptime(self.future, "%m/%d/%Y|%I:%M|%p")
                end_time = now_time.minute - future_time.minute
                if end_time < 4:
                    boolean = str(now_time.hour) + ":" + str(now_time.minute) >= str(future_time.hour) + ":" + str(future_time.minute)
                    time.sleep(1)
                    helpers.click_element(context, self.step_intake_queue)
                    time.sleep(1)
                    helpers.input_element(context, self.step_intake_queue_policy_name_input_field,
                                          Constants.new_policy_name)
                    if boolean:
                        try:
                            time.sleep(1)
                            helpers.verify_element_displayed(context, self.step_intake_queue_status)
                            time.sleep(1)
                            status = helpers.get_element_text(context, self.step_intake_queue_status)
                            assert expected_status in status, "Getting "+status+" status from step intake queue"
                            break
                        except Exception as e:
                            context.driver.refresh()
                    else:
                        context.driver.refresh()
                else:
                    helpers.click_element(context, self.step_intake_queue)
                    time.sleep(1)
                    helpers.input_element(context, self.step_intake_queue_policy_name_input_field,
                                          Constants.new_policy_name)
                    time.sleep(1)
                    assert False, "Getting " + status + " status from step intake queue"
        except AssertionError as ex:
            self.log.logger.error(str(ex))
            attach(str(ex), name="Assertion error in verify policy from step intake queue"
                   , attachment_type=AttachmentType.TEXT)
            assert False, "Not getting "+expected_status+" status from step intake queue"
        except Exception as e:
            self.log.logger.error("Error in verify policy from step intake queue")
            attach(str(e), name="Error in verify policy from step intake queue"
                   , attachment_type=AttachmentType.TEXT)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.log.logger.info("Getting failure status at :" + str(current_time))
            attach(str(current_time), name="Getting failure status from step intake queue",
                   attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion Error in verify policy from data intake queue")
            attach(str(ex), name="Assertion in verify policy from data intake queue"
                   , attachment_type=AttachmentType.TEXT)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.log.logger.info("Getting failure status at :" + str(current_time))
            attach(str(current_time), name="Getting failure status from data intake queue",
                   attachment_type=AttachmentType.TEXT)
            assert False, ex

    def download_converted_file(self, context):
        self.log.logger.info("File is Successfully downloaded from AWS S3")
        try:
            by_locator = (By.XPATH, self.target_file)
            target_location = helpers.get_element_text(context, by_locator)
            by_locator = (By.XPATH, self.target_file)
            source_location = helpers.get_element_text(context, by_locator)
            # location = target_location.text
            if "s3://" in str(target_location):
                bucket_file_download.download_from_aws(context, target_location, source_location)
                self.log.logger.info("Downloaded file from AWS S3 Bucket")
            self.log.logger.info("File location: " + target_location)
        except Exception as e:
            self.log.logger.error("Error in file downloaded from AWS S3")
            attach(str(e), name="Error in file downloaded from AWS S3"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in file downloaded from AWS S3")
            attach(str(ex), name="Assertion error in file downloaded from AWS S3"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def check_die_records(self, context, text):
        self.log.logger.info("Check die record")
        try:
            die_checkbox = '//label[text()=' + text + ']//div//input'
            helpers.scroll_to_element_with_locator(context, die_checkbox)
            helpers.click_element_with_locator(context, die_checkbox)
        except Exception as e:
            self.log.logger.error("Error in check die record")
            attach(str(e), name="Error in check die record"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in check die record")
            attach(str(ex), name="Assertion error in check die record"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def check_summary_records(self, context):
        self.log.logger.info("Check summary record")
        try:
            records = context.driver.find_elements_by_xpath(self.summary_records)
            for count in range(1, len(records) + 1):
                element = '(//h6[text()="Summary Records"]/parent::div/label/div/input)['
                element += str(count)
                element += ']'
                sum_record = context.driver.find_element_by_xpath(element)
                context.driver.execute_script("arguments[0].scrollIntoView();", sum_record)
                context.driver.execute_script("arguments[0].click();", sum_record)
        except Exception as e:
            self.log.logger.error("Error in check summary record")
            attach(str(e), name="Error in check summary record"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in check summary record")
            attach(str(ex), name="Assertion error in check summary record"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def check_summary_records_for_specific_checkbox(self, context, check_box_texts):
        try:
            HBR = "HBR"
            SBR = "SBR"
            TSR = "TSR"
            comma = ","
            check_box_text_list = []
            if comma in check_box_texts:
                check_box_text_list = check_box_texts.split(comma)
            else:
                check_box_text_list.append(check_box_texts)
            for check_box_text in check_box_text_list:
                check_box_text = check_box_text.strip()
                if HBR in check_box_text:
                    check_box_text = check_box_text.split(HBR)[0]
                    label_text = check_box_text + "Hard Bin Record"
                elif SBR in check_box_text:
                    check_box_text = check_box_text.split(SBR)[0]
                    label_text = check_box_text + "Soft Bin Record"
                else:
                    check_box_text = check_box_text.split(TSR)[0]
                    label_text = check_box_text + "Test Synopsis Record"
                self.log.logger.info("Check summary record")
                element = '(//h6[contains(text(),"Summary")]/parent::div/label[contains(text(),"' + label_text + '")]//input)[last()]'
                by_locator = (By.XPATH, element)
                helpers.scroll_to_element(context, by_locator)
                helpers.click_element(context, by_locator)
        except Exception as e:
            self.log.logger.error("Error in check summary record")
            attach(str(e), name="Error in check summary record"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in check summary record")
            attach(str(ex), name="Assertion error in check summary record"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Actions
    def select_selection_criteria(self, context, table_names):
        self.log.logger.info("Clicked on Selection Criteria")
        try:
            helpers.click_element(context, web_elements.SelectSelectionCriteria)
            self.log.logger.info("Clicked on Selection Criteria")
            selection_criteria_data_list = table_names.split(",")
            report_helper.selecting_facility_name_from_selection_criteria(context,
                                                                          selection_criteria_data_list[
                                                                              0])
            report_helper.selecting_lot_name_from_selection_criteria(context,
                                                                     selection_criteria_data_list[1])
            report_helper.selecting_wafer_name_from_selection_criteria(context,
                                                                       selection_criteria_data_list[2])
            report_helper.selecting_test_parameters_from_selection_criteria(context,
                                                                            selection_criteria_data_list[
                                                                                3])
            helpers.click_element(context, web_elements.SelectAndCloseBtn)
        except Exception as e:
            self.log.logger.error("Error in clicked on Selection Criteria")
            attach(str(e), name="Error in entered policy name"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on Selection Criteria")
            attach(str(ex), name="Assertion error in clicked on Selection Criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_selection_criteria(self, context):
        self.log.logger.info("Clicked on Selection Criteria")
        try:
            helpers.click_element(context, web_elements.SelectSelectionCriteria)
        except Exception as e:
            self.log.logger.error("Error in clicked on Selection Criteria")
            attach(str(e), name="Error in entered policy name"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on Selection Criteria")
            attach(str(ex), name="Assertion error in clicked on Selection Criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Actions
    def verify_the_data_selection_criteria_for_table(self, context, table_names):
        self.log.logger.info("Verifying the data from selection criteria")
        try:
            for file_name in self.facility_name.keys():
                for table_name in table_names.split(","):
                    time.sleep(2)
                    table_name = table_name.strip()
                    if "Facility" in table_name:
                        selection_criteria_helper.verify_facility_name_from_selection_criteria(context, table_name,
                                                                                               self.facility_name[
                                                                                                   file_name])
                    elif "Work Center" in table_name:
                        selection_criteria_helper.verify_work_center_from_selection_criteria(context, table_name,
                                                                                             self.work_center_list[
                                                                                                 file_name])
                    elif "Device" in table_name:
                        selection_criteria_helper.verify_device_from_selection_criteria(context, table_name,
                                                                                        self.device_list[file_name])
                    elif "Test Program" == table_name:
                        selection_criteria_helper.verify_test_program_from_selection_criteria(context, table_name,
                                                                                              self.test_program_list[
                                                                                                  file_name])
                    elif "Test Program Revision" == table_name:
                        selection_criteria_helper.verify_test_program_revision_from_selection_criteria(context, table_name,
                                                                                                       self.test_program_revision_list[
                                                                                                           file_name])
                    elif "Lot" in table_name:
                        selection_criteria_helper.verify_lot_name_from_selection_criteria(context, table_name,
                                                                                          self.lot_list[file_name])
                    elif "Wafer" in table_name:
                        selection_criteria_helper.verify_wafer_name_from_selection_criteria(context, table_name,
                                                                                            self.wafer_list[file_name])
                    elif "Test Parameter" in table_name:
                        if len(self.test_parameter_name_list[file_name]) > 0:
                            selection_criteria_helper.verify_test_parameters_from_selection_criteria(context, table_name,
                                                                                                     self.test_parameter_name_list[
                                                                                                         file_name])
                        else:
                            self.log.logger.warn("Test parameter is null")
        except Exception as e:
            self.log.logger.error("Error in verifying the data from selection criteria")
            attach(str(e), name="Error in verifying the data from selection criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verifying the data from selection criteria")
            attach(str(ex), name="Assertion error in verifying the data from selection criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_on_select_and_close_button(self, context):
        try:
            self.log.logger.info("Clicked on Selection And Close Criteria")
            helpers.click_element(context, web_elements.SelectAndCloseBtn)
        except Exception as e:
            self.log.logger.error("Error in clicked on Selection And Close Criteria")
            attach(str(e), name="Error in clicked on Selection And Close Criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on Selection And Close Criteria")
            attach(str(ex), name="Assertion error in clicked on Selection And Close Criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Actions
    def get_name_of_table_column(self, context, table_names, policy_name, mark_file_path):
        try:
            self.log.logger.info("Getting name of " + table_names + " data from marked file")
            self.log.logger.info("Getting name of " + table_names + " data from marked file")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[mark_file_path])
            table_name_list = table_names.split(",")
            self.facility_name = {}
            for file_name in files:
                for table_data in table_name_list:
                    self.facility_name[file_name] = []
                    self.facility_name[file_name] = database.get_facility_name(context, file_name)
                    # self.facility_name[file_name] = Constants.marked_facility_name[file_name]
                    all_data = database.get_table_column_name_against_facility(context, self.facility_name[file_name])
                    if "Facility" in table_data.strip():
                        # self.facility_name[file_name] = Constants.marked_facility_name[file_name]
                        self.facility_name[file_name] = database.get_facility_name(context, file_name)
                    elif "Work Center" in table_data.strip():
                        self.work_center_list[file_name] = all_data[1]
                    elif "Device" in table_data:
                        self.device_list[file_name] = all_data[2]
                    elif "Test Program" == table_data.strip():
                        self.test_program_list[file_name] = all_data[3]
                    elif "Test Program Revision" == table_data.strip():
                        self.test_program_revision_list[file_name] = all_data[4]
                    elif "Lot" in table_data.strip():
                        self.lot_list[file_name] = all_data[5]
                    elif "Wafer" in table_data.strip():
                        self.wafer_list[file_name] = all_data[6]
                    elif "Test Parameter" in table_data:
                        self.test_parameter_name_list[file_name] = all_data[0]
        except Exception as e:
            self.log.logger.error("Error in getting name of " + table_names + " data from marked file")
            attach(str(e), name="Error in getting name of " + table_names + " data from marked file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in getting name of " + table_names + " data from marked file")
            attach(str(ex), name="Assertion error  in getting name of " + table_names + " data from marked file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Select selection criteria for specific record #
    def select_selection_criteria_for_table(self, context, table_names):
        try:
            self.log.logger.info("Select data for " + table_names + "in Selection Criteria")
            # context.driver.execute_script("document.body.style.zoom='zoom %'")
            table_names = table_names.split(",")
            self.log.logger.info("Data of file is verified from database after marking the file")
            for file_name in self.facility_name.keys():
                for table_name in table_names:
                    time.sleep(2)
                    table_name = table_name.strip()
                    if "Facility" in table_name:
                        selection_criteria_helper.selecting_facility_from_selection_criteria(context, table_name,
                                                                                             self.facility_name[
                                                                                                 file_name])
                    elif "Work Center" in table_name:
                        selection_criteria_helper.selecting_work_center_from_selection_criteria(context, table_name,
                                                                                                self.work_center_list[
                                                                                                    file_name])
                    elif "Device" in table_name:
                        selection_criteria_helper.selecting_device_from_selection_criteria(context, table_name,
                                                                                           self.device_list[file_name])
                    elif "Test Program" == table_name:
                        selection_criteria_helper.selecting_test_program_from_selection_criteria(context, table_name,
                                                                                                 self.test_program_list[
                                                                                                     file_name])
                    elif "Test Program Revision" == table_name:
                        selection_criteria_helper.selecting_test_program_revision_from_selection_criteria(context, table_name,
                                                                                                          self.test_program_revision_list[
                                                                                                              file_name])
                    elif "Lot" in table_name:
                        selection_criteria_helper.selecting_lot_name_from_selection_criteria(context, table_name,
                                                                                             self.lot_list[file_name])
                    elif "Wafer" in table_name:
                        selection_criteria_helper.selecting_wafer_name_from_selection_criteria(context, table_name,
                                                                                               self.wafer_list[
                                                                                                   file_name])
                    elif "Test Parameter" in table_name:
                        if len(self.test_parameter_name_list[file_name]) > 0:
                            if "One" in table_name.strip():
                                table_name = table_name.split("One")[1].strip()
                                selection_criteria_helper.selecting_specific_test_parameters_from_selection_criteria(
                                    context, table_name,
                                    self.test_parameter_name_list[
                                        file_name][0])
                            else:
                                selection_criteria_helper.selecting_test_parameters_from_selection_criteria(context, table_name,
                                                                                                            self.test_parameter_name_list[
                                                                                                                file_name])
                        else:
                            self.log.logger.warn("Test parameter is null")
        except Exception as e:
            self.log.logger.error("Error in select data for " + str(table_names) + "in Selection Criteria")
            attach(str(e), name="Error in select data for " + str(table_names) + "in Selection Criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in select data for " + str(table_names) + "in Selection Criteria")
            attach(str(ex), name="Assertion error in select data for " + str(table_names) + "in Selection Criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

        # Select selection criteria for specific record #

    def select_selection_criteria_for_report(self, context, table_names):
        try:
            self.log.logger.info("Select data for " + table_names + "in Selection Criteria")
            table_names = table_names.split(",")
            for table_name in table_names:
                if "Facility" in table_name.strip():
                    report_helper.selecting_facility_from_selection_criteria(context, table_name)
                elif "Work Center" in table_name.strip():
                    report_helper.selecting_work_center_from_selection_criteria(context, table_name)
                elif "Device" in table_name.strip():
                    report_helper.selecting_device_from_selection_criteria(context, table_name)
                elif "Test Program" == table_name.strip():
                    report_helper.selecting_test_program_from_selection_criteria(context, table_name)
                elif "Test Program Revision" == table_name.strip():
                    report_helper.selecting_test_program_revision_from_selection_criteria(context, table_name)
                elif "NGP754" in table_name.strip() or "Demo LOT" in table_name.strip():
                    report_helper.selecting_lot_name_from_selection_criteria(context, table_name)
                elif "02" in table_name.strip() or "W006" in table_name.strip():
                    report_helper.selecting_wafer_name_from_selection_criteria(context, table_name)
                elif "wp_" in table_name.strip() or "tot" in table_name.strip():
                    if len(table_name) > 0:
                        report_helper.selecting_test_parameters_from_selection_criteria(context, table_name)
                    else:
                        self.log.logger.warn("Test parameter is null")
        except Exception as e:
            self.log.logger.error("Error in select data for " + table_names + "in Selection Criteria")
            attach(str(e), name="Error in select data for " + table_names + "in Selection Criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in select data for " + table_names + "in Selection Criteria")
            attach(str(ex), name="Assertion error in select data for " + table_names + "in Selection Criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

        # Select selection criteria for specific record #

    def verify_automatically_selected_value_field_in_table(self, context, table_names):
        try:
            self.log.logger.info("Verifying automatically selected value field in table")
            table_names = table_names.split(",")
            for table_name in table_names:
                report_helper.verify_automatically_selected_table_value(context, table_name)

        except Exception as e:
            self.log.logger.error("Verifying automatically selected value field in table")
            attach(str(e), name="Error in verifying automatically selected value field in table"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Entered policy name")
            attach(str(ex), name="Assertion error in verifying automatically selected value field in table"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex


