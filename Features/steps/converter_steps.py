from behave import *
from pages.converter import ConverterClass
from pages.comparison import FileComparison
import logging
from Utilities.log import Logger

converter_page = ConverterClass()
file_comparison = FileComparison()
log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))


@given('Create a bucket on AWS S3 {bucket_name}')
def create_bucket_on_aws_s3(context, bucket_name):
    converter_page.create_bucket(context, bucket_name)


@given('I create a bucket on AWS S3')
def create_bucket_on_aws_s3(context, bucket_name):
    converter_page.create_bucket(context, bucket_name)

@given('I upload the {policy_name} files from {input_golden_file} into {input_golden_file_bucket_name} AWS S3 bucket')
def upload_the_files_into_the_bucket(context, policy_name, input_golden_file, input_golden_file_bucket_name):
    converter_page.upload_files_to_bucket(context, policy_name, input_golden_file, input_golden_file_bucket_name)


@when('I login to application using {api} api with {payload_path}')
def calling_login_API(context, api, payload_path):
    converter_page.post_login_api(context, api, payload_path)


@then('I create policy for {policy_name} stage and add {payload_path}')
def create_policy_and_add_stage(context, policy_name, payload_path):
    converter_page.post_policy_api_endpoint(context, policy_name, payload_path)


@then('I compare both {golden_file_path} files and {downloaded_file_path} file for {policy_name} from '
      '{input_golden_file_collection_name} and store value into {identical_file_path} and {different_lines_file_path} '
      'local directory path')
def compare_golden_file_against_newly_generated_file(context, golden_file_path, downloaded_file_path, policy_name
                                                     , input_golden_file_collection_name
                                                     , identical_file_path, different_lines_file_path):
    file_comparison.comparing_newly_generated_file_against_golden_file(context, policy_name, input_golden_file_collection_name,
                                                                       golden_file_path, downloaded_file_path,
                                                                       identical_file_path, different_lines_file_path)


@then('I update the {payload_path} for {policy_name} with {new_policy_name} and {bucket_name} bucket')
def updating_the_payload_with_policy_name(context, payload_path, policy_name, new_policy_name, bucket_name):
    converter_page.updated_the_payload(context, payload_path, policy_name, new_policy_name, bucket_name)


@then('I verify the response status code {status_code} for {policy}')
def verify_status_code(context, status_code, policy):
    converter_page.verify_status_code(context, status_code, policy)
