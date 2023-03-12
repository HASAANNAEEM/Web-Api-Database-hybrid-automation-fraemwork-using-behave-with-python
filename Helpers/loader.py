import decimal
import math
import logging
import re

from Utilities.log import Logger
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from config.constants import Constants
from pages.database import DatabaseManagement


class Loader:
    def __init__(self):
        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    # I get the identical PTR data from the file #
    def get_the_ptr_data_from_the_atdf_marked_file(self, context, file_path
                                                   , expected_ptr_list_name
                                                   , expected_ptr_list, expected_ptr_test_number
                                                   , expected_ptr_result, expected_ptr_test_unit,
                                                   expected_ptr_low_critical_limit,
                                                   expected_ptr_high_critical_limit):
        self.log.logger.info(file_path)
        file_row = open(file_path, "r")
        tag_name = "PTR"
        for line in file_row:
            try:
                expected_value = str(line).split("|")
                value2 = expected_value[Constants.first_index]
                if tag_name in value2:
                    if expected_value[3] not in expected_ptr_result:
                        expected_ptr_result.append(expected_value[3])
                    if line not in expected_ptr_list:
                        if expected_value[6] not in expected_ptr_list_name:
                            expected_ptr_list.append(line)
                            test_number = expected_value[Constants.first_index].split(":")[1]
                            expected_ptr_test_number.append(test_number)
                            expected_ptr_list_name.append(expected_value[6])
                            expected_ptr_test_unit.append(expected_value[9])
                            expected_ptr_low_critical_limit.append(expected_value[10])
                            expected_ptr_high_critical_limit.append(expected_value[11])
            except Exception as e:
                self.log.logger.error("Error in line  : " + line)

    # Verify the data for test parameter table from database after marking the file #
    def verify_the_test_parameter(self, context, test_parameter_data, expected_ptr_list_name, expected_ptr_test_number,
                                  expected_ptr_low_critical_limit, expected_ptr_high_critical_limit):
        self.log.logger.info("Verify the test parameter")
        ptr_low_critical_limit_result = False
        ptr_high_critical_limit_result = False

        for ptr_data_list in test_parameter_data:
            try:
                value = ptr_data_list[5]
                assert ptr_data_list[5] in expected_ptr_list_name, "Test name is not exist in database: " + \
                                                                   ptr_data_list[5]
                ptr_test_name = str(ptr_data_list[6]).split(".")[Constants.first_index]
                assert ptr_test_name in expected_ptr_test_number, "Test number is not exist in database: " + \
                                                                  ptr_test_name

                ptr_low_critical_limit = str(ptr_data_list[7])
                for expected_ptr_low_critical_limit_value in expected_ptr_low_critical_limit:
                    if expected_ptr_low_critical_limit_value == "":
                        expected_ptr_low_critical_limit_value = "0.0"

                    ptr_low_critical_limit_result = math.isclose(float(ptr_low_critical_limit),
                                                                 float(expected_ptr_low_critical_limit_value),
                                                                 rel_tol=0.1)
                    if ptr_low_critical_limit_result:
                        self.log.logger.info("PTR Low Critical Limit and Expected PTR Low Critical Limit Value "
                                             "is close ")
                        break
                    else:
                        self.log.logger.warn("PTR Low Critical Limit and Expected PTR Low Critical Limit Value "
                                             "is not close ")
                assert ptr_low_critical_limit_result, "PTR Low Critical Limit and Expected " \
                                                      "PTR Low Critical Limit Value is not close"

                ptr_high_critical_limit = str(ptr_data_list[8])
                for expected_ptr_high_critical_limit_value \
                        in expected_ptr_high_critical_limit:
                    if expected_ptr_high_critical_limit_value == "":
                        expected_ptr_high_critical_limit_value = "0.0"
                    ptr_high_critical_limit_result = math.isclose(float(ptr_high_critical_limit),
                                                                  float(expected_ptr_high_critical_limit_value),
                                                                  rel_tol=0.1)
                    if ptr_high_critical_limit_result:
                        self.log.logger.info("PTR high critical limit and expected ptr high critical limit value "
                                             "is close ")
                    else:
                        self.log.logger.warn("PTR high critical limit and expected ptr high critical limit value "
                                             "is not close ")
                assert ptr_low_critical_limit_result, "PTR Low Critical Limit and Expected " \
                                                      "PTR Low Critical Limit Value is not close"

            except AssertionError as e:
                attach(str(e), name="Test Parameter Table Error",
                       attachment_type=AttachmentType.TEXT)
                self.log.logger.error("Test Parameter Table Error" + str(e))
                assert False

    # Verify the data for test dynamic table from database after marking the file #
    def verify_the_dynamic_table(self, context, dynamic_table_values, expected_ptr_result):
        for dynamic_table_value in dynamic_table_values[Constants.first_index]:
            if type(dynamic_table_value) is decimal.Decimal:
                try:
                    pta_test_result = dynamic_table_value.normalize()
                    value = re.search('[a-zA-Z]', str(pta_test_result))
                    pta_test_result = str(pta_test_result)
                    if value != None:
                        try:
                            value = value.match()
                        except :
                            value = value.regs[0][0]
                            pta_test_result = pta_test_result.split(pta_test_result[value])[0]

                    assert pta_test_result in expected_ptr_result, "Test result is not exist in database: " \
                                                                        + pta_test_result
                except Exception as e:
                    attach(str(e), name="Dynamic Table Error",
                           attachment_type=AttachmentType.TEXT)
                    self.log.logger.warning("Dynamic Table Error" + str(e))
                    assert False

            else:
                self.log.logger.warn("Dynamic table value is not decimal")

    # Attach the table data after verification into the allure report #
    def adding_the_table_dynamic_table_result_into_the_report(self, context, file_name, expected_ptr_result):
        self.log.logger.warn("Attach the value into allure report")
        attach(str(file_name),
               name="Verified Meta Data for file :" + str(file_name),
               attachment_type=AttachmentType.TEXT)
        attach("Success",
               name="Database dynamic table",
               attachment_type=AttachmentType.TEXT)

        attach(str(expected_ptr_result),
               name="Data Verified - Test Result",
               attachment_type=AttachmentType.TEXT)

    def adding_the_test_parameter_test_result_into_the_report(self, context, file_name, lot_id, wafer_id,
                                                              die_id,
                                                              facility_name, expected_ptr_test_number,
                                                              expected_ptr_list_name,
                                                              expected_ptr_low_critical_limit,
                                                              expected_ptr_high_critical_limit):
        self.log.logger.warn("Attach the value into allure report")
        attach(str(file_name),
               name="Verified Meta Data for file :" + str(file_name),
               attachment_type=AttachmentType.TEXT)
        attach("Success",
               name="Database Tables and Data Verified",
               attachment_type=AttachmentType.TEXT)
        attach(facility_name,
               name="Database Tables Facility name",
               attachment_type=AttachmentType.TEXT)
        attach(lot_id,
               name="Database Tables Lot ID",
               attachment_type=AttachmentType.TEXT)
        attach(wafer_id,
               name="Database Tables Wafer ID",
               attachment_type=AttachmentType.TEXT)
        attach(str(die_id),
               name="Database Tables Die ID",
               attachment_type=AttachmentType.TEXT)
        attach(str(expected_ptr_test_number),
               name="Data Verified - Test Number",
               attachment_type=AttachmentType.TEXT)

        attach(str(expected_ptr_list_name),
               name="Data Verified - Test Text",
               attachment_type=AttachmentType.TEXT)
        attach(str(expected_ptr_low_critical_limit),
               name="Data Verified - Low Limit",
               attachment_type=AttachmentType.TEXT)
        attach(str(expected_ptr_high_critical_limit),
               name="Data Verified - High Limit",
               attachment_type=AttachmentType.TEXT)

    # Verify generated bin data from data base #
    def verify_generated_bin_data_from_data_base(self, context, list_data, bin_name, bin_number, wafer_id):
        self.log.logger.info("Verify generated bin data from data base")
        bin_summaries, bin_summary_field_name = DatabaseManagement.get_bin_summary_table(context, self, wafer_id, bin_name, bin_number)
        for bin_summary in bin_summaries:

            for index in range(len(bin_summary)):
                if index == 6:
                    if str(bin_summary[index]) in bin_number:
                        attach(str(bin_number),
                               name=bin_name + " bin summary field name " + str(bin_summary_field_name[index]),
                               attachment_type=AttachmentType.TEXT)
                elif bin_summary[index] in list_data:
                    attach(str(bin_summary[index]),
                           name=bin_name + " bin summary field name " + str(bin_summary_field_name[index])
                           ,
                           attachment_type=AttachmentType.TEXT)
                elif str(bin_summary[index]) in list_data:
                    attach(str(bin_summary[index]),
                           name=bin_name + " bin summary field name " + str(bin_summary_field_name[index]),
                           attachment_type=AttachmentType.TEXT)
