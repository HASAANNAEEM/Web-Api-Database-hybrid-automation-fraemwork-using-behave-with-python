import logging
from Utilities import replacing_the_list
from Utilities.log import Logger
from Helpers.test_db import MongoDb
from Helpers import comparison
from allure_commons.types import AttachmentType
from allure_commons._allure import attach

obj_mongoDb = MongoDb()


class FileComparison:
    def __init__(self):
        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    """
    Newly generated file against golden file comparison
    Compare file for converter and create a new identical and difference file
    Getting golden file across newly generated atdf file
    Create identical and difference file
    Compare the file line by line 
    Removing trailing zeros
    Compare the flag for index 8 and 4 
    """

    # Newly generated file against golden file comparison #
    def comparing_newly_generated_file_against_golden_file(self, context, policy_name, input_golden_file_collection_name
                                                           , golden_file_path, downloaded_file_path
                                                           , identical_file_path
                                                           , different_lines_file_path):
        try:
            self.log.logger.info("Compare newly generated file with golden file ")
            obj_mongoDb.connect_mongo(context)
            input_golden_file_list = obj_mongoDb.read_value(context, input_golden_file_collection_name, 1)['Data']
            input_golden_file_list = replacing_the_list.replacing_the_list(context, input_golden_file_list)
            for key in input_golden_file_list:
                if "s3://" in str(key):
                    source_bucket, source_file_name = comparison.extract_file_bucket_name(context, key)
                    comparison.compare_files(context, policy_name, source_file_name, golden_file_path, downloaded_file_path,
                                             identical_file_path, different_lines_file_path)
                    self.log.logger.info("file Comparison - Done")
                else:
                    self.log.logger.info("file comparison - file name not right :" + key)

        except Exception as e:
            self.log.logger.error("Error in compare newly generated file with golden file ")
            attach(str(e), name="Error in compare newly generated file with golden file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in compare newly generated file with golden file")
            attach(str(ex), name="Assertion error in compare newly generated file with golden file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex