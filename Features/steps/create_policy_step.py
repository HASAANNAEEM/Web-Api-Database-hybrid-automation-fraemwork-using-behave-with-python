from behave import *

from pages.createpolicy import PoliciesPage

load_policy_Page = PoliciesPage()


@Then('I click on {text} from menu')
def click_on_option_from_menu(context, text):
    load_policy_Page.click_on_option(context, text)


@Then('I verify the create policy button is displayed')
def verify_create_policy_button_is_displayed(context):
    load_policy_Page.verify_create_policy_button(context)


@Then('I click on the create policy button')
def click_on_create_policy_button(context):
    load_policy_Page.click_on_create_policy_btn(context)


@Then('I enter policy name {text}')
def enter_policy_name_in_field(context, text):
    load_policy_Page.enter_policy_name(context, text)


@Then('I enter policy version {text}')
def enter_policy_version_in_field(context, text):
    load_policy_Page.enter_policy_version(context, text)


@Then('I enter policy description {text}')
def enter_policy_desc_in_field(context, text):
    load_policy_Page.enter_policy_desc(context, text)


# Enter owner input field
@Then('I enter policy owner email {text}')
def enter_policy_owner_input_field(context, text):
    load_policy_Page.enter_policy_owner_email(context, text)


@Then('I click on Add stage button')
def click_on_add_stage_button(context):
    load_policy_Page.click_add_stage_btn(context)


@Then('I select {text} stage')
def click_on_add_stage_button(context, text):
    load_policy_Page.select_stage(context, text)


@Then('I click on View button')
def click_on_view_button(context):
    load_policy_Page.click_view_button(context)


@then('I select source format as {text}')
def select_source_format_converter(context, text):
    load_policy_Page.select_source(context, text)


@then('I select source as {text}')
def select_source_cloud_storage(context, text):
    load_policy_Page.source_cloud(context, text)


@then('I enter source container {text}')
def enter_source_container(context, text):
    load_policy_Page.enter_source_container(context, text)


@then('I enter source ftp address {text}')
def enter_source_ftp_address(context, text):
    load_policy_Page.enter_source_ftp_address(context, text)


@then('I select policy step {policy_step}')
def select_policy_step(context, policy_step):
    load_policy_Page.select_policy_step(context, policy_step)


@then('I enter source ftp username {text}')
def enter_source_ftp_username(context, text):
    load_policy_Page.enter_data_ftp_username(context, text)


@then('I enter source ftp password {text}')
def enter_source_ftp_password(context, text):
    load_policy_Page.enter_data_ftp_password(context, text)


@then('I enter source folder to transfer files from {text}')
def enter_source_folder_to_transfer_files_from(context, text):
    load_policy_Page.enter_data_folder_to_transfer_files_from(context, text)


@then('I select schedule mode as {text}')
def select_schedule_mode(context, text):
    load_policy_Page.select_schedule_mode(context, text)


@then('I select schedule mode as')
def select_start_time(context):
    load_policy_Page.select_time(context)


@then('I enter policy polling time {text}')
def enter_policy_polling_time(context, text):
    load_policy_Page.enter_polling_time(context, text)


@then('I click on Save button')
def click_on_save_button(context):
    load_policy_Page.hit_save_btn(context)


@then('I verify the {message} alert message')
def verify_the_alert_message(context, message):
    load_policy_Page.verify_alert_message_from_screen(context, message)


# @then('I click on {text}')
# def click_on_data_intake_queue(context, text):
#     load_policy_Page.click_on_data_intake(context, text)


@then('I verify the {text} is successfully executed')
def verify_policy_status(context, text):
    load_policy_Page.verify_policy(context, text)


@then('I verify the {expected_status} status from step intake queue')
def verify_policy_status_from_step_intake_queue(context, expected_status):
    load_policy_Page.verify_policy_from_step_intake_view(context, expected_status)


@then('I download the converted files form s3')
def download_the_converted_file_From_s3(context):
    load_policy_Page.download_converted_file(context)


@then('I check the {text} option in die')
def check_the_die_records(context, text):
    load_policy_Page.check_die_records(context, text)


@then('I check all summary records')
def select_location_type(context):
    load_policy_Page.check_summary_records(context)


@then('I check the checkbox for {check_box_text} for summary records')
def check_specific_summary_record(context, check_box_text):
    load_policy_Page.check_summary_records_for_specific_checkbox(context, check_box_text)


@Then('I check the selection criteria for {table_name}')
def select_selection_criteria(context, table_name):
    load_policy_Page.select_selection_criteria_for_table(context, table_name)


@Then('I select the data from selection criteria for rpt {table_name}')
def select_selection_criteria_rpt(context, table_name):
    load_policy_Page.select_selection_criteria_for_report(context, table_name)


@Then('I get the {table_name}'
      ' names of column against {policy_name} policy from {file_path} from data base')
def get_name_of_columns(context, table_name, policy_name, file_path):
    load_policy_Page.get_name_of_table_column(context, table_name, policy_name, file_path)


@Then('I verify the {table_data} table data from data base')
def verify_the_table_data(context, table_data):
    load_policy_Page.verify_the_data_selection_criteria_for_table(context, table_data)


@Then('I select selection criteria button')
def clicking_on_selection_criteria_button(context):
    load_policy_Page.click_selection_criteria(context)


@Then('I select the {table_name} from selection criteria')
def select_selection_criteria(context, table_name):
    load_policy_Page.select_selection_criteria_for_table(context, table_name)


@Then('I select the starting time')
def select_start_time(context):
    load_policy_Page.select_time(context)