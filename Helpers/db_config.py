import json
import logging
from config.constants import YieldWerxDataBase
from config.constants import Constants
import MySQLdb
import sshtunnel
from Utilities import yaml_reader
from Utilities.log import Logger
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
yield_werx_variable = YieldWerxDataBase()


class DataBaseConfig:
    def __init__(self):

        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))
        self.query_data = yaml_reader.data_reader(self, "YieldWerxDataBase")
    sql_hostname = ""
    sql_host = ""
    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0
    connection = yield_werx_variable.connection
    tunnel = yield_werx_variable.tunnel
    sql_username = YieldWerxDataBase.sql_username
    sql_password = YieldWerxDataBase.sql_password
    sql_main_database = YieldWerxDataBase.sql_main_database
    sql_port = YieldWerxDataBase.sql_port
    ssh_host = YieldWerxDataBase.ssh_host
    ssh_user = YieldWerxDataBase.ssh_user
    ssh_port = YieldWerxDataBase.ssh_port
    key_path = YieldWerxDataBase.key_path
    ssh_tunnel_bit = YieldWerxDataBase.ssh_tunnel_bit
    executed = YieldWerxDataBase.executed
    file = YieldWerxDataBase.file
    query_file = YieldWerxDataBase.query_file

    # Connect to yield-werx database #
    def connect_yw_db(self, context):
        env = context.config.userdata['env']
        self.sql_hostname = YieldWerxDataBase.sql_hostname % env
        platform = context.config.userdata['platform']
        if "aws" in platform:
            self.sql_host = self.sql_hostname
            YieldWerxDataBase.user = "qa"
        else:
            self.sql_host = YieldWerxDataBase.local_host
            YieldWerxDataBase.user = "ktm"
        try:
            count = YieldWerxDataBase.starting_index
            while True:
                if count < YieldWerxDataBase.ending_index:
                    try:
                        if "aws" in platform:
                            self.log.logger.info("Connect with aws")
                            self.mysql_connect_aws(context)
                        else:
                            self.open_ssh_tunnel(context)
                            self.mysql_connect(context)
                        # time_out = 100000
                        # self.connection[Constants.first_index].callTimeout = time_out
                        break

                    except Exception as e:
                        count += 1
                        self.log.logger.error("Yield-werx Database connection issue "+str(e))

                else:
                    assert False, "Connection to DB not established : "+str(e)
        except Exception as e:
            self.log.logger.error("Error connection to DB not established")
            attach(str(e), name="Error connection to DB not established"
                   , attachment_type=AttachmentType.TEXT)
            assert False, e

        except AssertionError as ex:
            self.log.logger.error("Error connection to DB not established")
            attach(str(ex), name="Assertion error connection to DB not established"
                   , attachment_type=AttachmentType.TEXT)
            assert False, ex

    def open_ssh_tunnel(self, context):
        tunnel_connection = sshtunnel.SSHTunnelForwarder(
                (self.ssh_host, 22),
                ssh_username=self.ssh_user, ssh_pkey=self.key_path,
                remote_bind_address=(self.sql_hostname, self.sql_port)
            )
        self.log.logger.info("tunnel_connection")
        tunnel_connection.start()
        self.tunnel.clear()
        self.tunnel.append(tunnel_connection)

    def mysql_connect(self, context):
        db_connection = MySQLdb.connect(
            user=self.sql_username,
            passwd=self.sql_password,
            host=self.sql_host, port=self.tunnel[Constants.first_index].local_bind_port,
            db=self.sql_main_database,
        )
        self.log.logger.info("db_connection")
        self.log.logger.info(db_connection)
        self.connection.clear()
        self.connection.append(db_connection)
        return db_connection

    def mysql_connect_aws(self, context):
        db_connection = MySQLdb.connect(
            user=self.sql_username,
            passwd=self.sql_password,
            host=self.sql_host, port=self.sql_port,
            db=self.sql_main_database,
        )
        self.log.logger.info("db_connection")
        self.log.logger.info(db_connection)
        self.connection.clear()
        self.connection.append(db_connection)
        return db_connection

    def run_query(self, context, query_data_source, key, value):
        self.log.logger.info(YieldWerxDataBase.user)
        query_data = yaml_reader.data_reader(context, query_data_source)
        connection = self.connection[Constants.first_index]
        cursor = connection.cursor()
        query = query_data[key]
        query_data = query % (value, YieldWerxDataBase.user)
        self.log.logger.info(query_data)
        cursor.execute(query_data)
        query_result = cursor.fetchall()
        self.log.logger.info(query_result)
        return query_result

    def run_query_for_work_flow(self, context, query_data_source, key, value1, value2):
        self.log.logger.info(YieldWerxDataBase.user)
        query_data = yaml_reader.data_reader(context, query_data_source)
        connection = self.connection[Constants.first_index]
        cursor = connection.cursor()
        query = query_data[key]
        query_data = query % (value1, value2, YieldWerxDataBase.user)
        self.log.logger.info(query_data)
        cursor.execute(query_data)
        query_result = cursor.fetchall()
        self.log.logger.info(query_result)
        return query_result

    def run_query_from_database_query(self, context, query_for, key, value):
        query_data = yaml_reader.data_reader(context, query_for)
        cursor = self.connection[Constants.first_index].cursor()
        cursor.execute(query_data[key], (value,YieldWerxDataBase.user))
        return cursor.fetchall()

    def run_query_for_converter_query(self,  context,  policy_name, key, value):
        self.connect_yw_db(context)
        converter_data = yaml_reader.data_reader(context, policy_name)
        cursor = self.connection.cursor()
        cursor.execute(converter_data[key], (value,YieldWerxDataBase.user))
        return cursor.fetchall()

    def run_query_to_get_id(self, context, query, table_name, condition, value):
        try:
            cursor = self.connection[Constants.first_index].cursor()
        except Exception as e:
            self.connect_yw_db(context)
            cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[query]
        query = query % (table_name, condition, value, YieldWerxDataBase.user)
        try:
            cursor.execute(query)
            query_result = cursor.fetchone()
        except Exception as e:
            self.log.logger.error("run Query Error" + str(e))
            assert False
        return query_result

    def run_query_to_get_ids(self, context, query, table_name, condition, value):
        try:
            cursor = self.connection[Constants.first_index].cursor()
        except Exception as e:
            self.connect_yw_db(context)
            cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[query]
        query = query % (table_name, condition, value, YieldWerxDataBase.user)
        try:
            cursor.execute(query)
            query_result = cursor.fetchall()
        except Exception as e:
            self.log.logger.error("run Query Error" + str(e))
            assert False
        return query_result

    def run_query_to_get_test_parameter_id(self, context, query, table_name, condition, value, name, name_value):

        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[query]
        query = query % (table_name, condition, value, name, name_value, YieldWerxDataBase.user)
        try:
            cursor.execute(query)
        except Exception as e:
            self.log.logger.error("run Query Error" + str(e))
            assert False
        return cursor.fetchall()

    def run_query_to_get_specific_data(self, context, key, field_name, table_name, condition, value):
        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[key]
        query = query % (field_name, table_name, condition, value, YieldWerxDataBase.user)
        try:
            cursor.execute(query)
        except Exception as e:
            self.log.logger.error("run Query Error"+str(e))
            assert False
        return cursor.fetchone()

    def run_query_to_get_specific_data_without_user_id(self, context, key, field_name, table_name, condition, value):
        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[key]
        query = query % (field_name, table_name, condition, value)
        try:
            cursor.execute(query)
        except Exception as e:
            self.log.logger.error("run Query Error" + str(e))
            assert False
        return cursor.fetchone()

    def run_query_to_get_min_max_value_data(self, context, key, wafer_id):
        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[key]
        query = query % wafer_id
        try:
            cursor.execute(query)
        except Exception as e:
            self.log.logger.error("run Query Error"+str(e))
            assert False
        return cursor.fetchone()

    def run_query_to_get_die_count_data(self, context, key, wafer_id, start, end):
        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[key]
        query = query % (wafer_id, start, end, YieldWerxDataBase.user)
        try:
            cursor.execute(query)
        except Exception as e:
            self.log.logger.error("run Query Error"+str(e))
            assert False
        return cursor.fetchone()

    def run_query_to_get_specific_data_against_column(self, context, query, field_name, table_name, condition, value):
        cursor = self.connection[Constants.first_index].cursor()
        query = query % (field_name, table_name, condition, value, YieldWerxDataBase.user)
        try:
            cursor.execute(query)
        except Exception as e:
            self.log.logger.error("run Query Error"+str(e))
            assert False
        return cursor.fetchall()

    def run_query_to_get_all_data(self, context, key, table_name, condition, value):

        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[key]
        query = query % (table_name, condition, value, YieldWerxDataBase.user)
        try:
            cursor.execute(query)

        except Exception as e:
            self.log.logger.error("run Query Error"+str(e))
            assert False
        return cursor.fetchall()

    def run_query_to_get_all_data_without_user(self, context, key, table_name, condition, value):

        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[key]
        query = query % (table_name, condition, value)
        try:
            cursor.execute(query)

        except Exception as e:
            self.log.logger.error("run Query Error"+str(e))
            assert False
        return cursor.fetchall()

    def run_query_to_get_all_data_and_field_name(self, context, key, table_name, condition, value):
        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[key]
        query = query % (table_name, condition, value, YieldWerxDataBase.user)
        try:
            cursor.execute(query)
            field_names = [i[Constants.first_index] for i in cursor.description]
        except Exception as e:
            self.log.logger.error("run Query Error"+str(e))
            assert False
        return cursor.fetchall(), field_names

    def run_query_to_get_all_data_and_field_name_with_multiple_parameter(self, context, key, table_name, condition, value,
                                                                         bin_record_type,
                                                                         bin_record_type_value,
                                                                         bin_number,
                                                                         bin_number_value):
        cursor = self.connection[Constants.first_index].cursor()
        query = self.query_data[key]
        query = query % (table_name, condition, value, bin_record_type, bin_record_type_value, bin_number,
                         bin_number_value, YieldWerxDataBase.user)
        try:
            cursor.execute(query)
            field_names = [i[Constants.first_index] for i in cursor.description]
        except Exception as e:
            self.log.logger.error("run Query Error"+str(e))
            assert False
        return cursor.fetchall(), field_names

    def close_yw_connection(self, context):
        self.connection[Constants.first_index].close()
        self.tunnel[Constants.first_index].close()

    def run_query_to_delete_file(self, context, table_name, condition, value):
        count = Constants.first_index
        try:
            cursor = self.connection[Constants.first_index].cursor()
        except Exception as e:
            self.connect_yw_db(context)
            cursor = self.connection[Constants.first_index].cursor()
        query = f"delete from %s where %s = '%s' and created_by_id = (select id from user where user_name = '%s')"
        query = query % (table_name, condition, value, YieldWerxDataBase.user)
        while True:
            if count < 3:
                try:
                    cursor.execute(query)
                    self.connection[Constants.first_index].commit()
                    assert True
                    break
                except Exception as e:
                    self.log.logger.error("run Query Error" + str(e))
                    count += 1
            else:
                self.log.logger.error("No data is present in " + table_name)
                break

    def run_query_to_delete_workflow_load_table_data(self, context, table_name, condition, value1, value2):
        count = Constants.first_index
        try:
            cursor = self.connection[Constants.first_index].cursor()
        except Exception as e:
            self.connect_yw_db(context)
            cursor = self.connection[Constants.first_index].cursor()
        query = f"delete from %s where %s = '%s' and workflow_step_id = '%s' and created_by_id = (select id from user where user_name = '%s')"
        query = query % (table_name, condition, value1, value2, YieldWerxDataBase.user)
        while True:
            if count < 3:
                try:
                    cursor.execute(query)
                    self.connection[Constants.first_index].commit()
                    assert True
                    break
                except Exception as e:
                    self.log.logger.error("run Query Error" + str(e))
                    count += 1
            else:
                self.log.logger.error("No data is present in " + table_name)
                break

    def run_query_to_delete_file_without_created_by_id(self, context, table_name, condition, value):
        count = Constants.first_index
        cursor = self.connection[Constants.first_index].cursor()
        query = f"delete from %s where %s = '%s'"
        query = query % (table_name, condition, value)
        while True:
            if count < 3:
                try:
                    cursor.execute(query)
                    self.connection[Constants.first_index].commit()
                    assert True
                    break
                except Exception as e:
                    self.log.logger.error("run Query Error" + str(e))
                    count += 1
            else:
                self.log.logger.error("No data is present in " + table_name)
                break

    def run_query_to_get_id_without_created_by_id(self, context, table_name, condition, value):
        count = Constants.first_index
        cursor = self.connection[Constants.first_index].cursor()
        query = f"SELECT id  from %s where %s = '%s'"
        query = query % (table_name, condition, value)
        while True:
            if count < 3:
                try:
                    cursor.execute(query)
                    query_data = cursor.fetchall()
                    return query_data
                except Exception as e:
                    self.log.logger.error("run Query Error" + str(e))
                    count += 1
            else:
                self.log.logger.error("No data is present in " + table_name)
                break

    def run_query_to_update_the_record(self, context, table_name, column_name, column_value, condition, value):
        count = Constants.first_index
        cursor = self.connection[Constants.first_index].cursor()
        query = "UPDATE %s SET %s = %s where %s = '%s' and %s  is not  null and created_by_id = (select id from user where user_name = '%s')"
        query = query % (table_name, column_name, column_value, condition, value, column_name, YieldWerxDataBase.user)
        while True:
            if count < 3:
                try:
                    cursor.execute(query)
                    self.connection[Constants.first_index].commit()
                    assert True
                    break
                except Exception as e:
                    self.log.logger.error("run Query Error" + str(e))
                    count += 1
            else:
                self.log.logger.error("source_die_id is null")
                break

    def run_query_to_drop_table(self, context, table_name):
        count = Constants.first_index
        cursor = self.connection[Constants.first_index].cursor()
        query = "DROP TABLE %s"
        query = query % table_name

        while True:
            if count < 3:
                try:
                    cursor.execute(query)
                    assert True
                    break
                except Exception as e:
                    self.log.logger.error("run Query Error : " + str(e))
                    count += 1
            else:
                self.log.logger.error(table_name + " is not exist in db")
                break

