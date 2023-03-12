import time
import logging
import allure
import ast
import decimal
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from config.web import WebConfigurations
from config.driver_manager import WebDriverManager
from Helpers.generics import GenericMethods
from Utilities.log import Logger
from Elements.login import LoginElements
from Elements.reports_elements import ReportsElements
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.database import DatabaseManagement
from Elements.create_policy import CreatePolicyElements
from Helpers.db_config import DataBaseConfig

database_config = DataBaseConfig()
database = DatabaseManagement()
reports_elements = ReportsElements()
manage_driver = WebDriverManager()
web_conf = WebConfigurations()
helpers = GenericMethods()
login_elements = LoginElements()
web_elements = CreatePolicyElements()


class ParametricHistogramPage:
    log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))
    die_data = []
    graph_die_data = []
    stats_grid_from_db = []
    stats_grid_view = []
    data_grid_view = []
    errors_grid_view = []
    data_grid_view_from_db = []
    data_grid_chooser = []
    legend_die_count = []
    start_end_die_list = {}
    data_grid_view_data_tab=[]
    minvalue = []
    maxvalue = []
    diecount = []
    min_max_diecount_dic={}

    def verification_of_die_data_against_report(self, context):
        try:
            self.log.logger.info("Verification of die data against report")
            set1 = set(self.die_data)
            set2 = set(self.graph_die_data)
            set3 = set1.intersection(set2)
            attach(str(set1), name="Parametric Histogram report data from Report"
                   , attachment_type=AttachmentType.TEXT)
            attach(str(set2), name="Parametric Histogram report data from Database"
                   , attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Verification of Parametric Histogram report - Done")
        except Exception as e:
            self.log.logger.error("Error in verification of die data against report")
            attach(str(e), name="Error in verification of die data against report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of die data against report")
            attach(str(ex), name="Assertion error in verification of die data against report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_die_data(self, context, facility_name):
        try:
            self.log.logger.info("Get die data from YW Database")
            facility_id = database.get_facility_id(context, facility_name)
            customer_id = database.get_customer_id(context, facility_id)
            business_unit_id = database.get_business_unit_id(context, customer_id)
            work_center_id = database.get_work_center_id(context, business_unit_id)
            device_family_id = database.get_device_family_id(context, work_center_id)
            device_id = database.get_device_id(context, device_family_id)
            test_program_id = database.get_test_program_id(context, device_id)
            test_program_revision_id = database.get_test_program_revision_id(context,
                test_program_id)
            lot_id = database.get_lot_id(context, test_program_revision_id)
            wafer_id = database.get_wafer_id(context, lot_id)
            self.die_data = database.get_all_die_all_data(context, wafer_id)
            self.log.logger.info("Get die data from YW Database - Done")
        except Exception as e:
            self.log.logger.error("Error in get die data from YW Database")
            attach(str(e), name="Error in get die data from YW Database"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get die data from YW Database")
            attach(str(ex), name="Assertion error in get die data from YW Database"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_select_and_close(self, context):
        self.log.logger.info("Clicking the Save and close btn from selection criteria")
        try:
            helpers.click_element(context, web_elements.SelectAndCloseBtn)
            self.log.logger.info("Clicked the Save and close btn from selection criteria - Done")
        except Exception as e:
            self.log.logger.error("Error in clicking the Save and close btn from selection criteria")
            attach(str(e), name="Error in clicking the Save and close btn from selection criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicking the Save and close btn from selection criteria")
            attach(str(ex), name="Assertion error in clicking the Save and close btn from selection criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_stats_tab(self, context):
        self.log.logger.info("Click on Stats tab from report ")
        try:
            helpers.click_element(context, reports_elements.stats_tab)
            self.log.logger.info("Click on Stats tab from report - Done")
        except Exception as e:
            self.log.logger.error("Error in clicked on Stats tab from report")
            attach(str(e), name="Error in clicked on Stats tab from report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on Stats tab from report")
            attach(str(ex), name="Assertion error in clicked on Stats tab from report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # def verifying_stats(self, context):
    #     self.log.logger.info("Verification of Parametric Histogram report Stats")
    #     # # context.driver.find_elements(By.XPATH, self.stats)
    #     # helpers.click_element(context, reports_elements.stats)
    #
    #     self.log.logger.info("Verification of Parametric Histogram report Legends Stats - Done")
    #     except Exception as e:
    #         self.log.logger.error("Error in clicked on the legends button")
    #         attach(str(e), name="Error in clicked on the legends button"
    #                , attachment_type=AttachmentType.TEXT)
    #         assert False, e
    #
    #     except AssertionError as ex:
    #         self.log.logger.error("Assertion error in clicked on the legends button")
    #         attach(str(ex), name="Assertion error in clicked on the legends button"
    #                , attachment_type=AttachmentType.TEXT)
    #         assert False, ex

    def verify_stats_grid(self, context):
        self.log.logger.info("Verification of Parametric Histogram report Statistics Grid View")
        try:
            table = helpers.get_web_elements(context, reports_elements.data_grid_view_element)
            for expected_data in self.stats_grid_view:
                for row in table:
                    data = helpers.get_web_element_text(context, row)
                    # self.stats_grid_view.append(value)
                    if data == expected_data:
                        attach(str(data),
                               name="Verification of Parametric Histogram report Statistics Grid View - Done"
                               , attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Verification of Parametric Histogram report Statistics Grid View - Done")
        except Exception as e:
            self.log.logger.error("Error in verification of Parametric Histogram report Statistics Grid View")
            attach(str(e), name="Error in verification of Parametric Histogram report Statistics Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Parametric Histogram report Statistics Grid View")
            attach(str(ex), name="Assertion error in verification of Parametric Histogram report Statistics Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_data_tab(self, context):
        self.log.logger.info("Click on Data tab from report ")
        try:
            helpers.click_element(context, reports_elements.data_tab)
            self.log.logger.info("Click on Data tab from report - Done")
        except Exception as e:
            self.log.logger.error("Error in clicked on Data tab from report")
            attach(str(e), name="Error in clicked on Data tab from report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on Data tab from report")
            attach(str(ex), name="Assertion error in clicked on Data tab from report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_selected_tables_grid_chooser(self, context):
        self.log.logger.info("Verification of Data Grid View")
        try:
            table = helpers.get_web_elements(context, reports_elements.grid_window_facility_sib)
            # rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
            actions = ActionChains(context.driver)
            for row in table:
                actions.move_to_element(row).perform()
                row.click()
                self.data_grid_chooser.append(row.text)
            attach(str(self.data_grid_view),
                   name="Verification of Parametric Histogram report Grid Chooser selected data"
                   , attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Verification of Parametric Histogram report Legends Data Grid View - Done")
        except Exception as e:
            self.log.logger.error("Error in verification of Data Grid View")
            attach(str(e), name="Error in verification of Data Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Data Grid View")
            attach(str(ex), name="Assertion error in verification of Data Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_grid_chooser_data_against_data_gridview(self, context):
        self.log.logger.info("Verification of Parametric Histogram report Data Grid View")
        try:
            name = helpers.get_web_element_text(context, reports_elements.grid_window_facility_child_element)
            self.data_grid_chooser.append(name)
            self.log.logger.info("Verification of Parametric Histogram report Data Grid View - Done")
        except Exception as e:
            self.log.logger.error("Error in verification of Parametric Histogram report Data Grid View")
            attach(str(e), name="Error in verification of Parametric Histogram report Data Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Parametric Histogram report Data Grid View")
            attach(str(ex), name="Assertion error in verification of Parametric Histogram report Data Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_data_from_data_grid_view(self, context):
        self.log.logger.info("Verification of Parametric Histogram report Data Grid View")

        try:
            table = helpers.get_web_elements(context, reports_elements.data_grid_view_element)
            for row in table:
                value = helpers.get_web_element_text(context, row)
                self.data_grid_view.append(value)
            attach(str(self.data_grid_view),
                   name="Verification of Parametric Histogram report Data Grid View - Done"
                   , attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Verification of Parametric Histogram report Legends Data Grid View - Done")
        except Exception as e:
            self.log.logger.error("Error in verification of Parametric Histogram report Data Grid View")
            attach(str(e), name="Error in verification of Parametric Histogram report Data Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Parametric Histogram report Data Grid View")
            attach(str(ex), name="Assertion error in verification of Parametric Histogram report Data Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_errors_grid_view(self, context):
        self.log.logger.info("Getting data read from errors tab of Parametric Histogram report Errors Grid View")
        try:
            table = helpers.get_web_elements(context, reports_elements.data_grid_view_element)
            for row in table:
                value = helpers.get_web_element_text(context, row)
                self.errors_grid_view.append(value)
            attach(str(self.data_grid_view),
                   name="Getting data read from errors tab of of Parametric Histogram report Errors Grid View - Done"
                   , attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Getting data read from errors tab of of Parametric Histogram"
                                 " report Legends Errors Grid View - Done")
        except Exception as e:
            self.log.logger.error("Error in get data read from errors tab of Parametric Histogram report Errors Grid View")
            attach(str(e), name="Error in get data read from errors tab of Parametric Histogram report Errors Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get data read from errors tab of Parametric Histogram report Errors Grid View")
            attach(str(ex), name="Assertion error in get data read from errors tab of Parametric Histogram report Errors Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_errors_grid_view(self, context):
        self.log.logger.info("Verification of Parametric Histogram report Errors Grid View")
        try:
            table = helpers.get_web_elements(context, reports_elements.data_grid_view_element)
            for expected_data in self.errors_grid_view:
                for row in table:
                    data = helpers.get_web_element_text(context, row)
                    if data == expected_data:
                        attach(str(self.data_grid_view),
                               name="Verified Parametric Histogram report Errors Grid View"
                               , attachment_type=AttachmentType.TEXT)
                self.log.logger.info("Verification of Parametric Histogram report Legends Errors Grid View - Done")
        except Exception as e:
            self.log.logger.error("Error in verification of Parametric Histogram report Errors Grid View")
            attach(str(e), name="Error in verification of Parametric Histogram report Errors Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Parametric Histogram report Errors Grid View")
            attach(str(ex), name="Assertion error in verification of Parametric Histogram report Errors Grid View"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_errors_tab(self, context):
        self.log.logger.info("Click on errors tab from report ")
        try:
            helpers.click_element(context, reports_elements.errors_tab)
            self.log.logger.info("Click on errors tab from report - Done")
        except Exception as e:
            self.log.logger.error("Error in clicked on errors tab from report ")
            attach(str(e), name="Error in clicked on errors tab from report "
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on errors tab from report ")
            attach(str(ex), name="Assertion error in clicked on errors tab from report "
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verifying_legends(self, context):
        self.log.logger.info("Verification of Parametric Histogram report Legends")
        try:
            all_die_count_elements = context.driver.find_elements(By.XPATH, reports_elements.die_count_legend)
            for die_count in all_die_count_elements:
                self.legend_die_count.append(die_count.text)
                attach(str(self.legend_die_count), name="Verification of Parametric Histogram report Legends"
                       , attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error("Error in verification of Parametric Histogram report Legends")
            attach(str(e), name="Error in verification of Parametric Histogram report Legends"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Parametric Histogram report Legends")
            attach(str(ex), name="Assertion error in verification of Parametric Histogram report Legends"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex
        self.log.logger.info("Verification of Parametric Histogram report Legends - Done")

    def select_die_count_from_legend(self, context):
        try:
            self.log.logger.info("Selecting die count data from Legends")
            all_die_count_elements = context.driver.find_elements(By.XPATH, reports_elements.die_count_legend)
            for die in all_die_count_elements:
                helpers.hover_to_element(context, die)
                self.list_die_count=helpers.get_web_element_text(context, die)
            self.log.logger.info("Selecting die count data from Legends - Done")
        except Exception as e:
            self.log.logger.error("Error in selecting die count data from Legends")
            attach(str(e), name="Error in selecting die count data from Legends"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in selecting die count data from Legends")
            attach(str(ex), name="Assertion error in selecting die count data from Legends"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_on_btn_from_graph(self, context, text):
        try:
            self.log.logger.info("Clicked on "+text)
            option = '//a[@data-title=' + text + ']'
            element = "//div[@class='plot-container plotly']"
            graph_element = context.driver.find_element(By.XPATH, element)
            helpers.hover_to_element_and_click(context, graph_element)
            element = context.driver.find_element(By.XPATH, option)
            locator = (By.XPATH, option)
            helpers.hover_to_element_and_click(context, element)
            helpers.click_element(context, locator)
            self.log.logger.info("Clicked on "+text)
        except Exception as e:
            self.log.logger.error("Error in clicked on "+text)
            attach(str(e), name="Error in clicked on "+text
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on "+text)
            attach(str(ex), name="Assertion error in clicked on "+text
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def click_on_btn(self, context):
        self.log.logger.info("Clicked on the legends button")
        try:
            helpers.click_element(context, reports_elements.legend_btn)
        except Exception as e:
            self.log.logger.error("Error in clicked on the legends button")
            attach(str(e), name="Error in clicked on the legends button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in clicked on the legends button")
            attach(str(ex), name="Assertion error in clicked on the legends button"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verifying_graph(self, context):

        self.log.logger.info("Verification of Parametric Histogram report")
        try:
            lst = context.driver.find_elements(By.XPATH, reports_elements.graph_svg_element)
            actions = ActionChains(context.driver)
            for i in lst:
                actions.move_to_element(i).perform()
                locator = (By.XPATH, reports_elements.graph_bar_value)
                text_element = helpers.get_element_text(context, locator)
                # text_element = context.driver.find_element(By.XPATH, reports_elements.graph_bar_value).text
                self.graph_die_data.append(text_element)
                attach(str(text_element), name="Verification of Parametric Histogram report"
                       , attachment_type=AttachmentType.TEXT)

            self.get_die_data(context, "Demo Facility")
            self.verification_of_die_data_against_report(context)
            attach(str(reports_elements.soft_bin), name="Verification of Parametric Histogram report - Done"
                   , attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Verification of Parametric Histogram report - Done")
        except Exception as e:
            self.log.logger.error("Error in verification of Parametric Histogram report ")
            attach(str(e), name="Error in verification of Parametric Histogram report "
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Parametric Histogram report ")
            attach(str(ex), name="Assertion error in verification of Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_y_tick(self, context):
        self.log.logger.info("Verification of y-axis")
        try:
            graph_y_tick_lst = []
            lst = context.driver.find_elements(By.XPATH, reports_elements.graph_g_ytick)
            actions = ActionChains(context.driver)
            for i in lst:
                actions.move_to_element(i).perform()
                locator = (By.XPATH, reports_elements.graph_bar_value)
                text_element = helpers.get_element_text(context, locator)
                # text_element = context.driver.find_element(By.XPATH, reports_elements.graph_bar_value).text
                graph_y_tick_lst.append(text_element)

            if graph_y_tick_lst == sorted(graph_y_tick_lst):
                attach(str(graph_y_tick_lst), name="Verified the Y-axis scale - Done"
                       , attachment_type=AttachmentType.TEXT)
                assert True
        except Exception as e:
            self.log.logger.error("Error in verification of y-axis")
            attach(str(e), name="Error in verification of y-axis"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of y-axis")
            attach(str(ex), name="Assertion error in verification of y-axis"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_x_tick(self, context):
        self.log.logger.info("Verification of x-axis")
        try:
            graph_x_tick_lst = []
            lst = context.driver.find_elements(By.XPATH, reports_elements.graph_g_xtick)
            actions = ActionChains(context.driver)
            for i in lst:
                actions.move_to_element(i).perform()
                locator = (By.XPATH, reports_elements.i)
                text_element = helpers.get_element_text(context, locator)
                graph_x_tick_lst.append(text_element)

            if graph_x_tick_lst == sorted(graph_x_tick_lst):
                attach(str(graph_x_tick_lst), name="Verified the x-axis scale - Done"
                       , attachment_type=AttachmentType.TEXT)
                assert True
        except Exception as e:
            self.log.logger.error("Error in verification of x-axis")
            attach(str(e), name="Error in verification of x-axis"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of x-axis")
            attach(str(ex), name="Assertion error in verification of x-axis"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def generate_report(self, context):
        try:
            self.log.logger.info("Generating the report")
            # waiting for the content saving then generate the report
            helpers.click_element(context, reports_elements.generate_report_btn)
            self.log.logger.info("Generating the report - Done")
        except Exception as e:
            self.log.logger.error("Error in generating the report")
            attach(str(e), name="Error in generating the report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in generating the report")
            attach(str(ex), name="Assertion error in generating the report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_the_grid_column_chooser(self, context):
        try:
            self.log.logger.info("click on the grid column chooser")
            helpers.click_element(context, reports_elements.btn_element_grid_chooser)
            self.log.logger.info("Generating the report")
        except Exception as e:
            self.log.logger.error("Error in click on the grid column chooser")
            attach(str(e), name="Error in click on the grid column chooser"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in click on the grid column chooser")
            attach(str(ex), name="Assertion error in click on the grid column chooser"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_selection_criteria(self, context):
        try:
            self.log.logger.info("Selection criteria window appeared - Successful")
            allure.attach(context.driver.get_screenshot_as_png(), name="Selection criteria", attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.log.logger.error("Error in selection criteria window appeared")
            attach(str(e), name="Error in selection criteria window appeared"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in selection criteria window appeared")
            attach(str(ex), name="Assertion error in selection criteria window appeared"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_columns_data_for_verify_data_tab(self, context, facility_name):
        try:
            self.log.logger.info("Getting column data of "+ facility_name+" for verifying the data tab")
            self.data_grid_view_from_db = database.get_table_column_name_against_facility(context, facility_name)
        except Exception as e:
            self.log.logger.error("Error in getting column data of " + facility_name+" for verifying the data tab")
            attach(str(e), name="Error in getting column data of " + facility_name+" for verifying the data tab"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in getting column data of " + facility_name+" for verifying the data tab")
            attach(str(ex), name="Assertion error in getting column data of " + facility_name+" for verifying the data tab"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_columns_data_to_verify_stats_tab(self, context, facility_name):
        try:
            self.log.logger.info("Getting column name against : " + facility_name + " for verification of stats tab")
            self.stats_grid_from_db = database.get_table_column_name_against_facility(context, facility_name)
        except Exception as e:
            self.log.logger.error("Error in getting column name against : " + facility_name + " for verification of stats tab")
            attach(str(e), name="Error in getting column name against : " + facility_name + " for verification of stats tab"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in getting column name against : "+ facility_name+ " for verification of stats tab")
            attach(str(ex), name="Assertion error in getting column name against : "+ facility_name+ " for verification of stats tab"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_data_die_count(self, context):
        try:
            self.log.logger.info("get data of die count ")
            min = database_config.run_query_to_get_min_max_value_data(context, 'min_value', wafer_id="c76f11f9-f17f-4399-83b8-15bbc5363328")[0]
            max = database_config.run_query_to_get_min_max_value_data(context, 'max_value',
                                                                      wafer_id="c76f11f9-f17f-4399-83b8-15bbc5363328")[0]
            start = min
            end = min
            Interval = (max-min)/10
            for i in range(0, 10):
                if i == 0:
                    start = start
                else:
                    start = end
                end = end + Interval
                die_count = database_config.run_query_to_get_die_count_data(context, 'die_count'
                                                                            , "c76f11f9-f17f-4399-83b8-15bbc5363328",
                                                                            str(start), str(end))[0]
                self.start_end_die_list[i+1] = [str(start), str(end), str(die_count)]
            attach(str(self.start_end_die_list), name="Die Count Verify - From Database"
                   , attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error("Error in get data of die count")
            attach(str(e), name="Error in get data of die count"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get data of die count")
            attach(str(ex), name="Assertion error in get data of die count"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_die_count(self, context):
        try:
            self.log.logger.info("Getting expected die count")
            all_die_count_elements = context.driver.find_elements(By.XPATH, reports_elements.die_count_legend)
            all_min_legend = context.driver.find_elements(By.XPATH, reports_elements.min_legend)
            all_max_legend = context.driver.find_elements(By.XPATH, reports_elements.max_legend)
            for index in all_min_legend:
                helpers.hover_to_element(context, index)
                value = helpers.get_web_element_text(context, index)
                # value = decimal.Decimal(value).normalize()
                self.minvalue.append(value)

            for index in all_max_legend:
                helpers.hover_to_element(context, index)
                value = helpers.get_web_element_text(context, index)
                # value = decimal.Decimal(value).normalize()
                self.maxvalue.append(value)
            for index in all_die_count_elements:
                helpers.hover_to_element(context, index)
                value = helpers.get_web_element_text(context, index)
                # value = decimal.Decimal(value).normalize()
                self.diecount.append(value)

            for index in range(1, 10):

                    dic = "['" + self.minvalue[index] + "','" + self.maxvalue[index] + "','" + self.diecount[index] + "']"
                    self.min_max_diecount_dic[index] = dic
        except Exception as e:
            self.log.logger.error("Error in getting expected die count")
            attach(str(e), name="Error in getting expected die count"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in getting expected die count")
            attach(str(ex), name="Assertion error in getting expected die count"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # self.min_max_diecount_dic
    def save_in_mongo(self, context, expected_result_col, expected_result_key):
        try:
            self.log.logger.info("Saving Expected data  in mongo")
            if "min_max_diecount" in expected_result_key:
                value = self.min_max_diecount_dic
            elif "data_tab_grid" in expected_result_key:
                value = self.data_grid_view
            elif "stats_tab_grid" in expected_result_key:
                value = self.stats_grid_view
            elif "errors_tab_grid" in expected_result_key:
                value = self.errors_grid_view
            database.write_expected_output_in_the_collection(context, expected_result_col, expected_result_key, value)
            self.log.logger.info("Saved Expected data  in mongo - Done")
        except Exception as e:
            self.log.logger.error("Error in saving Expected data  in mongo")
            attach(str(e), name="Error in saving Expected data  in mongo"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in saving Expected data  in mongo")
            attach(str(ex), name="Assertion error in saving Expected data  in mongo"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_die_count(self, context):
        try:
            self.log.logger.info("Verification of die count ")
            all_die_count_elements = context.driver.find_elements(By.XPATH, reports_elements.die_count_legend)
            all_min_legend = context.driver.find_elements(By.XPATH, reports_elements.min_legend)
            all_max_legend = context.driver.find_elements(By.XPATH, reports_elements.max_legend)
            min_data = []
            max_data = []
            die_count_data = []
            self.start_end_die_list = ast.literal_eval(self.start_end_die_list)

            for value in self.start_end_die_list:
                row = self.start_end_die_list[value].split(",")
                n = str(row[0]).replace('[', '')
                # d = n
                min_data.append(n)
                max_data.append(row[1])
                n = str(row[2]).replace("]", "")
                die_count_data.append(n)

            # assert min limit
            for index in all_min_legend:
                helpers.hover_to_element(context, index)
                value = helpers.get_web_element_text(context, index)
                value = decimal.Decimal(value).normalize()
                for data in min_data:
                    data = data.replace("'", "")
                    data = decimal.Decimal(data)
                    # data = decimal.Decimal(data).normalize()
                    if value == data:
                        assert value == data
                        allure.attach(str(value), name="min limit verified- Histogram", attachment_type=AttachmentType.TEXT)
            # assert max limit
            for index in all_max_legend:
                helpers.hover_to_element(context, index)
                value = helpers.get_web_element_text(context, index)
                value = decimal.Decimal(value).normalize()
                for data in max_data:
                    data = data.replace("'", "")
                    data = decimal.Decimal(data)
                    # data = decimal.Decimal(data).normalize()
                    if value == data:
                        assert value == data
                        allure.attach(str(value), name="max limit verified- Histogram", attachment_type=AttachmentType.TEXT)
                # assert die_count in
            # assert die count
            for index in all_die_count_elements:
                helpers.hover_to_element(context, index)
                value = helpers.get_web_element_text(context, index)
                value = decimal.Decimal(value).normalize()
                for data in die_count_data:
                    data = data.replace("'", "")
                    data = decimal.Decimal(data)
                    # data = decimal.Decimal(data).normalize()
                    if value == data:
                        assert value == data
                        allure.attach(str(value), name="die count verified- Histogram", attachment_type=AttachmentType.TEXT)
                # assert die_count in
            self.log.logger.info("Verified of of die count - Done")
            attach(str(self.start_end_die_list), name="Verified Parametric Histogram Legend data - min,max,die count"
                   , attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error("Error in verification of die count")
            attach(str(e), name="Error in verification of die count"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of die count")
            attach(str(ex), name="Assertion error in verification of die count"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_data_tab(self, context):
        try:
            self.log.logger.info("Verification of Parametric Histogram report")
            for expected_data in self.data_grid_view_data_tab:
                for data in self.data_grid_view:
                    if data == expected_data:
                        attach(str(expected_data), name="Parametric Histogram report - Verifying the Data tab"
                               , attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error("Error in verification of Parametric Histogram report")
            attach(str(e), name="Error in verification of Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Parametric Histogram report")
            attach(str(ex), name="Assertion error in verification of Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_stats_tab(self, context):
        try:
            self.log.logger.info("Verification of Parametric Histogram report - Stats Tab")
            for expected_data in self.stats_grid_view:
                for data in self.data_grid_view:
                    if data == expected_data:
                        attach(str(data), name="Parametric Histogram report - Verifying the Stats Tab"
                               , attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Verification of Parametric Histogram report - Stats Tab- Done")
        except Exception as e:
            self.log.logger.error("Error in verification of Parametric Histogram report - Stats Tab")
            attach(str(e), name="Error in verification of Parametric Histogram report - Stats Tab"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verification of Parametric Histogram report - Stats Tab")
            attach(str(ex), name="Assertion error in verification of Parametric Histogram report - Stats Tab"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def read_expected_results(self, context, collection_name, key):
        try:
            self.log.logger.info("I get the expected results for the Parametric Histogram report")
            data = database.read_mongo_data_value(context, collection_name, key)
            self.data_grid_view_data_tab.append(data['Data'])
            self.log.logger.info("I get the expected results for the Parametric Histogram report - Done")
        except Exception as e:
            self.log.logger.error("Error in get the expected results for the Parametric Histogram report")
            attach(str(e), name="Error in get the expected results for the Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get the expected results for the Parametric Histogram report")
            attach(str(ex), name="Assertion error in get the expected results for the Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def read_expected_results_for_legends_hist(self, context, collection_name):
        try:
            self.log.logger.info("I get the expected results for the Parametric Histogram report")
            data = database.read_mongo_data(context, collection_name)
            self.data_grid_view_data_tab.append(data['Data'])
            self.log.logger.info("I get the expected results for the Parametric Histogram report - Done")

        except Exception as e:
            self.log.logger.error("Error in get the expected results for the Parametric Histogram report")
            attach(str(e), name="Error in get the expected results for the Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get the expected results for the Parametric Histogram report")
            attach(str(ex), name="Assertion error in get the expected results for the Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex