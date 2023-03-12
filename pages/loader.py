import logging
import os
import time

from datetime import timezone
from Utilities import performance_log_calculation
from Utilities import payload_modifications
from Utilities.log import Logger
from Utilities import marking_files
from Utilities import yaml_reader
from pages.database import DatabaseManagement
from Helpers.test_db import MongoDb
from config.constants import Constants
from Helpers.loader import Loader
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from pages.converter import ConverterClass
from datetime import datetime
from Helpers.db_config import DataBaseConfig
from config.constants import RollBackTransaction
from config.constants import RollBackTransactionConverter

database = DatabaseManagement()
mongo_db = MongoDb()
loader_helper = Loader()
converter_page = ConverterClass()
database_config = DataBaseConfig()


class LoaderClass:
    expected_ptr_list = []
    expected_ptr_test_number = []
    expected_ptr_result = []
    expected_ptr_list_name = []
    expected_ptr_test_unit = []
    expected_ptr_low_critical_limit = []
    expected_ptr_high_critical_limit = []
    dynamic_table_name = {}
    dynamic_table_values = ""
    test_program_revision_id = {}
    test_parameter_data = {}
    die_ids = {}
    facility_name = {}
    facility_id = {}
    customer_id = {}
    business_unit_id = {}
    work_center_id = {}
    device_family_id = {}
    device_id = {}
    test_program_id = {}
    lot_id = {}
    TSR_data = {}
    HBR_data = {}
    SBR_data = {}
    wafer_id = {}
    generated_hard_bin = {}
    generated_soft_bin = {}
    generated_tsr = {}

    def __init__(self):
        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    """
    Mark the downloaded file for identify the changed
    Create the list of tag in a single line
    Marking the file for loader
    Mark the mir tag
    Mark the wir tag
    Mark the wrr tag
    """

    # Mark the downloaded file for identify the changed #
    def mark_identity(self, context, policy_name, without_marked_file_path, tag_name, mark_file_path):
        try:
            feature_name = context.feature.filename.split("/")[1].split(".")[0]
            self.log.logger.info("Mark the downloaded file for identify the changed")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[without_marked_file_path])
            Constants.marked_facility_name = {}
            for f in files:
                file_path = data[without_marked_file_path] + f
                self.log.logger.info(file_path)
                marking_files.file_marking(context, feature_name, policy_name, file_path, tag_name, mark_file_path)
                self.log.logger.info("file '" + f + "' Marked")
        except Exception as e:
            self.log.logger.error("Error in mark the downloaded file for identify the changed")
            attach(str(e), name="Error in mark the downloaded file for identify the changed"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in mark the downloaded file for identify the changed")
            attach(str(ex), name="Assertion error in mark the downloaded file for identify the changed"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    """
    Save the marked data into test db
    """

    # Save the marked data into test db #
    def save_the_marked_data_into_test_db(self, context, marked_collection):
        try:
            self.log.logger.info("Save the marked data into test db")
            for index in range(len(Constants.marked_file_name)):
                collection_list = mongo_db.get_all_collections(context)
                if marked_collection in collection_list:
                    mongo_db.delete_docs_from_collection(context, marked_collection)
                else:
                    mongo_db.create_new_collection(context, marked_collection)
                mongo_db.write_value(context, marked_collection, Constants.marked_file_name[index],
                                     Constants.marked_file_data[Constants.marked_file_name[index]][index])
            Constants.marked_file_name = []
        except Exception as e:
            self.log.logger.error("Error in save the marked data into test db")
            attach(str(e), name="Error in save the marked data into test db"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in save the marked data into test db")
            attach(str(ex), name="Assertion error in save the marked data into test db"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    """
    Verified the data of file from database after marking the file
    I get the identical PTR data from the file
    I get the facility name after marking the file
    I get the data for test parameter table after marking the file
    I get the data for test dynamic table after marking the file
    Verify the data for test parameter table from database after marking the file
    Verify the data for test dynamic table from database after marking the file
    Attach the table data after verification into the allure report
    """
    # Get the ptr data from marked file
    def get_ptr_data_from_marked_file(self, context, mark_file_path,  policy_name):
        try:
            self.log.logger.info("Getting the data after against facility name that is generated")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[mark_file_path])
            for file_name in files:
                file_path = data[mark_file_path] + file_name
                loader_helper.get_the_ptr_data_from_the_atdf_marked_file(context, file_path
                                                                         , self.expected_ptr_list_name
                                                                         , self.expected_ptr_list
                                                                         , self.expected_ptr_test_number
                                                                         , self.expected_ptr_result
                                                                         , self.expected_ptr_test_unit
                                                                         , self.expected_ptr_low_critical_limit
                                                                         , self.expected_ptr_high_critical_limit)
        except Exception as e:
            self.log.logger.error("Error in getting the data after against facility name that is generated")
            attach(str(e), name="Error in getting the data after against facility name that is generated"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in getting the data after against facility name that is generated")
            attach(str(ex), name="Assertion error in getting the data after against facility name that is generated"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Getting the data after against facility name that is generated #
    def get_all_the_data_from_yield_werx_db(self, context, policy_name, file_path):
        try:
            self.log.logger.info("Getting the data after against facility name that is generated")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[file_path])
            self.facility_name = {}
            for file_name in files:
                self.facility_name[file_name] = []
                # self.facility_name[file_name] = Constants.marked_facility_name[file_name]

                self.facility_name[file_name] = database.get_facility_name(context, file_name)
                self.log.logger.info("Get facility name from test db : " + self.facility_name[file_name])
                attach(str(self.facility_name[file_name]), name="Facility name "
                       , attachment_type=AttachmentType.TEXT)
                start_time = datetime.now()
                while True:
                    end_time = datetime.now()
                    cal_time = end_time.minute - start_time.minute
                    if cal_time < 1:
                        try:
                            self.facility_id[file_name] = database.get_facility_id(context, self.facility_name[file_name])
                            break
                        except Exception as f:
                            self.log.logger.error("Not getting facility id against facility name : " + self.facility_name[file_name])
                    else:
                        now_time = datetime.now(timezone.utc)
                        # attach(str(now_time),
                        #        name="Error in getting facility name after 2 "
                        #             "minutes but get the success status of the file: " + str(now_time)
                        #        , attachment_type=AttachmentType.TEXT)
                        assert False, "Error in getting facility name after 2 " \
                                      "minutes but get the success status of the file: " + str(now_time)
                self.customer_id[file_name] = database.get_customer_id(context, self.facility_id[file_name])
                self.business_unit_id[file_name] = database.get_business_unit_id(context, self.customer_id[file_name])
                self.work_center_id[file_name] = database.get_work_center_id(context, self.business_unit_id[file_name])
                self.device_family_id[file_name] = database.get_device_family_id(context, self.work_center_id[file_name])
                self.device_id[file_name] = database.get_device_id(context, self.device_family_id[file_name])
                self.test_program_id[file_name] = database.get_test_program_id(context, self.device_id[file_name])
                self.test_program_revision_id[file_name] = database.get_test_program_revision_id(context,
                    self.test_program_id[file_name])
                self.lot_id[file_name] = database.get_lot_id(context, self.test_program_revision_id[file_name])
                self.wafer_id[file_name] = database.get_wafer_id(context, self.lot_id[file_name])
                self.test_parameter_data[file_name] = database.get_test_parameter_table(context,
                    self.test_program_revision_id[file_name])
                self.die_ids[file_name] = database.get_all_die_id(context, self.wafer_id[file_name])
        except Exception as e:
            self.log.logger.error("Error in getting facility name after 2 " \
                                      "minutes but get the success status of the file: " + str(now_time))
            attach(str(e), name="Error in getting the data after against facility name that is generated"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in getting the data after against facility name that is generated")
            attach(str(ex), name="Assertion error in getting the data after against facility name that is generated"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Verified the data of file from database after marking the file #
    def verification_of_the_test_parameter_table_after_marking(self, context, policy_name, mark_file_path):
        try:
            self.log.logger.info("Verifying the data of file is verified from database after marking the file")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[mark_file_path])
            for file_name in files:
                file_path = data[mark_file_path] + file_name
                loader_helper.get_the_ptr_data_from_the_atdf_marked_file(context, file_path
                                                                         , self.expected_ptr_list_name
                                                                         , self.expected_ptr_list
                                                                         , self.expected_ptr_test_number
                                                                         , self.expected_ptr_result
                                                                         , self.expected_ptr_test_unit
                                                                         , self.expected_ptr_low_critical_limit
                                                                         , self.expected_ptr_high_critical_limit)
                loader_helper.verify_the_test_parameter(context, self.test_parameter_data[file_name], self.expected_ptr_list_name
                                                        , self.expected_ptr_test_number
                                                        , self.expected_ptr_low_critical_limit
                                                        , self.expected_ptr_high_critical_limit)
                loader_helper.adding_the_test_parameter_test_result_into_the_report(context, file_name, self.lot_id[file_name],
                                                                                    self.wafer_id[file_name],
                                                                                    self.die_ids[file_name],
                                                                                    self.facility_name[file_name],
                                                                                    self.expected_ptr_test_number,
                                                                                    self.expected_ptr_list_name,
                                                                                    self.expected_ptr_low_critical_limit,
                                                                                    self.expected_ptr_high_critical_limit)
        except Exception as e:
            self.log.logger.error("Error in verifying the data of file is verified from database after marking the file")
            attach(str(e), name="Error in verifying the data of file is verified from database after marking the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verifying the data of file is verified from database after marking the file")
            attach(str(ex), name="Assertion error in verifying the data of file is verified from database after marking the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    """
    Verified the dynamic table data  after marking the file
    I get the dynamic table name from test parameter table
    """

    # Verified the dynamic table data  after marking the file #
    def verification_of_the_dynamic_table_data_after_marking(self, context):
        try:
            self.log.logger.info("Verified the dynamic table data  after marking the file")
            for file_name in self.test_parameter_data.keys():
                self.dynamic_table_name[file_name] = database.get_dynamic_table_name(context, self.test_parameter_data[file_name])
                for die_id in self.die_ids[file_name]:
                    try:
                        self.dynamic_table_values = database.get_dynamic_table(context, self.dynamic_table_name[file_name], die_id[0])
                    except Exception as e:
                        print(e)
                    loader_helper.verify_the_dynamic_table(context, self.dynamic_table_values, self.expected_ptr_result)
            if len(self.dynamic_table_values) != 0:
                self.log.logger.info("Validated the dynamic table")
                attach("Dynamic table name " + self.dynamic_table_name[file_name] +
                       " created successfully",
                       name="Verified the dynamic table ",
                       attachment_type=AttachmentType.TEXT)
            else:
                self.log.logger.warn("Dynamic table name " + self.dynamic_table_name[file_name] +
                                     " not created successfully")
                attach("Dynamic table name " + self.dynamic_table_name[file_name] +
                       " not created successfully",
                       name="Error Verified the dynamic table ",
                       attachment_type=AttachmentType.TEXT)
                assert False
            loader_helper.adding_the_table_dynamic_table_result_into_the_report(context, file_name, self.expected_ptr_result)
        except Exception as e:
            self.log.logger.error("Error in verified the dynamic table data  after marking the file")
            attach(str(e), name="Error in verified the dynamic table data  after marking the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verified the dynamic table data  after marking the file")
            attach(str(ex), name="Assertion error in verified the dynamic table data  after marking the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    """
    Attach the result into the allure report
    
    """

    # Attach the result into the allure report #

    def attach_result_into_the_allure_report(self, context):
        try:
            self.log.logger.info("Attach data into allure report")
            for file_name in self.dynamic_table_name.keys():
                loader_helper.adding_the_table_verify_result_into_the_report(context, file_name, self.facility_name[file_name],
                                                                             self.expected_ptr_test_number,
                                                                             self.expected_ptr_result,
                                                                             self.expected_ptr_list_name,
                                                                             self.expected_ptr_low_critical_limit,
                                                                             self.expected_ptr_high_critical_limit,
                                                                             self.expected_ptr_test_unit)
        except Exception as e:
            self.log.logger.error("Error in attach data into allure report")
            attach(str(e), name="Error in attach data into allure report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in attach data into allure report")
            attach(str(ex), name="Assertion error in attach data into allure report"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_data_from_file(self, context, tag_name, policy_name, marked_file_path):
        try:
            self.log.logger.info("Get the HBR , SBR and TSR data from marked file")
            HBR_list = []
            TSR_list = []
            SBR_list = []
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[marked_file_path])
            for file_name in files:
                file_path = data[marked_file_path] + file_name
                self.log.logger.info(file_path)
                file_gold = open(file_path, "r")

                file_1_line = file_gold.readline()
                while file_1_line != '':
                    for tag in tag_name.split(","):

                        if tag.strip() in file_1_line:
                            file_1_line = file_1_line.split("|")
                            if "HBR" in tag:
                                HBR_list.append(file_1_line)

                            elif "SBR" in tag:
                                SBR_list.append(file_1_line)

                            else:
                                TSR_list.append(file_1_line)

                            break
                            self.log.logger.info(file_1_line)
                    file_1_line = file_gold.readline()
                self.HBR_data[file_name] = HBR_list
                self.SBR_data[file_name] = SBR_list
                self.TSR_data[file_name] = TSR_list
                self.log.logger.info("Done")
        except Exception as e:
            self.log.logger.error("Error in get the HBR , SBR and TSR data from marked file")
            attach(str(e), name="Error in get the HBR , SBR and TSR data from marked file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get the HBR , SBR and TSR data from marked file")
            attach(str(ex), name="Assertion error in get the HBR , SBR and TSR data from marked file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def generate_bin_summary_data_from_file(self, context, bin_number, bin_name, policy_name, marked_file_path):
        try:
            self.log.logger.info("Generated bin summary data from marked file")
            count = 0
            head_no = ''
            site_no = ''
            flag = ''
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[marked_file_path])
            for file_name in files:
                file_path = data[marked_file_path] + file_name
                self.log.logger.info(file_path)
                file_gold = open(file_path, "r")
                line = file_gold.readline()
                while line != '':
                    expected_value = str(line).split("|")
                    if "PRR" in expected_value[0]:
                        if 'hard' in bin_name:
                            bin_index = expected_value[5]
                        else:
                            bin_index = expected_value[6]
                        if bin_number == bin_index:
                            count += 1
                            head_no = expected_value[0].split(":")[1]
                            site_no = expected_value[1]
                            flag = expected_value[4]
                    line = file_gold.readline()
                self.log.logger.info("Done")
                return head_no, site_no, flag, count
        except Exception as e:
            self.log.logger.error("Error in generated bin summary data from marked file")
            attach(str(e), name="Error in generated bin summary data from marked file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in generated bin summary data from marked file")
            attach(str(ex), name="Assertion error in generated bin summary data from marked file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_bin_number(self, context, bin_name, file):
        try:
            self.log.logger.info("Get bin number from PRR tag from file")
            bin_number_list = []
            file = open(file, "r")
            line = file.readline()
            while line != '':
                expected_value = str(line).split("|")

                if "PRR" in expected_value[0]:
                    if 'hard' in bin_name:
                        bin_index = expected_value[5]
                    else:
                        bin_index = expected_value[6]
                    if bin_index not in bin_number_list:
                        bin_number_list.append(bin_index)
                    else:
                        self.log.logger.warn("Bin Number already in the list")
                line = file.readline()
            return bin_number_list
        except Exception as e:
            self.log.logger.error("Error in get bin number from PRR tag from file")
            attach(str(e), name="Error in get bin number from PRR tag from file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get bin number from PRR tag from file")
            attach(str(ex), name="Assertion error in get bin number from PRR tag from file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def generate_bin_summary_for_bin(self, context, bin_name, bin_number, file):
        try:
            self.log.logger.info("Generated bin summary data from file")
            count = 0
            bin_data = []
            head_no = ""
            site_no = ""
            flag = ""
            file = open(file, "r")
            line = file.readline()
            while line != '':
                expected_value = str(line).split("|")
                if "PRR" in expected_value[0]:
                    if 'hard' in bin_name:
                        bin_index = expected_value[5]
                    else:
                        bin_index = expected_value[6]
                    if bin_number == bin_index:
                        count += 1
                        head_no = expected_value[0].split(":")[1]
                        site_no = expected_value[1]
                        flag = expected_value[4]
                line = file.readline()
            bin_data.append(head_no)
            bin_data.append(site_no)
            bin_data.append(count)
            bin_data.append(flag)
            return bin_data
        except Exception as e:
            self.log.logger.error("Error in generated bin summary data from file")
            attach(str(e), name="Error in generated bin summary data from file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in generated bin summary data from file")
            attach(str(ex), name="Assertion error in generated bin summary data from file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_test_summary_table(self, context):
        try:
            self.log.logger.info("Verifying the test summary table")
            for file_name in self.wafer_id.keys():
                if len(self.TSR_data) > 0:
                    try:
                        test_parameter_ids = database.get_test_parameter_ids(context, self.test_program_revision_id[file_name])
                        TSR_Lists = self.TSR_data[file_name]
                        for TSR_List in TSR_Lists:
                            for test_parameter_id in test_parameter_ids:
                                test_summaries, test_summary_field = database.get_test_summary_table(context,
                                    test_parameter_id[0])
                                # value = len(test_summary[0])
                                if len(test_summaries) > 0:
                                    for test_summary in test_summaries:
                                        for index in range(len(test_summary[0])):
                                            if test_summary[0][index] in TSR_List:
                                                attach("verified", name=test_summary_field[index] + " : "
                                                                        + test_summary[0][index] + " in data base bin summary",
                                                       attachment_type=AttachmentType.TEXT)
                                            elif str(test_summary[0][index]) in TSR_List:
                                                attach("verified"
                                                       , name=str(test_summary_field[index]) + " : " + str(
                                                        test_summary[0][index]) + " in data base bin summary",
                                                       attachment_type=AttachmentType.TEXT)
                                else:
                                    assert False, "Test parameter id is null in test summary against wafer id : " + self.wafer_id[
                            file_name]
                                    break
                    except Exception as e:
                        self.log.logger.error(
                            "Test parameter id is null in test summary against wafer id : " + self.wafer_id[file_name])
                        attach(str(e), name="Test parameter id is null in test summary against wafer id : " + self.wafer_id[
                            file_name]
                               , attachment_type=AttachmentType.TEXT)
                        assert False, "Test parameter id is null in test summary against wafer id : " + self.wafer_id[
                            file_name]
                else:
                    try:
                        TSR_Lists = self.generated_tsr[file_name]
                        for key in TSR_Lists:
                            test_parameter_ids = database.get_test_parameter_ids(context,
                                self.test_program_revision_id[file_name])
                            for test_parameter_id in test_parameter_ids:
                                test_summaries, test_summary_field = database.get_test_summary_table(context,
                                    test_parameter_id[0])
                                for test_summary in test_summaries:
                                    try:
                                        assert TSR_Lists[key][1] in test_summary
                                    except Exception as e:
                                        if len(test_summary) > 0:
                                            attach(str(test_summary[12]),
                                                   name="Sequencer_name is getting null in test summary table"
                                                   , attachment_type=AttachmentType.TEXT)
                                            break

                                        assert False, "Sequencer_name is getting null in test summary table"
                                        self.log.logger.warn(
                                            "Sequence name found in test summary : " + str(test_summary[0][11]))
                                        self.log.logger.warn(
                                            "Sequence name found in test summary : " + str(test_summary[1][11]))

                                # print(test_summary)
                    except AssertionError as e:
                        self.log.logger.error("Test summary table against wafer id : " + self.wafer_id[file_name] +
                                              " is not generated")
                        attach(str(e), name="Test summary table against wafer id : " + self.wafer_id[file_name] +
                                            " is not generated", attachment_type=AttachmentType.TEXT)
                        assert False
        except Exception as e:
            self.log.logger.error("Error in verifying the test summary table")
            attach(str(e), name="Error in verifying the test summary table"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verifying the test summary table")
            attach(str(ex), name="Assertion error in verifying the test summary table"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_bin_summary_table(self, context):
        try:
            self.log.logger.info("Verifying the bin summary table")

            for file_name in self.wafer_id.keys():
                HBR_Lists = self.HBR_data[file_name]
                SBR_Lists = self.SBR_data[file_name]
                for HBR_List in HBR_Lists:
                    hard_binary_no = HBR_List[2]
                    hard_binary_name = HBR_List[3]

                    bin_summary, bin_summary_field_name = database.get_bin_summary_table(context, self.wafer_id[file_name], "Hard",
                                                                                         hard_binary_no)
                    for index in range(len(bin_summary[0])):
                        if index == 6:
                            if str(bin_summary[0][index]) in HBR_List:
                                attach(str(hard_binary_name),
                                       name="Hard bin summary field name " + bin_summary_field_name[index],
                                       attachment_type=AttachmentType.TEXT)
                        elif bin_summary[0][index] in HBR_List:
                            attach(bin_summary[0][index],
                                   name="Hard bin summary field name " + bin_summary_field_name[index]
                                   ,
                                   attachment_type=AttachmentType.TEXT)
                        elif str(bin_summary[0][index]) in HBR_List:
                            attach(str(bin_summary[0][index]),
                                   name="Hard bin summary field name " + str(bin_summary_field_name[index]),
                                   attachment_type=AttachmentType.TEXT)
                for SBR_List in SBR_Lists:
                    soft_binary_no = SBR_List[2]
                    soft_binary_name = SBR_List[3]
                    bin_summary, bin_summary_field_name = database.get_bin_summary_table(context, self.wafer_id[file_name], "Soft",
                                                                                         soft_binary_no)
                    for index in range(len(bin_summary[0])):
                        if index == 7:
                            if str(bin_summary[0][index]) in SBR_List:
                                attach(str(soft_binary_name),
                                       name="Soft bin summary field name " + str(bin_summary_field_name[index])
                                       ,
                                       attachment_type=AttachmentType.TEXT)
                        elif bin_summary[0][index] in SBR_List:
                            attach(bin_summary[0][index], name="Soft bin summary field name " +
                                                               bin_summary_field_name[index],
                                   attachment_type=AttachmentType.TEXT)
                        elif str(bin_summary[0][index]) in SBR_List:
                            attach(str(bin_summary[0][index]),
                                   name="Soft bin summary field name " + str(bin_summary_field_name[index]),
                                attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error(
                "Error in verifying the bin summary table")
            attach(str(e),
                   name="Error in verifying the bin summary table"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error(
                "Assertion error in verifying the bin summary table")
            attach(str(ex),
                   name="Assertion error in verifying the bin summary table"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def verify_bin_summary_table_for_read_and_generated_checkbox(self, context, checkbox):
        try:
            self.log.logger.info("Verifying the bin summary table for read and generate checkbox")
            for file_name in self.wafer_id.keys():

                checkbox_lists = checkbox.split(",")
                for checkbox_list in checkbox_lists:
                    if "readHbr" in checkbox_list:
                        HBR_Lists = self.HBR_data[file_name]
                        for HBR_List in HBR_Lists:
                            database.verify_read_bin_from_data_base(context, HBR_List, "Hard", self.wafer_id[file_name])
                    elif "readSBR" in checkbox_list:
                        SBR_Lists = self.SBR_data[file_name]
                        for SBR_List in SBR_Lists:
                            database.verify_read_bin_from_data_base(context, SBR_List, "Soft", self.wafer_id[file_name])
                    elif "generateHbr" in checkbox_list:
                        HBR_generated_lists = self.generated_hard_bin
                        for key in HBR_generated_lists.keys():
                            HBR_generated_list = HBR_generated_lists[key]
                            loader_helper.verify_generated_bin_data_from_data_base(context, HBR_generated_list, "Hard", key,
                                                                                   self.wafer_id[file_name])
                    else:
                        SBR_generated_lists = self.generated_soft_bin
                        for key in SBR_generated_lists.keys():
                            SBR_generated_list = SBR_generated_lists[key]
                            loader_helper.verify_generated_bin_data_from_data_base(context, SBR_generated_list, "Soft", key,
                                                                                   self.wafer_id[file_name])
        except Exception as e:
            self.log.logger.error("Error in verifying the bin summary table for read and generate checkbox")
            attach(str(e), name="Error in verifying the bin summary table for read and generate checkbox"
                   , attachment_type=AttachmentType.TEXT)
            assert False, str(e)

        except AssertionError as ex:
            self.log.logger.error("Assertion error in verifying the bin summary table for read and generate checkbox")
            attach(str(ex), name="Assertion error in verifying the bin summary table for read and generate checkbox"
                   , attachment_type=AttachmentType.TEXT)
            assert False, str(ex)

    # Update The Payload Policy for selection criteria #
    def updated_the_payload_for_selection_criteria(self, context, payload_path, payload_policy):
        try:
            self.log.logger.info("Update The payload policy for selection criteria")
            for file_name in self.wafer_id.keys():
                test_parameter_ids = database.get_test_parameter_ids(context, self.test_program_revision_id[file_name])
                payload_modifications.payload_update_for_selection_criteria(context, payload_path, payload_policy
                                                                            , self.facility_id[file_name]
                                                                            , self.work_center_id[file_name]
                                                                            , self.device_id[file_name]
                                                                            , self.test_program_id[file_name]
                                                                            , self.test_program_revision_id[file_name]
                                                                            , self.lot_id[file_name]
                                                                            , self.wafer_id[file_name]
                                                                            , test_parameter_ids)
                attach(str(payload_policy), name="Update The Payload Policy for selection criteria",
                       attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error("Error in update The payload policy for selection criteria")
            attach(str(e), name="Error in update The payload policy for selection criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in update The payload policy for selection criteria")
            attach(str(ex), name="Assertion error in update The payload policy for selection criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    # Calculate the execution time for selection criteria #
    def calculate_execution_time_for_selection_criteria(self, context, payload, policy_name):
        try:
            self.log.logger.info("Calculate the execution time for selection criteria")
            starting_time = str(datetime.now())
            converter_page.post_policy_api_endpoint(context, policy_name, payload)
            ending_time = str(datetime.now())

            calculated_execution_time = performance_log_calculation.performance_calc_for_selection_criteria(context,
                starting_time
                , ending_time)
            attach(str(calculated_execution_time), name="Calculated execution time",
                   attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error("Error in calculate the execution time for selection criteria")
            attach(str(e), name="Error in calculate the execution time for selection criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in calculate the execution time for selection criteria")
            attach(str(ex), name="Assertion error in calculate the execution time for selection criteria"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def updated_the_payload_for_checkbox(self, context, payload_path, payload_policy, new_policy_name, checkbox, bucket_name):
        try:
            self.log.logger.info("Update The Payload Policy for : " + checkbox)
            date_time = datetime.now()
            feature_name = context.feature.filename
            feature_name = feature_name.split(".")[0].split("/")[1]
            new_policy_name = new_policy_name + "for" + feature_name + " " + str(date_time)
            Constants.new_policy_name = new_policy_name
            attach(str(new_policy_name), name="Modify policy name",
                   attachment_type=AttachmentType.TEXT)
            payload_modifications.payload_update_with_checkbox(context, payload_path, payload_policy, new_policy_name, checkbox,
                                                               bucket_name)
            attach(str(payload_policy), name="Update The Payload Policy",
                   attachment_type=AttachmentType.TEXT)
        except Exception as e:
            self.log.logger.error("Error in update The Payload Policy for : "+ checkbox)
            attach(str(e), name="Error in update The Payload Policy for : "+ checkbox
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in update The Payload Policy for : "+ checkbox)
            attach(str(ex), name="Assertion error in update The Payload Policy for : "+ checkbox
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def generate_the_bin_summary_record(self, context, bin_summary, policy_name, mark_file_path):
        try:
            self.log.logger.info("Data of file is verified from database after marking the file")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[mark_file_path])
            bin_data = {}
            bin_lists = bin_summary.split(",")

            for file_name in files:
                file_path = data[mark_file_path] + file_name
                for bin_list in bin_lists:
                    bin_name = bin_list.strip()
                    bin_numbers = self.get_bin_number(context, bin_name, file_path)
                    for bin_number in bin_numbers:
                        bin_data[bin_number] = self.generate_bin_summary_for_bin(context, bin_name, bin_number, file_path)
                    if "hard" in bin_name:
                        self.generated_hard_bin = bin_data
                    else:
                        self.generated_soft_bin = bin_data
        except Exception as e:
            self.log.logger.error("Error in data of file is verified from database after marking the file")
            attach(str(e), name="Error in data of file is verified from database after marking the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in data of file is verified from database after marking the file")
            attach(str(ex), name="Assertion error in data of file is verified from database after marking the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def rollback_the_transaction(self, context, marked_file_path):
        try:
            self.log.logger.info("Cleaning the data base after creating loader policy")
            policy_name = "Loader"
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[marked_file_path])
            self.get_all_the_data_from_yield_werx_db(context, policy_name, marked_file_path)
            for file_name in files:
                test_parameter_ids = database.get_test_parameter_ids(context, self.test_program_revision_id[file_name])
                if len(test_parameter_ids) > 0:
                    self.dynamic_table_name[file_name] = database.get_dynamic_table_name(context,
                        self.test_parameter_data[file_name])
                    database_config.run_query_to_drop_table(context, self.dynamic_table_name[file_name])

                if len(self.lot_id) != 0:
                    wafer_ids = database.get_wafer_ids(context, self.lot_id[file_name])
                    for wafer_id in wafer_ids:
                        database_config.run_query_to_delete_file(context, RollBackTransaction.test_summary, RollBackTransaction.wafer_id,
                                                                 wafer_id[0])
                        database_config.run_query_to_delete_file(context, RollBackTransaction.bin_summary, RollBackTransaction.wafer_id,
                                                                 wafer_id[0])
                        database_config.run_query_to_update_the_record(context, RollBackTransaction.die,
                                                                       RollBackTransaction.source_die_id,
                                                                       RollBackTransaction.null,
                                                                       RollBackTransaction.wafer_id, wafer_id[0])
                        database_config.run_query_to_delete_file(context, RollBackTransaction.die, RollBackTransaction.wafer_id,
                                                                 wafer_id[0])

                database_config.run_query_to_delete_file(context, RollBackTransaction.wafer,
                                                         RollBackTransaction.lot_id, self.lot_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.lot,
                                                         RollBackTransaction.test_program_revision_id,
                                                         self.test_program_revision_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.test_parameter,
                                                         RollBackTransaction.test_program_revision_id,
                                                         self.test_program_revision_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.test_program_revision,
                                                         RollBackTransaction.test_program_id,
                                                         self.test_program_id[file_name])
                database_config.run_query_to_update_the_record(context, RollBackTransaction.test_program,
                                                               RollBackTransaction.device_id,
                                                               RollBackTransaction.null, RollBackTransaction.device_id,
                                                               self.device_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.test_program, RollBackTransaction.device_id,
                                                         self.device_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.device, RollBackTransaction.device_family_id,
                                                         self.device_family_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.device_family,
                                                         RollBackTransaction.work_center_id,
                                                         self.work_center_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.work_center,
                                                         RollBackTransaction.business_unit_id,
                                                         self.business_unit_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.business_unit, RollBackTransaction.customer_id,
                                                         self.customer_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.customer, RollBackTransaction.facility_id,
                                                         self.facility_id[file_name])
                database_config.run_query_to_delete_file(context, RollBackTransaction.facility, RollBackTransaction.name,
                                                         self.facility_name[file_name])
                workflow_steps = Constants.workflow_step
                for workflow_step in workflow_steps:
                    database_config.run_query_to_delete_workflow_load_table_data(context, RollBackTransaction.workflow_load_file,
                                                             RollBackTransaction.file_name,
                                                             file_name, workflow_step)
                policy_ids = database.get_policy_ids(context, Constants.new_policy_name)
                for policy_id in policy_ids:
                    policy_id = policy_id[0]
                    try:
                        policy_step_id = database.get_policy_step_id(context, policy_id)
                        database_config.run_query_to_delete_file(context, RollBackTransaction.loader_load_policy_step,
                                                                 RollBackTransaction.policy_step_id,
                                                                 policy_step_id)
                        database_config.run_query_to_delete_file(context, RollBackTransaction.file_location,
                                                                 RollBackTransaction.container,
                                                                 RollBackTransaction.container_name)
                        database_config.run_query_to_delete_file(context, RollBackTransaction.workflow_step,
                                                                 RollBackTransaction.policy_step_id,
                                                                 policy_step_id)

                    except Exception as e:
                        self.log.logger.warn("Policy step table data is not present against policy id :" + policy_id)
                    try:
                        work_flow_instance_ids = database_config.run_query_to_get_id_without_created_by_id(context, RollBackTransaction.workflow_instance
                                                                                                           , RollBackTransaction.policy_id, policy_id)
                        for work_flow_instance_id in work_flow_instance_ids:
                            work_flow_instance_id = work_flow_instance_id[0]
                            database_config.run_query_to_delete_file(context, RollBackTransaction.workflow_step,
                                                                     RollBackTransaction.workflow_instance_id,
                                                                     work_flow_instance_id)
                    except Exception as e:
                        self.log.logger.warn("Work flow instance  table data is not present against policy id :" + policy_id)

                    database_config.run_query_to_delete_file_without_created_by_id(context, RollBackTransaction.workflow_instance,
                                                                                   RollBackTransaction.policy_id,
                                                                                   policy_id)
                    database_config.run_query_to_delete_file(context, RollBackTransaction.policy_step,
                                                             RollBackTransaction.policy_id,
                                                             policy_id)

                    database_config.run_query_to_update_the_record(context, RollBackTransaction.Policy,
                                                                   RollBackTransaction.source_policy_id,
                                                                   RollBackTransaction.null,
                                                                   RollBackTransaction.id, policy_id)
                    database_config.run_query_to_delete_file(context, RollBackTransaction.Policy, RollBackTransaction.id,
                                                             policy_id)
        except Exception as e:
            self.log.logger.error("Error in cleaning the data base after creating loader policy")
            attach(str(e), name="Error in cleaning the data base after creating loader policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in cleaning the data base after creating loader policy")
            attach(str(ex), name="Assertion error in cleaning the data base after creating loader policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def rollback_the_transaction_for_converter(self, context):
        try:
            self.log.logger.info("Cleaning the data base after creating converter policy")
            data = yaml_reader.data_reader_from_test_data(context, "Converter")
            files = os.listdir(data[Constants.Input_Golden_file_Path])
            for file_name in files:
                database_config.run_query_to_delete_file(context, RollBackTransactionConverter.workflow_load_file,
                                                         RollBackTransactionConverter.file_name,
                                                         file_name)
                policy_ids = database.get_policy_ids(context, Constants.new_policy_name)
                for policy_id in policy_ids:
                    policy_id = policy_id[0]
                    try:
                        policy_step_id = database.get_policy_step_id(context, policy_id)
                        database_config.run_query_to_delete_file(context, RollBackTransactionConverter.loader_load_policy_step,
                                                                 RollBackTransactionConverter.policy_step_id,
                                                                 policy_step_id)
                        database_config.run_query_to_delete_file(context, RollBackTransactionConverter.file_location,
                                                                 RollBackTransactionConverter.container,
                                                                 RollBackTransactionConverter.container_name)
                        database_config.run_query_to_delete_file(context, RollBackTransactionConverter.workflow_step,
                                                                 RollBackTransactionConverter.policy_step_id,
                                                                 policy_step_id)
                    except Exception as e:
                        self.log.logger.warn("Policy step table data is not present against policy id :" + policy_id)
                    database_config.run_query_to_delete_file_without_created_by_id(context, RollBackTransactionConverter.workflow_instance,
                                                                                   RollBackTransactionConverter.policy_id,
                                                                                   policy_id)
                    database_config.run_query_to_delete_file(context, RollBackTransactionConverter.policy_step,
                                                             RollBackTransactionConverter.policy_id,
                                                             policy_id)

                    database_config.run_query_to_update_the_record(context, RollBackTransactionConverter.Policy,
                                                                   RollBackTransactionConverter.source_policy_id,
                                                                   RollBackTransactionConverter.null,
                                                                   RollBackTransactionConverter.id, policy_id)
                    database_config.run_query_to_delete_file(context, RollBackTransactionConverter.Policy,
                                                             RollBackTransactionConverter.id,
                                                             policy_id)

        except Exception as e:
            self.log.logger.error("Error in cleaning the data base after creating converter policy")
            attach(str(e), name="Error in cleaning the data base after creating converter policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in cleaning the data base after creating converter policy")
            attach(str(ex), name="Assertion error in cleaning the data base after creating converter policy"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def generate_the_test_summary_record(self, context, policy_name, mark_file_path):
        try:
            self.log.logger.info("Data of file is verified from database after marking the file")
            data = yaml_reader.data_reader_from_test_data(context, policy_name)
            files = os.listdir(data[mark_file_path])
            test_data = {}
            for file_name in files:
                file_path = data[mark_file_path] + file_name
                test_names = self.get_test_summary_name(context, file_path)
                for test_name in test_names:
                    test_data[test_name] = self.generate_test_summary(context, test_name, file_path)
            self.generated_tsr[file_name] = test_data
        except Exception as e:
            self.log.logger.error("Error in data of file is verified from database after marking the file")
            attach(str(e), name="Error in data of file is verified from database after marking the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in data of file is verified from database after marking the file")
            attach(str(ex), name="Assertion error in data of file is verified from database after marking the file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def generate_test_summary(self, context, test_name, file):
        try:
            self.log.logger.info("Generated PTR data from file")
            test_data = []
            value = 0
            file = open(file, "r")
            line = file.readline()
            while line != '':
                expected_count = 0
                expected_value = str(line).split("|")
                if "PTR" in expected_value[0]:
                    if test_name in expected_value:
                        value = value + float(expected_value[15])
                        expected_count += 1
                        test_data.append(expected_value[15])
                line = file.readline()
            return value, expected_count
        except Exception as e:
            self.log.logger.error("Error in generated PTR data from file")
            attach(str(e), name="Error in generated PTR data from file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in generated PTR data from file")
            attach(str(ex), name="Assertion error in generated PTR data from file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def get_test_summary_name(self, context, file):
        try:
            test_name_list = []
            self.log.logger.info("Get test summary name from PTR tag from file")
            file = open(file, "r")
            line = file.readline()
            while line != '':
                expected_value = str(line).split("|")
                if "PTR" in expected_value[0]:
                    test_name_list.append(expected_value[6])
                line = file.readline()
            return set(test_name_list)

        except Exception as e:
            self.log.logger.error("Error in get test summary name from PTR tag from file")
            attach(str(e), name="Error in get test summary name from PTR tag from file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Assertion error in get test summary name from PTR tag from file")
            attach(str(ex), name="Assertion error in get test summary name from PTR tag from file"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex
