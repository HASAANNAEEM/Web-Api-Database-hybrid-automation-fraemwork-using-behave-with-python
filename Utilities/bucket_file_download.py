import logging
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Utilities.log import Logger
from Utilities import yaml_reader
from Helpers.aws import AwsConfigurations

aws_config = AwsConfigurations()
log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))


# Download file from AWS with target file location#
def download_from_aws(context, target_file_location, source_location):
    data = yaml_reader.data_reader_from_test_data(context, "Converter")
    local_file_directory = data['local_file_directory']
    dot = "."
    target_bucket, target_file_name = extract_file_bucket_name(context, target_file_location)
    source_bucket, source_file_name = extract_file_bucket_name(context, source_location)
    try:
        # Creating directory and naming for downloading files
        if dot in str(source_file_name):
            source_string = str(source_file_name).split(dot)
            source_file_name = str(source_string[0])
            local_directory_with_file_name = local_file_directory+source_file_name+target_file_name

        bit = download_file(context, target_bucket, target_file_name, local_directory_with_file_name)
        log.logger.info("file Downloaded in Local Repository - Done")
        attach(str(bit), name="Status Verification - file Downloaded in Local Repository",
               attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.logger.error(str(e))
        assert False


# Download file from AWS s3 bucket #
def download_file(context, bucket, file_name, file_local_directory):
    s3 = aws_config.creating_aws_client(context)
    try:
        s3.download_file(bucket, file_name, file_local_directory)
        log.logger.info("Downloaded Successful")
        return True
    except Exception as e:
        log.logger.error(str(e))
        assert False


def extract_file_bucket_name(context, file_link):
    file_link_array = file_link.split("/")
    # Extracting the S3 Bucket name from file Link
    bucket = file_link_array[2]
    # Extracting the file name from file Link
    file_name = file_link_array[3]
    return bucket, file_name

