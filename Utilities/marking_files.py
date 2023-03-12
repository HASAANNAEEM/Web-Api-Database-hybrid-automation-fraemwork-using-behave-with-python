import logging
import os
import random

from Utilities import yaml_reader
from Utilities.log import Logger
from config.constants import Constants
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))


# Marking the file for loader #
def file_marking(context, feature_name, policy_name, file_path, tag_name, mark_file_path):
    file_data = []
    data = yaml_reader.data_reader_from_test_data(context, policy_name)
    filename = file_path.split("/")
    filename = filename[len(filename)-1]
    Constants.marked_file_name.append(filename)
    Constants.marked_file_data[filename] = []
    # createdPath = data[mark_file_path] + filename[len(filename)-1]
    createdPath = os.getcwd()+'/'+data[mark_file_path] + filename
    log.logger.info(createdPath+"++++++++")
    created_file = open(createdPath, "w")
    new_list = []
    new_list = remove_multiple_line_tags(context, file_path, new_list)
    for line in new_list:
        expected_value = str(line).split("|")
        value2 = expected_value[0]
        for value in tag_name.split(","):
            if value in value2:
                if value == "MIR":
                    file_data.append(mark_mir(context, feature_name, filename, expected_value))
                elif value == "WIR":
                    file_data.append(mark_wir(context, expected_value, value))
                else:
                    file_data.append(mark_wrr(context, expected_value, value))
                break
        joined_string = "|".join(expected_value)
        created_file.writelines(joined_string+"\n")
    if len(file_data) > 0:
        Constants.marked_file_data[filename].append(file_data)


# Mark the mir tag #
def mark_mir(context, feature_name, filename, expected_value):
    marked_data_for_mir = []
    FirstIndexValue = expected_value[0]
    expected_value[0] = FirstIndexValue + " LOT ID Test"
    marked_data_for_mir.append(expected_value[0])
    SecondIndexValue = expected_value[1]
    expected_value[1] = SecondIndexValue + " Part Type Test"
    marked_data_for_mir.append(expected_value[1])
    ThirdIndexValue = expected_value[2]
    expected_value[2] = ThirdIndexValue + " Job Name Test"
    marked_data_for_mir.append(expected_value[2])
    TwelveIndexValue = expected_value[11]
    expected_value[11] = TwelveIndexValue + " Test Code Test"
    marked_data_for_mir.append(expected_value[11])
    TwentySixIndexValue = expected_value[25]
    expected_value[25] = TwentySixIndexValue + " Test " + feature_name + " " + str(random.randint(0, 2000))
    Constants.marked_facility_name[filename] = expected_value[25]
    marked_data_for_mir.append(expected_value[25])
    attach(str(expected_value[25]), name="Facility name"
           , attachment_type=AttachmentType.TEXT)
    return marked_data_for_mir


# Mark the wir tag #
def mark_wir(context, expected_value, value):
    marked_data_for_wir = []
    FourthIndexValue = expected_value[3].split("\n")[0]
    expected_value[3] = FourthIndexValue + " Wafer ID Test"
    marked_data_for_wir.append(value + ":" + expected_value[3])
    return marked_data_for_wir


# Mark the wrr tag #
def mark_wrr(context, expected_value, value):
    marked_data_for_wrr = []
    FourthIndexValue = expected_value[3]
    expected_value[3] = FourthIndexValue + " Wafer ID Test"
    marked_data_for_wrr.append(value + ":" + expected_value[3])
    return marked_data_for_wrr


# Create the list of tag in a single line #
def remove_multiple_line_tags(context, filename, new_list):
    with open(filename) as f:
        for line in f:
            expected_value = str(line).split("|")
            value2 = expected_value[0].split(":")[0]

            if value2 in Constants.all_tag:
                new_list.append(line.strip())

            else:
                new_list[-1] += line.strip()

        return new_list
