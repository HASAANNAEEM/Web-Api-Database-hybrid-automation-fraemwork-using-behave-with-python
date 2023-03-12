import decimal
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Utilities import yaml_reader
import os
from datetime import datetime
from Utilities.log import Logger
import logging

from Helpers import database_helper

log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))


# Extracting file from target line location#
def extract_file_bucket_name(context, target_link):
    file_loc = target_link.split("/")
    final_file_name = file_loc[3]
    final_bucket = file_loc[2]
    return final_bucket, final_file_name


# Compare file for converter and create a new identical and difference file #
def compare_files(context, policy_name, source_file_name, golden_file_path, downloaded_file_path, identical_file_path,
                  different_lines_file_path):
    try:
        ignore_collection = "ignore_field"
        collection_lists = database_helper.get_all_data_from_testDB(context, ignore_collection)
        list_with_key_values = get_data_with_key(context, collection_lists)
        data = yaml_reader.data_reader_from_test_data(context, policy_name)
        dot = "."
        golden_file_path = data[golden_file_path]
        newly_atdf_file_path = data[downloaded_file_path]
        identical_file_path = data[identical_file_path]
        different_file_path = data[different_lines_file_path]
        source_file_name = str(source_file_name).split(dot)[0]
        file_gold, golden_file_path_name = get_golden_files_across_newly_atdf_files(context, golden_file_path, source_file_name)
        file_Identical, file_Difference, newly_file_path, file_Newly = create_file_for_identical_and_difference_file(context,
            newly_atdf_file_path, source_file_name, identical_file_path, different_file_path)
        log.logger.info("Comparing files ", " @ " + 'file1.txt', " # " + 'file2.txt', '\n')
        golden_file_line = file_gold.readlines()
        newly_file_line = file_Newly.readlines()
        skip_line = []
        for line_no in range(len(golden_file_line)):
            file_line, file2_line, skip_line = getting_same_line(context, line_no, file_Difference, golden_file_line,
                                                                 newly_file_line, skip_line)
            try:
                log.logger.info("Difference Lines in Both files")
                if file2_line != "":
                    line_by_line_comparison(context, list_with_key_values, file_line, file2_line, line_no, file_Difference,
                                            file_Identical)
                else:
                    log.logger.warn("Line is skipped from newly generated file")
            except Exception as e:
                log.logger.error("Error in compare the file " + str(e))
                assert False

            finally:
                file_gold.close()
                file_Newly.close()
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


# Getting golden file across newly generated atdf file #
def get_golden_files_across_newly_atdf_files(context, golden_file_path, source_file_name):
    try:
        all_golden_files_in_directory = os.listdir(golden_file_path)

        for golden_file in all_golden_files_in_directory:
            # Checking if the Golden file Exists across the Newly generated in directory and open the matching file
            if source_file_name in golden_file:
                golden_file_path_name = golden_file_path + golden_file
                file_gold = open(golden_file_path_name, "r")
        return file_gold, golden_file_path_name
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


# Compare the file line by line #
def line_by_line_comparison(context, list_with_key_values, golden_file_line, newly_file_line, line_no, file_difference,
                            file_identical):
    try:
        expected_value = ""
        index_eight = 8
        index_four = 4
        pipeline = "|"
        test_parameter = "PTR"
        value = str(golden_file_line).split(pipeline)
        if golden_file_line.lower() != newly_file_line.lower():
            value2 = str(newly_file_line).split(pipeline)
            if bool(compare_after_ignore_dynamic_value(context, list_with_key_values, value, value2)):
                expected_value = value
            else:
                for index in range(len(value)):
                    if bool(is_date(context, value[index])):
                        # Skip date
                        pass
                    elif value[index].isdigit() or isfloat(context, value[index]):
                        # Remove trailing zero
                        expected_value = remove_trailing_zeros(context, index, value, value2, expected_value)
                    elif value[index] != value2[index]:
                        if test_parameter in value[0]:
                            if index == index_eight or index == index_four:
                                # Compare P and F flag of ptr tag on two different indexes
                                expected_value = look_for_pass_flag(context, index, value, value2, expected_value)
                        else:
                            log.logger.info("Line ", str(line_no), ":")
                            file_difference.writelines(golden_file_line)
                            file_difference.writelines(newly_file_line)
                            file_difference.writelines("Difference on Line no " + str(line_no))
                            log.logger.info("\tGolden file:", golden_file_line)
                            log.logger.info("\tNewly file:", newly_file_line)
                            attach(str(golden_file_line), name="Difference in files", attachment_type=AttachmentType.TEXT)
                            break
        else:
            expected_value = value

        write_output_files(context, expected_value, golden_file_line, newly_file_line, file_identical, file_difference, line_no)
    except Exception as e:
        print(e)
    except TypeError as e:
        print(e)


# Writing the output files #
def write_output_files(context, expected_value, golden_file_line, newly_file_line, file_identical, file1_difference, line_no):
    try:
        if expected_value != "":
            joined_string = "|".join(expected_value)
            joined_string = joined_string
            if golden_file_line in joined_string:
                file_identical.writelines(joined_string)
                expected_value = []
            else:
                file1_difference.writelines(golden_file_line)
                file1_difference.writelines(newly_file_line)
                file1_difference.writelines("Difference on Line no " + str(line_no))
                log.logger.info("\tgolden file line :", newly_file_line)
                log.logger.info("\tnewly generated file line:", newly_file_line)
                expected_value = []
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


# Removing trailing zeros #
def remove_trailing_zeros(context, index, value, value2, expected_value):
    try:
        value_line_1 = decimal.Decimal(value[index]).normalize()
        value_line_2 = decimal.Decimal(value2[index]).normalize()
        if value_line_1 == value_line_2:
            expected_value = value
        else:
            expected_value = value2

        return expected_value
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


# Ignore the data #
def is_date(context, date):
    try:
        datetime.strptime(date, '%H:%M:%S %d-%b-%Y')
        return True
    except Exception as e:
        log.logger.error("Date warning" + str(e))
        return False


# Compare the flag for index 8 and 4 #
def look_for_pass_flag(context, index, value, value2, expected_value):
    try:
        if index == 8:
            value[index].lower() == value2[4].lower()
        elif index == 4:
            value2[4].lower() == value2[8].lower()
        return value
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


# Create identical and difference file #
def create_file_for_identical_and_difference_file(context, newly_atdf_file_path, source_file_name, identical_file_path,
                                                  different_file_path):
    try:
        files_and_directories = os.listdir(newly_atdf_file_path)
        for file in files_and_directories:
            if source_file_name in file:
                newly_file_path = newly_atdf_file_path + file
                file_Newly = open(newly_file_path, "r")
                file1 = file.split(".")
                identical_filename = identical_file_path + file1[0] + ".txt"
                difference_filename = different_file_path + file1[0] + ".txt"

        file_Identical = open(identical_filename, "w")
        file1_Difference = open(difference_filename, "w")
        return file_Identical, file1_Difference, newly_file_path, file_Newly
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


# Compare after ignore dynamic value#
def compare_after_ignore_dynamic_value(context, ignore_field, value, value2):
    try:
        golden_value = ""
        newly_generated_value = ""
        for key in ignore_field.keys():

            if key in value2[0]:
                for index in range(len(value)):
                    if str(index) not in ignore_field[key]:
                        if golden_value == "":
                            golden_value = value[index]
                            newly_generated_value = value2[index]
                        else:
                            golden_value = golden_value + "|" + value[index]
                            newly_generated_value = newly_generated_value + "|" + value2[index]

            if golden_value == newly_generated_value:
                return True
            elif golden_value != newly_generated_value:

                return False
            else:
                return True
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


def get_data_with_key(context, collection_lists):
    try:
        list_with_key_values = {}
        for collection_list in collection_lists:
            key_list = collection_list['Key'].split(",")
            data_list = collection_list['Data'].split(",")
            data_list_value = []
            for source_file in data_list:
                data_source_file = source_file.replace("[", "").replace("'", "").replace("]", "")
                source_file = data_source_file.split(",")[0]
                source_file = source_file.replace("[", "").replace("'", "").replace(" ", "")
                data_list_value.append(source_file)
            list_with_key_values[key_list[0]] = data_list_value
        return list_with_key_values
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


def isfloat(context, num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# Getting the same line from both line #
def getting_same_line(context, line_no, file_Difference, golden_file_line, newly_file_line, skip_line):
    try:
        pipeline = "|"
        index = line_no
        line_1 = golden_file_line[line_no]
        for skin_line_no in range(len(skip_line)):
            index = index - 1
        line_2 = newly_file_line[index]
        value = str(line_1).split(pipeline)
        value2 = str(line_2).split(pipeline)

        if "PRR" in value2[0]:
            line_2 = newly_file_line[index]
        else:

            while True:
                if value[0] != value2[0]:
                    if "MRR" in value[0]:
                        break
                    else:

                        index += 1
                        line_2 = newly_file_line[index]
                        value2 = str(line_2).split(pipeline)
                        if "PRR" in value2[0]:
                            break

                else:
                    break
            if "PRR" in value2[0]:
                skip_line.append(line_1)
                line_2 = ""
                file_Difference.writelines(line_1)
                file_Difference.writelines("Line no " + str(line_no) + " is not present in new downloaded file\n")
                log.logger.info("Line no " + str(line_no) + " is not present in new downloaded file")

        return line_1, line_2, skip_line
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
