import logging
import os
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Utilities.log import Logger
from Utilities import api
from Utilities import json_reader
from Utilities import payload_modifications
from Utilities import upload_file_to_bucket
from Utilities import yaml_reader
from config.api_endpoints import ApiConfigurations
from config.constants import Constants
from datetime import datetime
from datetime import date

api_config = ApiConfigurations()


class ConverterClass:
    def __init__(self):
        self.log = Logger(logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                                                        level=logging.INFO,
                                                        datefmt='%Y-%m-%d %H:%M:%S'))

    """
    Post Login API Endpoint with login api url and their payload
    Read data from test database 
    Read data from yml file
    Post Request for login
    """

    #  Post Login API Endpoint with login api url and their payload  #
    def post_login_api(self, context, login_api, payload_path):
        try:
            self.log.logger.info(" Post Login API Endpoint with login api url and their payload ")
            data = yaml_reader.data_reader_from_test_data(context, login_api)
            payload = json_reader.json_data_reader(context, data[payload_path])
            platform = context.config.userdata['platform']
            payload = payload[platform]
            env = context.config.userdata['env']
            api_end_point = api_config.login_endpoint % env
            response = api.post_api_without_access_key(context, api_end_point, payload)
            Constants.response = response.status_code
            site_response = str(response.content)
            bearer_token = site_response.split("'")
            Constants.access_token = bearer_token[1]
            self.log.logger.info("Generated Token: " + Constants.access_token)
        except Exception as e:
            attach(str(e), name="Error in post Login API Endpoint with login api url and their payload"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            attach(str(ex), name="Assertion error in post Login API Endpoint with login api url and their payload"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    """
        Post the api end point
        Read data from test database 
        Read data from yml file
        Post Request With Access key
    """

    # Post the api end point #
    def post_policy_api_endpoint(self, context, payload_policy_name, payload_path):
        try:
            data = yaml_reader.data_reader_from_test_data(context, payload_policy_name)
            payload = json_reader.json_data_reader(context, data[payload_path])
            env = context.config.userdata['env']
            api_end_point = api_config.loader_endpoint % env
            response = api.post_api_with_access_key(context, Constants.access_token, api_end_point, payload)
            Constants.response = response.status_code
            self.log.logger.info("Post the api end point for " + payload_policy_name)
        except Exception as e:
            attach(str(e), name="Error in post the api end point for " + payload_policy_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            attach(str(ex), name="Assertion error in post the api end point for " + payload_policy_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Creating a bucket... #
    def create_bucket(self, context, bucket_name):
        try:
            self.log.logger.info("Creating a bucket...")
            data = yaml_reader.data_reader_from_test_data(context, bucket_name)
            upload_file_to_bucket.create_aws_bucket(context, data['bucket'])
            self.log.logger.info("Bucket created! " + data['bucket'])
        except Exception as e:
            attach(str(e), name="Error in creating a bucket"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            attach(str(ex), name="Assertion error in creating a bucket"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Creating a bucket for feature name #
    def create_bucket_with_feature_name(self, context):
        try:
            self.log.logger.info("Creating a bucket...")
            feature_name = context.feature.filename
            feature_name = feature_name.split(".")[0].split("/")[1]
            bucket_name = "yw-"+feature_name+"-1"
            data = yaml_reader.data_reader_from_test_data(context, bucket_name)
            upload_file_to_bucket.create_aws_bucket(context, data['bucket'])
            self.log.logger.info("Bucket created! " + data['bucket'])
        except Exception as e:
            attach(str(e), name="Error in creating a bucket"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            attach(str(ex), name="Assertion error in creating a bucket"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    """
    Uploading files into the bucket
    Upload the files into the bucket with bucket name  and their location 
    """

    # Uploading files into the bucket #
    def upload_files_to_bucket(self, context, policy_name, path_of_file, bucket_name):
        try:
            Constants.collection_file_location_data.clear()
            self.log.logger.info("Uploading files into the bucket")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            print(data)
            files_path = os.listdir(data[path_of_file])
            for file_name in files_path:
                file_path = data[path_of_file] + file_name
                self.log.logger.info(file_path)
                upload_file_to_bucket.upload_file_to_aws(context, file_path, bucket_name, file_name)
                source_file_loc = "s3://" + bucket_name + "/" + file_name
                self.log.logger.info("file '" + file_name + "' uploaded")
                Constants.collection_file_location_data.append(source_file_loc)
        except Exception as e:
            attach(str(e), name="Error in uploading files into the bucket"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            attach(str(ex), name="Assertion error in uploading files into the bucket"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    """
    Update The Payload Policy
    Update the current time, policy name and bucket name  in payload
    """

    # Update The Payload Policy #
    def updated_the_payload(self, context,  payload_path, payload_policy, new_policy_name, bucket_name):
        try:
            date_time = datetime.now()
            feature_name = context.feature.filename
            feature_name = feature_name.split(".")[0].split("/")[1]
            new_policy_name = new_policy_name + "for" + feature_name + " " + str(date_time)
            Constants.new_policy_name = new_policy_name
            attach(str(new_policy_name), name="Modify policy name",
                   attachment_type=AttachmentType.TEXT)
            payload_modifications.payload_update(context, payload_path, payload_policy, new_policy_name, bucket_name)
            attach(str(payload_policy), name="Update The Payload Policy",
                   attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Update The Payload Policy")
        except Exception as e:
            attach(str(e), name="Error in update The Payload Policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            attach(str(ex), name="Assertion error in update The Payload Policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    """
    Verify the status code
    """

    # Verify the status code #
    def verify_status_code(self, context, expected_status_code, policy_name):
        try:
            value = str(Constants.response)
            assert value == expected_status_code, "Expected Status code " + expected_status_code + " is not equal to " \
                                                  + value
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            attach(str(current_time), name="Starting time after getting response status : " + str(expected_status_code),
                   attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Starting time after getting response status : " + str(expected_status_code))
            attach(str(expected_status_code),
                   name="Expected Status code " + expected_status_code + " is equal to " + value,
                   attachment_type=AttachmentType.TEXT)
            self.log.logger.info("Expected Status code " + expected_status_code + " is equal to " + value)
        except Exception as e:
            attach(str(e),
                   name="Error in verify the expected Status code " + expected_status_code + " is equal to " + value
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            attach(str(ex),
                   name="Assertion error in verify the expected Status code " + expected_status_code + " is equal to " + value
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex
