from behave import *
from Hooks.delete_s3_bucket import DeleteFilesFromS3Buckets
from Helpers.db_config import DataBaseConfig
from pages.database import DatabaseManagement

database_yw = DatabaseManagement()
delete_bucket = DeleteFilesFromS3Buckets()
database_config = DataBaseConfig()


@given('I delete files from AWS S3 bucket')
def delete_bucket_on_aws_s3(context):
    delete_bucket.delete_file_from_bucket(context)


@given('I delete files from AWS S3 bucket with name')
def delete_bucket_on_aws_s3_with_feature_name(context):
    delete_bucket.delete_file_from_bucket_with_feature_name(context)


@then('I verify the {expected_status} status of policy in database from {collection_name}')
def verify_status_of_policy(context, expected_status, collection_name):
    database_yw.verify_the_status_of_file(context, expected_status, collection_name)


@then('I verify policy data is created in yield-werx-db')
def get_work_flow_step(context):
    database_yw.get_work_flow_instance(context)


@then('I get the data {target_file_table} , {start_date_table} and {end_date_table} from '
      '{input_golden_file_collection_name} with {query_data_source} for {policy_name} policy validation of Calculated '
      'Performance log with {expected_performance_log}')
def verify_performance_log_step(context, target_file_table, start_date_table, end_date_table,
                                input_golden_file_collection_name,
                                query_data_source, policy_name, expected_performance_log):
    database_yw.verify_performance_log(context, target_file_table, start_date_table, end_date_table,
                                       input_golden_file_collection_name, query_data_source, policy_name,
                                       expected_performance_log)


@then('I get the Source file list from test database {download_file_collection} then download converted file from Aws '
      's3')
def download_converter_file(context, download_file_collection):
    database_yw.download_file_from_aws(context, download_file_collection)


@then('I store the values into source file location {collection_name}')
def store_the_value_into_test(context, collection_name):
    database_yw.store_the_data_into_test_database(context, collection_name)


@then('I connect to YW database')
def connect_to_yw_database(context):
    database_config.connect_yw_db(context)


@then('I close to YW database')
def connect_to_yw_database(context):
    database_config.close_yw_connection(context)


@then('I get the meta data')
def get_meta_data(context):
    database_yw.get_meta_data(context)


@then('I connect to test database')
def connect_to_test_db(context):
    database_yw.connect_to_test_database(context)


@then('I delete the data from {collection_name} collection')
def connect_to_test_db(context, collection_name):
    database_yw.delete_the_collection_data_from_test_database(context, collection_name)


@then('I write the data into {collection_name} collection')
def write_value_into_test_db(context, collection_name):
    database_yw.write_value_in_the_collection(context, collection_name)


