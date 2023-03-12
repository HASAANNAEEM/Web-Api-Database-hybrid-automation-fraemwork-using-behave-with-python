import json
from datetime import datetime
from datetime import timedelta
import logging
from Utilities.log import Logger
import pytz
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Utilities import yaml_reader
from config.constants import Constants

current_time = datetime.now()

log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))


# Update the current time, policy name and bucket name in payload #
def payload_update(context, payload_path, policy_name, new_policy_name, bucket_name):
    source_location = bucket_name
    dataApi = yaml_reader.data_reader_from_test_data(context, policy_name)
    json_file_path = dataApi[payload_path]
    with open(json_file_path) as json_data:
        data = json.load(json_data)
    if Constants.source_format in data:
        source_format = dataApi[Constants.source_format]
        data[Constants.payload_step][0][Constants.payload_step_settings][
            Constants.payload_source_format] = source_format
    future_time = datetime.now() + timedelta(minutes=0.5)
    log.logger.info("Future date time : " + str(future_time))
    attach(str(future_time), name="Future date time for policy"
           , attachment_type=AttachmentType.TEXT)
    future_datetime = future_time.astimezone(pytz.UTC).strftime(Constants.date_format)
    f_datetime = future_datetime.split(' ')
    future_time_str = f_datetime[0] + "T" + f_datetime[1] + "Z"
    data[Constants.payload_name] = new_policy_name
    data[Constants.payload_schedule][Constants.payload_start_at] = future_time_str
    data[Constants.payload_step][0][Constants.payload_step_settings][
        Constants.payload_source_location][Constants.payload_container] = source_location
    with open(json_file_path, 'w') as fp:
        json.dump(data, fp)
    return data


def payload_update_for_selection_criteria(context, payload_path, policy_name, facility_list, work_center_list,
                                          device_list, test_program_list, test_program_revision, lot_list, wafer_list,
                                          test_parameter_list
                                          ):
    entity_value = "values"
    dataApi = yaml_reader.data_reader_from_test_data(context, policy_name)

    json_file_path = dataApi[payload_path]
    with open(json_file_path) as json_data:
        data = json.load(json_data)
    value = data[0][entity_value]
    data[0][entity_value] = facility_list
    data[1][entity_value] = work_center_list
    data[2][entity_value] = device_list
    data[3][entity_value] = test_program_list
    data[4][entity_value] = test_program_revision
    data[5][entity_value] = lot_list
    data[6][entity_value] = wafer_list
    data[7][entity_value] = test_parameter_list
    return data


# Update the current time, policy name and bucket name in payload #
def payload_update_with_checkbox(context, payload_path, policy_name, new_policy_name, checkbox, bucket_name):
    source_location = bucket_name
    dataApi = yaml_reader.data_reader_from_test_data(context, policy_name)
    json_file_path = dataApi[payload_path]
    comma = ","
    with open(json_file_path) as json_data:
        data = json.load(json_data)
    if Constants.source_format in data:
        source_format = dataApi[Constants.source_format]
        data[Constants.payload_step][0][Constants.payload_step_settings][
            Constants.payload_source_format] = source_format
    checkbox_list = checkbox
    if 'readHbr' in checkbox_list:
        data[Constants.payload_step][0][Constants.payload_step_settings]["readHbr"] = True
    else:
        data[Constants.payload_step][0][Constants.payload_step_settings]["readHbr"] = False
    if "readSbr" in checkbox_list:
        data[Constants.payload_step][0][Constants.payload_step_settings]["readSbr"] = True
    else:
        data[Constants.payload_step][0][Constants.payload_step_settings]["readSbr"] = False
    if "readTsr" in checkbox_list:
        data[Constants.payload_step][0][Constants.payload_step_settings]["readTsr"] = True
    else:
        data[Constants.payload_step][0][Constants.payload_step_settings]["readTsr"] = False
    if "generateHbr" in checkbox_list:
        data[Constants.payload_step][0][Constants.payload_step_settings]["generateHbr"] = True
    else:
        data[Constants.payload_step][0][Constants.payload_step_settings]["generateHbr"] = False

    if "generateSbr" in checkbox_list:
        data[Constants.payload_step][0][Constants.payload_step_settings]["generateSbr"] = True
    else:
        data[Constants.payload_step][0][Constants.payload_step_settings]["generateSbr"] = False
    if "generateTsr" in checkbox_list:
        data[Constants.payload_step][0][Constants.payload_step_settings]["generateTsr"] = True
    else:
        data[Constants.payload_step][0][Constants.payload_step_settings]["generateTsr"] = False
    future_time = datetime.now() + timedelta(minutes=0.5)
    log.logger.info("Future date time : " + str(future_time))
    attach(str(future_time), name="Future date time for policy"
           , attachment_type=AttachmentType.TEXT)
    future_datetime = future_time.astimezone(pytz.UTC).strftime(Constants.date_format)
    f_datetime = future_datetime.split(' ')
    future_time_str = f_datetime[0] + "T" + f_datetime[1] + "Z"
    data[Constants.payload_name] = new_policy_name
    data[Constants.payload_schedule][Constants.payload_start_at] = future_time_str
    data[Constants.payload_step][0][Constants.payload_step_settings][
        Constants.payload_source_location][Constants.payload_container] = source_location
    with open(json_file_path, 'w') as fp:
        json.dump(data, fp)
    return data
