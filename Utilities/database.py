import time

from Helpers.db_config import DataBaseConfig
from Helpers.test_db import MongoDb
from config.constants import Constants

database_config = DataBaseConfig()
mongoDb = MongoDb()


def get_id(context, table_name, table_column_condition, table_condition):
    return database_config.run_query_to_get_id(context, Constants.query_for_id_column, table_name, table_column_condition,
                                               table_condition)[0]


def get_test_parameter_id_with_name(context, table_name, table_column_condition, table_condition, name, value):
    return database_config.run_query_to_get_test_parameter_id(context, Constants.query_for__test_parameter_id, table_name,
                                                              table_column_condition, table_condition, name, value)[0][
        0]


def get_test_parameter_id(context, table_name, table_column_condition, table_condition):
    return database_config.run_query_to_get_test_parameter_id(context, Constants.query_for__test_parameter_id, table_name,
                                                              table_column_condition, table_condition)[0][0]


def get_all_id(context, table_name, table_column_condition, table_condition):
    return database_config.run_query_to_get_ids(context, Constants.query_for_all_id_column, table_name, table_column_condition,
                                               table_condition)


def get_all_names(context, field_name, table_name, condition, value):
    return database_config.run_query_to_get_specific_data_against_column(context, Constants.query_for_specific_column_values,
                                                                         field_name, table_name, condition, value)


def get_all_column(context, table_name, table_column_condition, table_condition):
    return database_config.run_query_to_get_all_data(context, Constants.query_for_all_column, table_name, table_column_condition,
                                                     table_condition)


def get_all_column_without_user(context, table_name, table_column_condition, table_condition):
    return database_config.run_query_to_get_all_data_without_user(context, Constants.query_for_all_column_without_user, table_name,
                                                     table_column_condition,
                                                     table_condition)


def get_all_column_value_and_name(context, table_name, table_column_condition, table_condition):
    return database_config.run_query_to_get_all_data_and_field_name(context, Constants.query_for_all_column, table_name,
                                                                    table_column_condition,
                                                                    table_condition)


def get_all_column_value_and_name_for_bin(context, table_name, table_column_condition, table_condition, bin_record_type
                                          , bin_record_type_value
                                          , bin_number, bin_number_value):
    return database_config.run_query_to_get_all_data_and_field_name_with_multiple_parameter(context, Constants.query_for_bin
                                                                                            , table_name
                                                                                            , table_column_condition
                                                                                            , table_condition
                                                                                            , bin_record_type
                                                                                            , bin_record_type_value
                                                                                            , bin_number,
                                                                                            bin_number_value)


def get_facility_name(context, file_name):
    mongoDb.connect_mongo(context)
    data = mongoDb.read_value(context, "Marking_file", file_name)
    value = data['Data'].split(",")[4]
    return value.split("\'")[1]


def get_test_program_revision_id(context, test_program_id):
    return get_id(context, "test_program_revision", "test_program_id", test_program_id)


def get_facility_id(context, facility_name):
    return get_id(context, "facility", "name", facility_name)


def get_customer_id(context, facility_id):
    return get_id(context, "customer", "facility_id", facility_id)


def get_business_unit_id(context, customer_id):
    return get_id(context, "business_unit", "customer_id", customer_id)


def get_work_center_id(context, business_unit_id):
    return get_id(context, "work_center", "business_unit_id", business_unit_id)


def get_device_family_id(context, work_center_id):
    return get_id(context, "device_family", "work_center_id", work_center_id)


def get_device_id(context, device_family_id):
    return get_id(context, "device", "device_family_id", device_family_id)


def get_test_program_id(context, device_id):
    return get_id(context, "test_program", "device_id", device_id)


def get_test_parameter(context, test_program_id):
    return get_all_column(context, "test_parameter", "test_program_revision_id",
                          test_program_id)


def get_test_parameter_id(context, test_program_id, name):
    return get_test_parameter_id_with_name(context, "test_parameter", "test_program_revision_id",
                                           test_program_id, "name", name)


def get_test_parameter_ids(context, test_program_id):
    return get_all_id(context, "test_parameter", "test_program_revision_id",
                      test_program_id)


# def get_test_parameter_ids(context, test_program_id):
#     return get_all_id(context, "test_parameter", "test_program_revision_id",
#                       test_program_id)

def get_lot_id(context, test_program_id):
    return get_id(context, "lot", "test_program_revision_id",
                  test_program_id)


def get_wafer_id(context, lot_id):
    return get_id(context, "wafer", "lot_id",
                  lot_id)


def get_wafer_ids(context, lot_id):
    return get_all_id(context, "wafer", "lot_id",
                      lot_id)


def get_policy_id(context, name):
    return get_id(context, "policy", "name",
                  name)


def get_policy_ids(context, name):
    return get_all_id(context, "policy", "name",
                      name)


def get_policy_step_id(context, policy_id):
    return get_id(context, "policy_step", "policy_id",
                  policy_id)


def get_work_flow_step_id(context, policy_step_id):
    return get_all_id(context, "workflow_step", "policy_step_id",
                      policy_step_id)


def get_task_schedule_id(context, policy_id):
    return get_id(context, "task_schedule", "info_id",
                  policy_id)


def get_policy_step_ids(context, policy_id):
    return get_all_id(context, "policy_step", "policy_id",
                      policy_id)


def get_test_summary(context, test_parameter_id):
    return get_all_column_value_and_name(context, "test_summary", "test_parameter_id",
                                         test_parameter_id)


def get_test_summary_against_wafer_id(context, wafer_id):
    return get_all_column_value_and_name(context, "test_summary", "wafer_id",
                                         wafer_id)


def get_bin_summary(context, wafer_id, bin_record_type_value, bin_number_value):
    return get_all_column_value_and_name_for_bin(context, "bin_summary", "wafer_id",
                                                 wafer_id, "bin_record_type", bin_record_type_value, "bin_number",
                                                 bin_number_value)


def get_die_id(context, wafer_id):
    return get_all_id(context, "die", "wafer_id",
                      wafer_id)


def get_dynamic_table_value(context, dynamic_table_name, die_id):
    return get_all_column_without_user(context, dynamic_table_name, "die_id", die_id)


def get_table_columns_name_against_facility_name(context, facility_name):
    test_parameter_name_list = []
    work_center_list = []
    device_list = []
    test_program_list = []
    test_program_revision_list = []
    lot_list = []
    wafer_list = []
    facility_id = get_id(context, "facility", "name", facility_name)
    customer = get_all_column(context, "customer", "facility_id", facility_id)
    business_unit = get_id(context, "business_unit", "customer_id", customer[0][0])
    work_center = get_all_column(context, "work_center", "business_unit_id", business_unit)

    work_center_list.append(work_center[0][5])
    device_family = get_id(context, "device_family", "work_center_id", work_center[0][0])
    device = get_all_column(context, "device", "device_family_id", device_family)
    device_list.append(device[0][5])
    test_program = get_all_column(context, "test_program", "device_id", device[0][0])
    test_program_list.append(test_program[0][5])
    test_program_revision = get_all_column(context, "test_program_revision", "test_program_id", test_program[0][0])
    test_program_revision_list.append(test_program[0][5])
    test_parameters = get_all_column(context, "test_parameter", "test_program_revision_id", test_program_revision[0][0])
    for test_parameter in test_parameters:
        test_parameter_name_list.append(test_parameter[5])
    lot = get_all_column(context, "lot", "test_program_revision_id",
                         test_program_revision[0][0])
    lot_list.append(lot[0][13])
    wafers = get_all_column(context, "wafer", "lot_id", lot[0][0])
    for wafer in wafers:
        wafer_list.append(wafer[24])

    return test_parameter_name_list, work_center_list, device_list, test_program_list, \
           test_program_revision_list, lot_list, wafer_list


def get_die_all_data(context, wafer_id):
    return get_all_column(context, "die", "wafer_id",
                          wafer_id)
