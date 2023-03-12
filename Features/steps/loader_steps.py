from behave import *
from pages.converter import ConverterClass
from pages.loader import LoaderClass

converter_page = ConverterClass()
loader_page = LoaderClass()


@given('I mark the {without_marked_file_path} for {tag_name} tag in {policy_name} for verification the change and '
       'store into {mark_file_path}')
def mark_identity_on_file_to_be_loaded(context, without_marked_file_path, tag_name, policy_name, mark_file_path):
    loader_page.mark_identity(context, policy_name, without_marked_file_path, tag_name, mark_file_path)


@then('I save the marked data into {marked_collection}')
def save_the_marked_file_into_test_db(context, marked_collection):
    loader_page.save_the_marked_data_into_test_db(context, marked_collection)


@then('I get the ptr data from {mark_file_path} for {policy_name}')
def get_data_from_marked_file(context, mark_file_path, policy_name):
    loader_page.get_ptr_data_from_marked_file(context, mark_file_path, policy_name)


@then('I get the data from Yield-werx database table for {policy_name} from {file_path}')
def get_data_from_db(context, policy_name, file_path):
    loader_page.get_all_the_data_from_yield_werx_db(context, policy_name, file_path)


@then('I verify the {mark_file_path} file of {policy_name} from test parameter Yield-werx database table')
def verify_test_parameter_from_db(context, policy_name, mark_file_path):
    loader_page.verification_of_the_test_parameter_table_after_marking(context, policy_name, mark_file_path)


@then('I verify the dynamic table from test parameter Yield-werx database table')
def verify_dynamic_table(context):
    loader_page.verification_of_the_dynamic_table_data_after_marking(context)


@then('I attach the result into the allure report')
def attach_report(context):
    loader_page.attach_result_into_the_allure_report(context)


@then('I get the {tag_name} data from {mark_file_path} for {policy_name}')
def get_data_from_tag(context, tag_name, mark_file_path, policy_name):
    loader_page.get_data_from_file(context, tag_name, policy_name, mark_file_path)


@then('I verify the test summary table data from yield-werx database')
def verify_test_summary_table_step(context):
    loader_page.verify_test_summary_table(context)


@then('I verify the bin summary table data from yield-werx database')
def verify_bin_summary_table_step(context):
    loader_page.verify_bin_summary_table(context)


@then('I generate the {generated_bin} bin data from {file_directory} file for {policy_name}')
def verify_bin_summary_table_step(context, generated_bin, policy_name, file_directory):
    loader_page.generate_the_bin_summary_record(context, generated_bin, policy_name, file_directory)


@then('I generate the test data from {file_directory} file for {policy_name}')
def verify_bin_summary_table_step(context, policy_name, file_directory):
    loader_page.generate_the_test_summary_record(context, policy_name, file_directory)


@then('I update the {payload} for {policy_name}')
def updating_selection_criteria_payload_step(context, payload, policy_name):
    loader_page.updated_the_payload_for_selection_criteria(context, payload, policy_name)


@then('I calling the {selection_criteria} api with {payload} and getting the execution time')
def updating_selection_criteria_payload_step(context, selection_criteria, payload):
    loader_page.calculate_execution_time_for_selection_criteria(context, payload, selection_criteria)


@then('I update the {policy_name} {payload_path} with {new_policy_name}, {checkbox} and {bucket_name} bucket')
def updating_the_payload_with_different_checkbox(context, payload_path, policy_name, new_policy_name, checkbox,
                                                 bucket_name):
    loader_page.updated_the_payload_for_checkbox(context, payload_path, policy_name, new_policy_name, checkbox,
                                                 bucket_name)


@then('I verify the {bin_summary} bin summary table data from yield-werx database')
def verify_bin_summary_table_data_step(context, bin_summary):
    loader_page.verify_bin_summary_table_for_read_and_generated_checkbox(context, bin_summary)
