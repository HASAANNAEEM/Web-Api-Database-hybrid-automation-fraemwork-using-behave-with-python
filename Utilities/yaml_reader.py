import os

import yaml

from config.constants import Constants


# Read data from yml #
def data_reader(context, key):
    if "YieldWerx" in key:
        path = Constants.database_query_path
    elif "Policy" in key:
        path = Constants.create_policy_path
    elif "Login" in key:
        path = Constants.login_yml_path
    else:
        path = Constants.file_path
    with open(path) as stream:
        data_loaded = yaml.load(stream)
        data = data_loaded[key]
        return data


def data_reader_for_login(context, key):
    path = Constants.login_yml_path
    with open(path) as stream:
        data_loaded = yaml.load(stream)
        data = data_loaded[key]
        return data


# Read data from test database #
def data_reader_from_test_data(context, key):
    path = Constants.file_path
    with open(path) as stream:
        data_loaded = yaml.load(stream)
        data = data_loaded[key]
        return data


# Read data from database query #
def data_reader_from_database_query(context, key):
    path = Constants.database_query_path
    with open(path) as stream:
        data_loaded = yaml.load(stream)
        data = data_loaded[key]
        return data


# Update the data #
def data_update(context, bucket_name, key, value):
    my_path = os.path.abspath(os.path.dirname(Constants.dir_name))
    path = os.path.join(my_path, Constants.file_Path)
    with open(path) as stream:
        data_loaded = yaml.load(stream)
        data = data_loaded[bucket_name]
        data[key] = value
    with open(path, 'w') as fp:
        yaml.dump(data_loaded, fp)


#         data reader using file path
def data_reader_with_file_path(context, key, filepath):
    my_path = os.path.abspath(os.path.dirname(Constants.dir_name))
    path = os.path.join(my_path, filepath)
    with open(path) as stream:
        data_loaded = yaml.load(stream)
        data = data_loaded[key]
        return data