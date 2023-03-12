from behave import *

from pages.parametric_histogram_page import ParametricHistogramPage

parametric_histogram = ParametricHistogramPage()


@Then('I verify parametric histogram report')
def create_bucket_on_aws_s3(context):
    parametric_histogram.verifying_graph(context)


# @Then('I click on {text}')
# def click_on_btn_from_graph(context, text):
#     parametric_histogram.click_on_btn_from_graph(context, text)


@Then('I click on Select and Close button')
def click_save_btn(context):
    parametric_histogram.click_select_and_close(context)


@Then('I click on Stats tab')
def click_stats_tab(context):
    parametric_histogram.click_stats_tab(context)


@Then('I click on data tab')
def click_data_tab(context):
    parametric_histogram.click_data_tab(context)


@Then('I get selected tables from grid chooser')
def get_lst_selected_tables(context):
    parametric_histogram.get_selected_tables_grid_chooser(context)


@Then('I Verify the tables data against Grid view')
def verify_the_grid_chooser_against_data_grid_tab(context):
    parametric_histogram.verify_grid_chooser_data_against_data_gridview(context)


@Then('I get the data from database across {facility_name}')
def get_the_data_from_database(context, facility_name):
    parametric_histogram.get_columns_data_for_verify_data_tab(context, facility_name)


@Then('I get the data from Data Grid View')
def get_data_from_data_grid_view_data_tab(context):
    parametric_histogram.get_data_from_data_grid_view(context)


@Then('I get the data from Errors Grid View')
def get_data_from_data_grid_view_data_tab(context):
    parametric_histogram.get_errors_grid_view(context)


@Then('I get the data from statistics grid')
def get_data_from_statistics_grid(context):
    parametric_histogram.get_data_from_statistics_grid_view(context)


@Then('I click on the grid column chooser')
def click_on_grid_col_chooser(context):
    parametric_histogram.verify_the_grid_column_chooser(context)


@Then('I verify the data grid views data against database data')
def verify_dat_tab(context):
    parametric_histogram.verify_data_tab(context)


@Then('I verify the Min, Max , Die Count')
def verify_die_count(context):
    parametric_histogram.verify_die_count(context)


@Then('Get the Expected result')
def verify_die_count(context):
    parametric_histogram.get_die_count(context)


@Then('Save in {expected_result_col} across {expected_result_key} test database')
def verify_die_count(context, expected_result_col, expected_result_key):
    parametric_histogram.save_in_mongo(context, expected_result_col, expected_result_key)


@Then('I get data from database to validate die count')
def verify_die_count(context):
    parametric_histogram.get_data_die_count(context)


@Then('I click on errors tab')
def click_errors_tab(context):
    parametric_histogram.click_errors_tab(context)


@Then('I click on {btn} from graph')
def click_on_btn(context, btn):
    parametric_histogram.click_on_btn_from_graph(context, btn)


@Then('I verify the graph elements y axis')
def create_bucket_on_aws_s3(context):
    parametric_histogram.verify_y_tick(context)


@Then('I verify the graph elements x axis')
def create_bucket_on_aws_s3(context):
    parametric_histogram.verify_x_tick(context)


@Then('I click on the legends button')
def click_legends(context):
    parametric_histogram.click_on_btn(context)


@Then('I select the Die count from legends')
def select_die_count(context):
    parametric_histogram.select_die_count_from_legend(context)


@Then('I verify the legends')
def verify_legends(context):
    parametric_histogram.verifying_legends(context)


@Then('I verify the selection criteria window in displayed')
def screen_visible_selection_criteria(context):
    parametric_histogram.verify_selection_criteria(context)


@Then('I verify the data tab')
def verify_data_grid_view(context):
    parametric_histogram.verifying_data_grid_view(context)


@Then('I verify the stats tab')
def verify_stats(context):
    parametric_histogram.verify_stats_grid(context)


@Then('I verify the errors tab')
def verify_stats(context):
    parametric_histogram.verify_errors_grid_view(context)


@Then('I get the {collection_name} expected output data from test automation database')
def read_value_from_test_db(context, collection_name):
    parametric_histogram.read_expected_results_for_legends_hist(context, collection_name)


@Then('I get the {expected_result_col} across {expected_result_key} from test automation database')
def read_value_from_test_db(context, expected_result_col, expected_result_key):
    parametric_histogram.read_expected_results(context, expected_result_col, expected_result_key)

