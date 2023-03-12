from datetime import datetime
from datetime import timezone
import json
import logging
import time
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Helpers.db_config import DataBaseConfig
from Helpers.test_db import MongoDb
from Utilities import performance_log_calculation
from Utilities.log import Logger
from Utilities import bucket_file_download
from config.constants import Constants
from config.constants import YieldWerxDataBase
from Utilities import database
from Utilities import yaml_reader
from Utilities import replacing_the_list
from Helpers import database_helper
from config.constants import RollBackTransaction
from config.constants import PolicyVerification

mongoDb = MongoDb()
database_yw = DataBaseConfig()
database_utilities = database

log = Logger(logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'))


class DatabaseManagement:
    log = Logger(logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'))
    work_fow_step = []
    """
    Verify the expected status of the file
    I get the data into test db
    I check the status of the file
    """

    # Verify the expected status of the file #
    def verify_the_status_of_file(self, context, expected_status, collection_name):
        try:
            self.log.logger.info("Verify the " + expected_status + " status of the file")
            source_file_location_lst = database_helper.get_data_from_testDB(context, collection_name)
            data_list_source_file = source_file_location_lst['Data']
            list_source_file = data_list_source_file.split(",")
            for source_file in list_source_file:
                for work_fow_step in self.work_fow_step:
                    data_source_file = source_file.replace("[", "").replace("'", "").replace("]", "")
                    source_file = data_source_file.split(",")
                    source_file = source_file[0]
                    source_file = source_file.replace("[", "").replace("'", "").replace(" ", "")
                    Constants.source_files_list.append(source_file)
                    self.log.logger.info(source_file)
                    database_helper.check_status_of_file(context, expected_status,
                                                         YieldWerxDataBase.yield_werx_database,
                                                         source_file, work_fow_step)
        except Exception as e:
            self.log.logger.error("Error in verifying the " + expected_status + " status of the file")
            attach(str(e), name="Error in verifying the " + expected_status + " status of the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verifying the " + expected_status + " status of the file")
            attach(str(ex), name="Assertion error in verifying the " + expected_status + " status of the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Verification of policy from policy, work step and work instance table #

    def get_work_flow_instance(self, context):
        self.log.logger.info("policy_name : " + Constants.new_policy_name)
        policy_ids = database.get_policy_ids(context, Constants.new_policy_name)
        self.log.logger.info("Policy id : " + str(policy_ids))
        attach(str(policy_ids), name="policy id's"
               , attachment_type=AttachmentType.TEXT)
        for policy_id in policy_ids:
            policy_id = policy_id[0]

            self.log.logger.info("Policy id : " + policy_id)
            attach(str(policy_id), name="policy id"
                   , attachment_type=AttachmentType.TEXT)
            try:
                policy_step_id = database.get_policy_step_id(context, policy_id)
                self.log.logger.info("Policy step id : " + policy_step_id)
                attach(str(policy_step_id), name="policy step id"
                       , attachment_type=AttachmentType.TEXT)
                task_scheduling_time = database_yw.run_query_to_get_specific_data_without_user_id(context,
                                                                                                  PolicyVerification.column_value,
                                                                                                  PolicyVerification.start_at,
                                                                                                  PolicyVerification.task_schedule,
                                                                                                  PolicyVerification.info_id,
                                                                                                  policy_id)[0]
                while True:
                    now_time = datetime.now(timezone.utc)
                    boolean = str(now_time.hour) + ":" + str(now_time.minute) + ":" + str(now_time.second) >= str(
                        task_scheduling_time.hour) + ":" + str(task_scheduling_time.minute) + ":" + str(
                        task_scheduling_time.second)
                    if boolean:
                        self.log.logger.info("Validate start at from task_scheduling " + str(task_scheduling_time))
                        attach(str(task_scheduling_time), name="Start at time from task_scheduling"
                               , attachment_type=AttachmentType.TEXT)
                        break
                start_time = datetime.now(timezone.utc)
                while True:
                    end_time = datetime.now(timezone.utc)
                    if end_time.minute - start_time.minute <= 1:
                        try:
                            database_yw.connect_yw_db(context)
                            self.work_fow_step = []
                            work_fow_step = database.get_work_flow_step_id(context, policy_step_id)[0][0]
                            self.work_fow_step.append(work_fow_step)
                            Constants.workflow_step = self.work_fow_step
                            self.log.logger.info("work flow step " + work_fow_step)
                            attach(str(work_fow_step), name="Workflow step id"
                                   , attachment_type=AttachmentType.TEXT)
                            database_yw.connect_yw_db(context)
                            work_flow_instance_ids = database_yw.run_query_to_get_id_without_created_by_id(
                                context, RollBackTransaction.workflow_instance
                                , RollBackTransaction.policy_id, policy_id)[0][0]
                            self.log.logger.info("work flow instance ids " + work_flow_instance_ids)
                            attach(str(work_flow_instance_ids), name="Workflow instance id"
                                   , attachment_type=AttachmentType.TEXT)
                            break
                        except Exception as e:
                            self.log.logger.warn("Not getting work flow step table data against policy step id : "
                                                 + str(policy_step_id))
                    else:
                        now_time = datetime.now(timezone.utc)
                        attach(str(now_time), name="Current time"
                               , attachment_type=AttachmentType.TEXT)
                        assert False, e

                # count = 0
                # while True:
                #     try:
                #         database_yw.connect_yw_db(context)
                #         work_fow_step = database.get_work_flow_step_id(context, policy_step_id)[0][0]
                #         self.work_fow_step.append(work_fow_step)
                #         self.log.logger.info("work flow step " + work_fow_step)
                #         attach(str(work_fow_step), name="Workflow step id"
                #                , attachment_type=AttachmentType.TEXT)
                #         database_yw.connect_yw_db(context)
                #         work_flow_instance_ids = database_yw.run_query_to_get_id_without_created_by_id(
                #             context, RollBackTransaction.workflow_instance
                #             , RollBackTransaction.policy_id, policy_id)[0][0]
                #         self.log.logger.info("work flow instance ids " + work_flow_instance_ids)
                #         attach(str(work_flow_instance_ids), name="Workflow instance id"
                #                , attachment_type=AttachmentType.TEXT)
                #         break
                #     except Exception as e:
                #         count += 1
                #         if count > 5:
                #             now_time = datetime.now(timezone.utc)
                #             attach(str(now_time), name="Current time"
                #                    , attachment_type=AttachmentType.TEXT)
                #             assert False, e

            except Exception as e:
                self.log.logger.warn(
                    "Error in verification of policy from policy, work step and work instance table : " + str(e))
                assert False, "Error in verification of policy from policy, work step and work instance table : " + str(
                    e)

    """
    Verify the Performance log of the file
    Read data from test database
    Read the data value from test database with collection name and key
    """

    # Verify the Performance log of the file #
    def verify_performance_log(self, context, target_file_table, start_date_table, end_date_table,
                               input_golden_file_collection_name, query_data_source, policy_name,
                               expected_performance_log):
        try:
            self.log.logger.info("Verify the Performance log of the file")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            mongoDb.connect_mongo(context)
            source_file_list = mongoDb.read_value(context, input_golden_file_collection_name, 1)['Data']
            source_file_list = source_file_list.split(",")
            for source_file in source_file_list:
                source_file_url = source_file.replace("[", "").replace("'", "").replace("]", "")
                source_file_url = source_file_url.split(",")
                source_file_url = source_file_url[0]
                source_file_url = source_file_url.replace("[", "").replace("'", "").replace(" ", "")
                # Target file Location Query
                target_file_location = database_yw.run_query(context, query_data_source, target_file_table,
                                                             source_file_url)
                # Start Date Query
                start_date = database_yw.run_query(context, query_data_source, start_date_table, source_file_url)
                # END Date Query
                end_date = database_yw.run_query(context, query_data_source, end_date_table, source_file_url)

                performance_logs = performance_log_calculation.performance_calc(context, start_date, end_date)

                with open(data[expected_performance_log]) as json_data:
                    execution_time_data = json.load(json_data)
                for key in execution_time_data:
                    source_file_name = source_file.split("//")[1].split("/")[1]
                    key_value = key.split(".")[0]
                    if "_" in key_value:
                        key_value = key_value.split("_")[0]
                    if key_value in source_file_name:
                        self.log.logger.info(source_file_name)
                        execution_time = execution_time_data[key]
                        break

                database_helper.validating_performance_log(context, execution_time, performance_logs)
                Constants.values.append([target_file_location, start_date, end_date, performance_logs])
        except Exception as e:
            self.log.logger.error("Error in verify the Performance log of the file")
            attach(str(e), name="Error in verify the Performance log of the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verify the Performance log of the file")
            attach(str(ex), name="Assertion error in verify the Performance log of the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Store the data into test db #
    def store_the_data_into_test_database(self, context, collection_name):
        try:
            self.log.logger.info("Store the data into test db against collection_name : " + collection_name)
            for index in range(len(Constants.source_files_list)):
                source_file = Constants.source_files_list[index]
                Value = Constants.values[index]
                mongoDb.connect_mongo(context)
                mongoDb.write_value(context, collection_name, source_file, Value)
        except Exception as e:
            self.log.logger.error("Error in store the data into test db against collection_name : " + collection_name)
            attach(str(e), name="Error in store the data into test db against collection_name : " + collection_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in store the data into test db against collection_name : " + collection_name)
            attach(str(ex),
                   name="Assertion error in store the data into test db against collection_name : " + collection_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Download the file from aws #
    def download_file_from_aws(self, context, download_file_collection):
        try:
            self.log.logger.info(
                "Downloading file from AWS S3 Bucket against download_file_collection : " + download_file_collection)
            comma = ","
            mongoDb.connect_mongo(context)
            for key in Constants.source_files_list:
                source_file_list = mongoDb.read_value(context, download_file_collection, key)['Data']
                source_file_list = replacing_the_list.replacing_the_list(context, source_file_list)
                if comma in source_file_list:
                    source_file_list = source_file_list.split(",")
                else:
                    self.log.logger.warn("Contain one file to download")
                for source_file in source_file_list:
                    data = source_file.replace("[", "").replace("'", "").replace("]", "")
                    source_file = data.split(",")
                    source_file = source_file[0]
                    target_link = source_file.replace("[", "").replace("'", "").replace(" ", "").replace("((", "")
                    self.log.logger.info("Target link : " + target_link)
                    if "s3://" in str(target_link):
                        bucket_file_download.download_from_aws(context, target_link, key)
                        self.log.logger.info("Downloaded file from AWS S3 Bucket")
        except Exception as e:
            self.log.logger.error(
                "Error in downloading file from AWS S3 Bucket against download_file_collection : " + download_file_collection)
            attach(str(e),
                   name="Error in downloading file from AWS S3 Bucket against download_file_collection : " + download_file_collection
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in downloading file from AWS S3 Bucket against download_file_collection : " + download_file_collection)
            attach(str(ex),
                   name="Assertion error in downloading file from AWS S3 Bucket against download_file_collection : " + download_file_collection
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Get Loader Test Data #
    def get_loader_data_testDB(self, context):
        try:
            self.log.logger.info("Getting source file link from TestDatabase for loader")
            mongoDb.connect_mongo(context)
            source_file_list = mongoDb.read_value(context, "loader_file_location", 1)
            return source_file_list
        except Exception as e:
            self.log.logger.error("Error in get source file link from TestDatabase for loader")
            attach(str(e), name="Error in get source file link from TestDatabase for loader"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get source file link from TestDatabase for loader")
            attach(str(ex), name="Assertion error in get source file link from TestDatabase for loader"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_all_die_id(self, context, wafer_id):
        try:
            if wafer_id != "":
                self.log.logger.info("Getting die id table data against wafer_id : " + wafer_id)
                return database_utilities.get_die_id(context, wafer_id)
        except Exception as e:
            self.log.logger.error("Error in get die id table data against wafer_id : " + wafer_id)
            attach(str(e), name="Error in get die id table data against wafer_id : " + wafer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get die id table data against wafer_id : " + wafer_id)
            attach(str(ex), name="Assertion error in get die id table data against wafer_id : " + wafer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_all_die_all_data(self, context, wafer_id):
        try:
            if wafer_id != "":
                self.log.logger.info("Getting die data table data against wafer_id : " + wafer_id)
                return database_utilities.get_die_all_data(context, wafer_id)
        except Exception as e:
            self.log.logger.error("Error in get die data table data against wafer_id : " + wafer_id)
            attach(str(e), name="Error in get die data table data against wafer_id : " + wafer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get die data table data against wafer_id : " + wafer_id)
            attach(str(ex), name="Assertion error in get die data table data against wafer_id : " + wafer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_lot_id(self, context, test_program_id):
        try:
            if test_program_id != "":
                self.log.logger.info("Getting test parameter table data against test_program_id : " + test_program_id)
                return database_utilities.get_lot_id(context, test_program_id)
        except Exception as e:
            self.log.logger.error("Error in get test parameter table data against test_program_id : " + test_program_id)
            attach(str(e), name="Error in get test parameter table data against test_program_id : " + test_program_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get test parameter table data against test_program_id : " + test_program_id)
            attach(str(ex),
                   name="Assertion error in get test parameter table data against test_program_id : " + test_program_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_wafer_id(self, context, lot_id):
        try:
            if lot_id != "":
                self.log.logger.info("Getting test parameter table data against lot_id : " + lot_id)
                return database_utilities.get_wafer_id(context, lot_id)
        except Exception as e:
            self.log.logger.error("Error in get wafer table all id against lot_id : " + lot_id)
            attach(str(e), name="Error in get wafer table all id against lot_id : " + lot_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get wafer table all id against lot_id : " + lot_id)
            attach(str(ex), name="Assertion error in get wafer table all id against lot_id : " + lot_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_wafer_ids(self, context, lot_id):
        try:
            if lot_id != "":
                self.log.logger.info("Getting wafer table all id's against lot_id : " + lot_id)
                return database_utilities.get_wafer_ids(context, lot_id)
        except Exception as e:
            self.log.logger.error("Error in get wafer table all id's against lot_id : " + lot_id)
            attach(str(e), name="Error in get wafer table all id's against lot_id : " + lot_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get wafer table all id's against lot_id : " + lot_id)
            attach(str(ex), name="Assertion error in get wafer table all id's against lot_id : " + lot_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_policy_id(self, context, name):
        try:
            if name != "":
                self.log.logger.info("Getting policy table id against " + name)
                return database_utilities.get_policy_id(context, name)
        except Exception as e:
            self.log.logger.error("Error in get policy table id against " + name)
            attach(str(e), name="Error in get policy table id against " + name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get policy table id against " + name)
            attach(str(ex), name="Assertion error in get policy table id against " + name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_policy_ids(self, context, name):
        try:
            if name != "":
                self.log.logger.info("Getting policy table all id's against " + name)
                return database_utilities.get_policy_ids(context, name)
        except Exception as e:
            self.log.logger.error("Error in get policy table id's against " + name)
            attach(str(e), name="Error in get policy step table id's against " + name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get policy table id's against " + name)
            attach(str(ex), name="Assertion error in get policy table id's against " + name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_policy_step_id(self, context, policy_id):
        try:
            if policy_id != "":
                self.log.logger.info("Getting policy step table id against " + policy_id)
                return database_utilities.get_policy_step_id(context, policy_id)
        except Exception as e:
            self.log.logger.error("Error in get policy step table id against " + policy_id)
            attach(str(e), name="Error in get policy step table id against " + policy_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get policy step table id against " + policy_id)
            attach(str(ex), name="Assertion error in get policy step table id against " + policy_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_policy_step_ids(self, context, policy_id):
        try:

            if policy_id != "":
                self.log.logger.info("Getting policy step table id's against " + policy_id)
                return database_utilities.get_policy_step_ids(context, policy_id)
        except Exception as e:
            self.log.logger.error("Error in get policy step table id's against " + policy_id)
            attach(str(e), name="Error in get policy step table id's against " + policy_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get policy step table id's against " + policy_id)
            attach(str(ex), name="Assertion error in get policy step table id's against " + policy_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the facility name after marking the file #
    def get_facility_name(self, context, file_name):
        try:
            self.log.logger.info("Getting test parameter table data against file_name : " + file_name)
            return database_utilities.get_facility_name(context, file_name)
        except Exception as e:
            self.log.logger.error("Error in get test parameter table data against file_name : " + file_name)
            attach(str(e), name="Error in get test parameter table data against file_name : " + file_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get test parameter table data against file_name : " + file_name)
            attach(str(ex), name="Assertion error in get test parameter table data against file_name : " + file_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the facility id  after marking the file #
    def get_facility_id(self, context, facility_name):
        try:
            self.log.logger.info("Getting facility id table data against facility name : " + str(facility_name))
            return database_utilities.get_facility_id(context, facility_name)
        except Exception as e:
            self.log.logger.error("Error in get facility id table data against facility name : " + str(facility_name))
            attach(str(e), name="Error in get facility id table data against facility name : " + str(facility_name)
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get facility id table data against facility name : " + str(facility_name))
            attach(str(ex),
                   name="Assertion error in get facility id table data against facility name : " + str(facility_name)
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the customer id  after marking the file #
    def get_customer_id(self, context, facility_id):
        try:
            self.log.logger.info("Getting customer id table data against facility_id : " + facility_id)
            return database_utilities.get_customer_id(context, facility_id)
        except Exception as e:
            self.log.logger.error("Error in get customer id table data against facility_id : " + facility_id)
            attach(str(e), name="Error in get customer id table data against facility_id : " + facility_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get customer id table data against facility_id : " + facility_id)
            attach(str(ex), name="Assertion error in get customer id table data against facility_id : " + facility_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the business unit id  after marking the file #
    def get_business_unit_id(self, context, customer_id):
        try:
            self.log.logger.info("Getting business unit id table data against customer_id + " + customer_id)
            return database_utilities.get_business_unit_id(context, customer_id)
        except Exception as e:
            self.log.logger.error("Error in get business unit id table data against customer_id + " + customer_id)
            attach(str(e), name="Error in get business unit id table data against customer_id + " + customer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get business unit id table data against customer_id + " + customer_id)
            attach(str(ex),
                   name="Assertion error in get business unit id table data against customer_id + " + customer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the work_center id  after marking the file #
    def get_work_center_id(self, context, business_unit_id):
        try:
            self.log.logger.info("Getting test parameter table data against business_unit_id : " + business_unit_id)
            return database_utilities.get_work_center_id(context, business_unit_id)
        except Exception as e:
            self.log.logger.error(
                "Error in get test parameter table data against business_unit_id : " + business_unit_id)
            attach(str(e), name="Error in get test parameter table data against business_unit_id : " + business_unit_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get test parameter table data against business_unit_id : " + business_unit_id)
            attach(str(ex),
                   name="Assertion error in get test parameter table data against business_unit_id : " + business_unit_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the device family id after marking the file #
    def get_device_family_id(self, context, work_center_id):
        try:
            self.log.logger.info("Getting device family id table data against work_center_id : " + work_center_id)
            return database_utilities.get_device_family_id(context, work_center_id)
        except Exception as e:
            self.log.logger.error("Error in get device family id table data against work_center_id : " + work_center_id)
            attach(str(e), name="Error in get device family id table data against work_center_id : " + work_center_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get device family id table data against work_center_id : " + work_center_id)
            attach(str(ex),
                   name="Assertion error in get device family id table data against work_center_id : " + work_center_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the device family id after marking the file #
    def get_device_id(self, context, device_family_id):
        try:
            self.log.logger.info("Getting device id table data against device_family_id : " + device_family_id)
            return database_utilities.get_device_id(context, device_family_id)
        except Exception as e:
            self.log.logger.error("Error in get device id table data against device_family_id : " + device_family_id)
            attach(str(e), name="Error in get device id table data against device_family_id : " + device_family_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get device id table data against device_family_id : " + device_family_id)
            attach(str(ex),
                   name="Assertion error in get device id table data against device_family_id : " + device_family_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the test program id after marking the file #
    def get_test_program_id(self, context, device_id):
        try:
            self.log.logger.info("Getting test program id table data against device_id : " + device_id)
            return database_utilities.get_test_program_id(context, device_id)
        except Exception as e:
            self.log.logger.error("Error in get test program id table data against device_id : " + device_id)
            attach(str(e), name="Error in get test program id table data against device_id : " + device_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get test program id table data against device_id : " + device_id)
            attach(str(ex), name="Assertion error in get test program id table data against device_id : " + device_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the data for test parameter table after marking the file #
    def get_test_program_revision_id(self, context, test_program_id):
        try:
            self.log.logger.info("Getting test parameter table data against test_program_id : " + test_program_id)
            return database_utilities.get_test_program_revision_id(context, test_program_id)
        except Exception as e:
            self.log.logger.error("Error in get test parameter table data against test_program_id : " + test_program_id)
            attach(str(e), name="Error in get test parameter table data against test_program_id : " + test_program_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get test parameter table data against test_program_id : " + test_program_id)
            attach(str(ex),
                   name="Assertion error in get test parameter table data against test_program_id : " + test_program_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the data for test parameter table after marking the file #
    def get_test_parameter_table(self, context, test_program_revision_id):
        try:
            self.log.logger.info(
                "Getting test parameter table data against test_program_revision_id : " + test_program_revision_id)
            return database_utilities.get_test_parameter(context, test_program_revision_id)
        except Exception as e:
            self.log.logger.error(
                "Error in get test parameter table data against test_program_revision_id : " + test_program_revision_id)
            attach(str(e),
                   name="Error in get test parameter table data against test_program_revision_id : " + test_program_revision_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get test parameter table data against test_program_revision_id : " + test_program_revision_id)
            attach(str(ex),
                   name="Assertion error in get test parameter table data against test_program_revision_id : " + test_program_revision_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the data for test parameter table with test parameter id and name after marking the file #
    def get_test_parameter_id(self, context, test_program_id, name):
        try:
            self.log.logger.info(
                "Getting the data for test parameter table with test parameter id and name against test_program_id : " + test_program_id)
            return database_utilities.get_test_parameter_id(context, test_program_id, name)
        except Exception as e:
            self.log.logger.error(
                "Error in get the data for test parameter table with test parameter id and name against test_program_id : " + test_program_id)
            attach(str(e),
                   name="Error in get the data for test parameter table with test parameter id and name against test_program_id : " + test_program_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get the data for test parameter table with test parameter id and name against test_program_id : " + test_program_id)
            attach(str(ex),
                   name="Assertion error in get the data for test parameter table with test parameter id and name against test_program_id : " + test_program_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the data for test parameter table all id's with test parameter id after marking the file #
    def get_test_parameter_ids(self, context, test_program_id):
        try:
            self.log.logger.info("Getting test parameter table all id against test_program_id : " + test_program_id)
            return database_utilities.get_test_parameter_ids(context, test_program_id)
        except Exception as e:
            self.log.logger.error(
                "Error in get test parameter table all id against test_program_id : " + test_program_id)
            attach(str(e), name="Error in get test parameter table all id against test_program_id : " + test_program_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get test parameter table all id against test_program_id : " + test_program_id)
            attach(str(ex),
                   name="Assertion error in get test parameter table all id against test_program_id : " + test_program_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the data for test summary table after marking the file #
    def get_test_summary_table(self, context, test_parameter_id):
        try:
            self.log.logger.info(
                "Getting the data for test summary table against test_parameter_id :" + test_parameter_id)
            return database_utilities.get_test_summary(context, test_parameter_id)
        except Exception as e:
            self.log.logger.error(
                "Error in get the data for test summary table against test_parameter_id :" + test_parameter_id)
            attach(str(e),
                   name="Error in get the data for test summary table against test_parameter_id :" + test_parameter_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get the data for test summary table against test_parameter_id :" + test_parameter_id)
            attach(str(ex),
                   name="Assertion error in get the data for test summary table against test_parameter_id :" + test_parameter_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the data for test summary table against wafer id after marking the file #
    def get_test_summary_against_wafer_id_table(self, context, wafer_id):
        try:
            self.log.logger.info("Getting test summary table data against wafer id :" + wafer_id)
            return database_utilities.get_test_summary_against_wafer_id(context, wafer_id)
        except Exception as e:
            self.log.logger.error("Error in get test summary table data against wafer id :" + wafer_id)
            attach(str(e), name="Error in get test summary table data against wafer id :" + wafer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get test summary table data against wafer id :" + wafer_id)
            attach(str(ex), name="Assertion error in get test summary table data against wafer id :" + wafer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the dynamic table name from test parameter table #
    def get_dynamic_table(self, context, dynamic_table_name, die_id):
        try:
            self.log.logger.info("Getting the dynamic table name from test parameter table against die_id : " + die_id)
            return database_utilities.get_dynamic_table_value(context, dynamic_table_name, die_id)
        except Exception as e:
            self.log.logger.error(
                "Error in get the dynamic table name from test parameter table against die_id : " + die_id)
            attach(str(e),
                   name="Error in get the dynamic table name from test parameter table against die_id : " + die_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get the dynamic table name from test parameter table against die_id : " + die_id)
            attach(str(ex),
                   name="Assertion error in get the dynamic table name from test parameter table against die_id : " + die_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the bin summary table name with bin record  type from test parameter table #
    def get_bin_summary_table(self, context, wafer_id, bin_record_type, bin_number_value):
        try:
            self.log.logger.info(
                "Getting the bin summary table name with bin record  type from test parameter table against wafer_id :" + wafer_id)
            return database_utilities.get_bin_summary(context, wafer_id, bin_record_type, bin_number_value)
        except Exception as e:
            self.log.logger.error(
                "Error in get the bin summary table name with bin record  type from test parameter table against wafer_id :" + wafer_id)
            attach(str(e),
                   name="Error in get the bin summary table name with bin record  type from test parameter table against wafer_id :" + wafer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in get the bin summary table name with bin record  type from test parameter table against wafer_id :" + wafer_id)
            attach(str(ex),
                   name="Assertion error in get the bin summary table name with bin record  type from test parameter table against wafer_id :" + wafer_id
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the data for test dynamic table after marking the file #
    def get_dynamic_table_name(self, context, test_parameter_data):
        try:
            self.log.logger.info("Getting the data for test dynamic table after marking the file")
            return test_parameter_data[0][11]
        except Exception as e:
            self.log.logger.error("Error in get the data for test dynamic table after marking the file ")
            attach(str(e), name="Error in get the data for test dynamic table after marking the file "
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get the data for test dynamic table after marking the file ")
            attach(str(ex), name="Assertion error in get the data for test dynamic table after marking the file "
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I connect to test database #
    def connect_to_test_database(self, context):
        try:
            self.log.logger.info("Connect to test db")
            mongoDb.connect_mongo(context)
        except Exception as e:
            self.log.logger.error("Error in connect to test db")
            attach(str(e), name="Error in connect to test db"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in connect to test db")
            attach(str(ex), name="Assertion error in connect to test db"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Delete the collection data from test database #
    def delete_the_collection_data_from_test_database(self, context, collection_name):
        try:
            mongoDb.connect_mongo(context)
            self.log.logger.info("Delete the collection data from test db against collection name :" + collection_name)
            get_collection_name = mongoDb.get_all_collections(context)
            if collection_name in get_collection_name:
                mongoDb.delete_docs_from_collection(context, collection_name)
            else:
                mongoDb.create_new_collection(context, collection_name)
            self.log.logger.info("Inserting source file link to TestDatabase")
        except Exception as e:
            self.log.logger.error(
                "Error in delete the collection data from test db against collection name :" + collection_name)
            attach(str(e),
                   name="Error in delete the collection data from test db against collection name :" + collection_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in delete the collection data from test db against collection name :" + collection_name)
            attach(str(ex),
                   name="Assertion error in delete the collection data from test db against collection name :" + collection_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Write the collection data from test database #
    def write_value_in_the_collection(self, context, collection_name):
        try:
            mongoDb.connect_mongo(context)
            self.log.logger.info("Write expected output into test db against collection name :" + collection_name)
            mongoDb.write_value(context, collection_name, 1, Constants.collection_file_location_data)
        except Exception as e:
            self.log.logger.error(
                "Error in write expected output into test db against collection name :" + collection_name)
            attach(str(e),
                   name="Error in write expected output into test db against collection name :" + collection_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in write expected output into test db against collection name :" + collection_name)
            attach(str(ex),
                   name="Assertion error in write expected output into test db against collection name :" + collection_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def write_expected_output_in_the_collection(self, context, collection_name, key_name, value):
        try:
            mongoDb.connect_mongo(context)
            self.log.logger.info(
                "Write expected output into test db against collection name :" + collection_name + " with key_name : " + key_name)
            mongoDb.write_value(context, collection_name, key_name, value)
        except Exception as e:
            self.log.logger.error(
                "Error in write expected output into test db against collection name :" + collection_name + " with key_name : " + key_name)
            attach(str(e),
                   name="Error in write expected output into test db against collection name :" + collection_name + " with key_name : " + key_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in write expected output into test db against collection name :" + collection_name + " with key_name : " + key_name)
            attach(str(ex),
                   name="Assertion error in write expected output into test db against collection name :" + collection_name + " with key_name : " + key_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Verify read bin data from data base #
    def verify_read_bin_from_data_base(self, context, list_data, bin_name, wafer_id):
        try:
            hard_binary_no = list_data[2]
            hard_binary_name = list_data[3]
            bin_summary, bin_summary_field_name = self.get_bin_summary_table(context, wafer_id, bin_name,
                                                                             hard_binary_no)

            if "1" not in list_data[0].split(":")[1] or "0" not in list_data[0].split(":")[1]:
                bin_summary_value = bin_summary[0]
            else:
                bin_summary_value = bin_summary[1]
            for index in range(len(bin_summary_value)):
                if index == 6:
                    if str(bin_summary_value[index]) in list_data:
                        attach(str(hard_binary_name),
                               name=bin_name + " bin summary field name " + bin_summary_field_name[index],
                               attachment_type=AttachmentType.TEXT)
                elif bin_summary_value[index] in list_data:
                    attach(bin_summary_value[index],
                           name=bin_name + " bin summary field name " + bin_summary_field_name[index]
                           ,
                           attachment_type=AttachmentType.TEXT)
                elif str(bin_summary_value[index]) in list_data:
                    attach(str(bin_summary_value[index]),
                           name=bin_name + " bin summary field name " + str(bin_summary_field_name[index]),
                           attachment_type=AttachmentType.TEXT)

        except Exception as e:
            self.log.logger.error("Error in verifying bin summary against wafer id : " + str(wafer_id))
            attach(str(e), name="Error in verifying bin summary against wafer id : " + str(wafer_id)
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verifying bin summary against wafer id : " + str(wafer_id))
            attach(str(ex), name="Assertion error in verifying bin summary against wafer id : " + str(wafer_id)
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # I get the names of column against facility name #
    def get_table_column_name_against_facility(self, context, facility_name):
        try:
            self.log.logger.info("I get the names of column against facility name")
            return database_utilities.get_table_columns_name_against_facility_name(context, facility_name)
        except Exception as e:
            self.log.logger.error("Error in get the names of column against facility name : " + facility_name)
            attach(str(e), name="Error in get the names of column against facility name : " + facility_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get the names of column against facility name : " + facility_name)
            attach(str(ex), name="Assertion error in get the names of column against facility name : " + facility_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def read_mongo_data(self, context, collection_name):
        try:
            mongoDb.connect_mongo(context)
            self.log.logger.info("Read the data from mongo db against collection_name : " + collection_name)
            return mongoDb.read_all(context, collection_name)
        except Exception as e:
            self.log.logger.error("Error in read the data from mongo db against collection_name : " + collection_name)
            attach(str(e), name="Error in read the data from mongo db against collection_name : " + collection_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in read the data from mongo db against collection_name : " + collection_name)
            attach(str(ex),
                   name="Assertion error in read the data from mongo db against collection_name : " + collection_name
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def read_mongo_data_value(self, context, collection_name, key):
        try:
            mongoDb.connect_mongo(context)
            self.log.logger.info("I get the expected results for the Parametric Histogram report - Done")
            return mongoDb.read_value(context, collection_name, key)

        except Exception as e:
            self.log.logger.error("Error in get the expected results for the Parametric Histogram report ")
            attach(str(e), name="Error in get the expected results for the Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get the expected results for the Parametric Histogram report")
            attach(str(ex), name="Assertion error in get the expected results for the Parametric Histogram report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex
