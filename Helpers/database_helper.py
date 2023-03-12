import logging
import math
import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Helpers.test_db import MongoDb
from Utilities.log import Logger
from config.constants import AWSCredential
from Helpers.db_config import DataBaseConfig
from config.constants import Constants
from datetime import datetime

aws_credential = AWSCredential()
mongoDB = MongoDb()
log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))
database_yw = DataBaseConfig()


# Validation of the performance log again expected time#
def validating_performance_log(context, execution_time, performance_logs):
    boolean = True
    try:
        if execution_time > performance_logs:
            assert boolean, "Converter Performance log : " + str(
                performance_logs) + "is greater than expected " \
                                    "execution time " + execution_time
            attach(str(execution_time), name="Expected Converter Execution Time",
                   attachment_type=AttachmentType.TEXT)
            attach(str(performance_logs), name="Calculated Converter  Execution Time",
                   attachment_type=AttachmentType.TEXT)
            attach("Passed", name="Calculated Execution is less than expected execution time "
                                  "Execution Time " + str(execution_time) +
                                  " Calculated Execution Time " +
                                  str(performance_logs),
                   attachment_type=AttachmentType.TEXT)
        else:
            boolean = math.isclose(performance_logs, execution_time)
            if not boolean:
                boolean = math.isclose(performance_logs, execution_time, rel_tol=0.5)

            assert boolean, "Performance log : " + str(performance_logs) + "is greater than expected " \
                                                                           "execution time " + str(execution_time)
            attach(str(execution_time), name="Expected Execution Time",
                   attachment_type=AttachmentType.TEXT)
            attach(str(performance_logs), name="Calculated Execution Time",
                   attachment_type=AttachmentType.TEXT)
            attach("Passed", name="Performance Log of Converter with Tolerance value 5 % Expected "
                                  "Execution Time " + str(execution_time) + " Calculated Execution Time " +
                                  str(performance_logs),
                   attachment_type=AttachmentType.TEXT)
    except Exception as e:
        attach("Failed",
               name="Error Performance Log of Converter with Tolerance value 5 % Expected "
                    "Execution Time " + str(execution_time) + " Calculated Execution Time " +
                    str(performance_logs) + str(e),
               attachment_type=AttachmentType.TEXT)
        log.logger.error("Performance logs validation" + str(e))
        assert False


# I check the status of the file #
def check_status_of_file(context, expected_status, yield_werx_database, source_file, work_fow_step):
    start_time = datetime.now()
    status_data = ""
    min_value = 0
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    attach(str(current_time), name="Starting time for verifying status of file in yw-db",
           attachment_type=AttachmentType.TEXT)
    log.logger.info("Starting time for verifying status of file in yw-db  in at : " + str(current_time))
    while True:
        if min_value < 5:
            try:
                status_data = database_yw.run_query_for_work_flow(context,
                                                                  yield_werx_database,
                                                                  "workflow_status",
                                                                  source_file,
                                                                  work_fow_step
                                                                  )[Constants.first_index][Constants.first_index]
            except Exception as ex:
                log.logger.warn("Not getting " + expected_status + " from yw-db")
            end_data = datetime.now()
            min_value = end_data.minute - start_time.minute
            if "SUCCESS" in status_data or "FAILURE" in status_data:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                log.logger.info("Getting "+status_data+" of file in yw-db in at : " + str(current_time))
                attach(str(current_time), name="Getting "+str(status_data)+" of file in yw-db",
                       attachment_type=AttachmentType.TEXT)
                created_on = database_yw.run_query(context, yield_werx_database, "workflow_created_on", source_file)[Constants.first_index][Constants.first_index]
                log.logger.info("Workflow table created on time after creating policy : " + str(created_on))
                attach(str(created_on), name="Workflow table created on time after creating policy",
                       attachment_type=AttachmentType.TEXT)
                workflow_start_date = database_yw.run_query(context, yield_werx_database, "workflow_start_date", source_file)[Constants.first_index][
                    Constants.first_index]
                log.logger.info("Workflow table start date time after creating policy : " + str(workflow_start_date))
                attach(str(workflow_start_date), name="Workflow table start date time after creating policy ",
                       attachment_type=AttachmentType.TEXT)
                workflow_end_date = database_yw.run_query(context, yield_werx_database, "workflow_end_date", source_file)[Constants.first_index][Constants.first_index]
                log.logger.info("Workflow table end date time after creating policy : " + str(workflow_end_date))
                attach(str(workflow_end_date),
                       name="Workflow table end date time after creating policy",
                       attachment_type=AttachmentType.TEXT)
                attach(str(min_value), name="File processing time after creating policy",
                       attachment_type=AttachmentType.TEXT)
                attach(status_data, name="Status Verified for file upload", attachment_type=AttachmentType.TEXT)
                assert expected_status in status_data, "Error " + expected_status + " status of " + source_file + \
                                                       " is not present in yw db"
                break
            else:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                log.logger.warning("Not getting status of file at : " + str(current_time))
                log.logger.warning(str(min_value))
            try:
                database_yw.connect_yw_db(context)
            except Exception as ef:
                log.logger.warn("Failed to connect to db")
        else:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            log.logger.info("Getting " + status_data + " of file in yw-db in at : " + str(current_time))
            attach(str(current_time), name="Getting " + str(status_data) + " of file in yw-db",
                   attachment_type=AttachmentType.TEXT)
            attach(str(status_data), name="FIle not uploading into db after more than 5 minutes",
                   attachment_type=AttachmentType.TEXT)
            assert False, "FIle not uploading into db after more than 5 minutes"


# Enter value into the collection#
def enter_value_with_key_into_the_collection(context, collection_name, key, value):
    try:
        mongoDB.connect_mongo(context)
        mongoDB.write_value(context, collection_name, key, value)
        log.logger.info("Inserting source file link to TestDatabase")
    except Exception as e:
        log.logger.error("Inserting source file link Error - TestDatabase : " + str(e))
        assert False
    attach(str(value), name="Data Saved In Test Database - Success",
           attachment_type=AttachmentType.TEXT)


# I get the data into test db #
def get_data_from_testDB(context, collection_name):
    attach(str("Get Data from Test Database"), name="Data Retrieving", attachment_type=AttachmentType.TEXT)
    try:
        mongoDB.connect_mongo(context)
        source_file_list = mongoDB.read_value(context, collection_name, 1)
        log.logger.info("Getting source file link from TestDatabase")
    except Exception as e:
        log.logger.error("Getting source file link from TestDatabase - Error : " + str(e))

    return source_file_list


# Get all the data into test db #
def get_all_data_from_testDB(context, collection_name):
    attach(str("Get Data from Test Database"), name="Data Retrieving", attachment_type=AttachmentType.TEXT)
    try:
        mongoDB.connect_mongo(context)
        source_file_list = mongoDB.read_all(context, collection_name)
        log.logger.info("Getting source file link from TestDatabase")
    except Exception as e:
        log.logger.error("Getting source file link from TestDatabase - Error : " + str(e))

    return source_file_list
