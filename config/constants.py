# Constants
class Constants:
    new_policy_name = ""
    first_index = 0
    starting_index = 0
    ending_index = 1200
    server_config = "local"
    marked_file_path = "marked_file_path"
    parametric_histogram_marked_file_path = "marked_parametric_file_path"
    selection_marked_file_path = "marked_selection_file_path"
    Input_Golden_file_Path = "Input_Golden_file_Path"
    access_token = ""
    source_format = "source_format"
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    payload_name = "Name"
    payload_start_at = "startsAt"
    payload_schedule = "Schedule"
    payload_step = "PolicySteps"
    payload_step_settings = "StepSettings"
    payload_source_format = "sourceFormat"
    payload_container = "container"
    payload_source_location = "sourceLocation"
    dir_name = "YieldwerxAutomation"
    file_path = "./TestData/test_data.yml"
    database_query_path = "TestData/yw_db_query.yml"
    create_policy_path = "TestData/policy.yml"
    login_yml_path = "TestData/login.yml"
    expected_execution_time = "TestData/excution_time.json"
    response = ""
    source_files_list = []
    collection_file_location_data = []
    values = []
    workflow_step = []
    marked_file_name = []
    marked_facility_name = {}
    marked_file_data = {}
    query_for_id_column = "table_id"
    query_for_all_column = "table_all_value"
    query_for_all_column_without_user = "table_all_value_without_user"
    query_for_all_id_column = "table_all_id"
    query_for_bin = "bin_summary"
    query_for_all_names = "table_all_names"
    query_for_specific_column_values = "specific_column_values"
    query_for__test_parameter_id = "test_parameter_id"
    all_tag = {"FAR", "ATR", "MIR", "MRR", "PCR", "HBR",
               "SBR", "PMR", "PGR", "PLR", "RDR", "SDR", "WIR", "WCR",
               "PIR", "PRR", "TSR", "PTR", "MPR", "FTR", "BPS", "EPS", "GDP", "DTR", "WRR", "GDR", "AUX"}


# Database Constants
class YieldWerxDataBase:
    starting_index = 0
    ending_index = 10
    yield_werx_database = "YieldWerxDataBase"
    sql_hostname = 'yw-%s.coej4rt3ls9f.us-east-1.rds.amazonaws.com'
    local_host = '127.0.0.1'
    sql_username = 'yieldwerx'
    sql_password = 'GM6bHwbiThSFLZL'
    sql_main_database = 'yieldwerx'
    sql_port = 3306
    ssh_host = 'ec2-52-1-221-148.compute-1.amazonaws.com'
    ssh_user = 'bitnami'
    ssh_port = 22
    key_path = 'TestData/DbRequirement/yieldwerx-root.pem'
    ssh_tunnel_bit = 1
    executed = False
    file = './TestData/test_data.yml'
    query_file = './TestData/yw_db_query.yml'
    connection = []
    tunnel = []
    user = ""


# Aws Credentials
class AWSCredential:
    access_key = 'AKIATKUY7SFICKW7Y7FF'
    secret_key = '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'


class DataBaseTableID:
    test_program_id = ""
    lot_id = ""
    wafer_id = ""
    die_id = ""


class PolicyVerification:

    column_value = "column_value"
    start_at = "start_at"
    task_schedule = "task_schedule"
    info_id = "info_id"
    workflow_step = "workflow_step"
    policy_step = "policy_step"
    Policy = "policy"
    id = "id"
    policy_step_id = "policy_step_id"


class RollBackTransaction:
    test_summary = "test_summary"
    wafer_id = "wafer_id"
    bin_summary = "bin_summary"
    die = "die"
    source_die_id = "source_die_id"
    null = "null"
    wafer = "wafer"
    lot_id = "lot_id"
    lot = "lot"
    test_program_revision_id = "test_program_revision_id"
    test_parameter = "test_parameter"
    test_program = "test_program"
    test_program_id = "test_program_id"
    test_program_revision = "test_program_revision"
    device_id = "device_id"
    device_family_id = "device_family_id"
    device = "device"
    device_family = "device_family"
    work_center_id = "work_center_id"
    work_center = "work_center"
    business_unit_id = "business_unit_id"
    business_unit = "business_unit"
    customer_id = "customer_id"
    customer = "customer"
    facility_id = "facility_id"
    facility = "facility"
    name = "name"
    workflow_load_file = "workflow_load_file"
    file_name = "file_name"
    policy = "policy"
    source_policy_id = "source_policy_id"
    policy_name = "ModifiedLoaderPolicyName"
    loader_load_policy_step = "loader_load_policy_step"
    policy_step_id = "policy_step_id"
    workflow_instance_id = "workflow_instance_id"
    workflow_instance = "workflow_instance"
    policy_id = "policy_id"
    file_location = "file_location"
    container = "container"
    container_name = "yw-loader-2"
    workflow_step = "workflow_step"
    policy_step = "policy_step"
    Policy = "policy"
    id = "id"


class RollBackTransactionConverter:
    null = "null"
    source_policy_id = "source_policy_id"
    workflow_load_file = "workflow_load_file"
    file_name = "file_name"
    policy_name = "ModifiedConverterPolicyName"
    loader_load_policy_step = "loader_converter_policy_step"
    policy_step_id = "policy_step_id"
    policy_id = "policy_id"
    file_location = "file_location"
    container = "container"
    container_name = "yw-rawfile-1"
    workflow_step = "workflow_step"
    workflow_instance = "workflow_instance"
    policy_step = "policy_step"
    Policy = "policy"
    id = "id"


class MongoDB:
    expected_data_collection = "expected_legend_histo"

