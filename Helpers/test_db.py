import logging
from pymongo import *
from Utilities.log import Logger
import logging

class MongoDb:
    def __init__(self):
        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))
        self.name = 'Mongo'
        self.client = None
        self.db = None
        self.Host = "localhost"
        self.Port = 27017
        self.dbName = "TestDataBase"
        self.collection = ""

    # Connect to mongo database #
    def connect_mongo(self, context):
        self.client = MongoClient(self.Host,self.Port)
        self.db = self.client[self.dbName]

    # Write the value into mongo database #
    def write_value(self, context, collection_name, key_name, value):
        try:
            self.collection = self.db[collection_name]
            post_data = {
                'Key': str(key_name),
                'Data': str(value)
            }
            self.collection.insert_one(post_data)
        except Exception as e:
            self.log.logger.warning("Write value in Test DB Error : "+e)
            assert False

        # Write the value into mongo database #

    def write_value_for_multiple_file(self, context, collection_name, key_name, value):
        try:
            self.collection = self.db[collection_name]
            post_data = {
                'Key': str(key_name),
                'Data': str(value)
            }
            self.collection.insert_one(post_data)
        except Exception as e:
            self.log.logger.warning("Write value in Test DB Error : " + e)
            assert False

    # Write the multiple value into mongo database #
    def write_multiple_value(self, context, collection_name, key_name, value):
        try:
            self.collection = self.db[collection_name]
            post_data = {
                'Key': str(key_name),
                'Data': value
            }
            self.collection.insert_one(post_data)
        except Exception as e:
            self.log.logger.warning("Write Multiple value in Test DB Error : "+e)
            assert False

    # Update the value into mongo database #
    def update_value(self, context, collection_name, key_name, value):
        try:
            self.collection = self.db[collection_name]
            self.collection.update_one(
                {"Key": str(key_name)},
                {
                    "$set": {
                        "Data": str(value)
                    }
                }
            )
        except Exception as e:
            self.log.logger.warning("Update value in Test DB Error : "+e)
            assert False

    # Read the data value from test database with collection name and key #
    def read_value(self, context, collection_name, key_name):
        try:
            self.collection = self.db[collection_name]
            value = self.collection.find_one({'Key': str(key_name)})
            return value
        except Exception as e:
            self.log.logger.warning("Read value in Test DB Error : "+str(e))
            assert False

    # Read the all data value from test database with collection name #
    def read_all(self, context, collection_name):
        try:
            self.collection = self.db[collection_name]
            all_value = []
            for value in self.collection.find():
                all_value.append(value)

            return all_value
        except Exception as e:
            self.log.logger.warning("Read value in Test DB Error : "+e)
            assert False

    # # Read the data value from test database with collection name #
    # def read_value(self, collection_name):
    #     try:
    #         self.collection = self.db[collection_name]
    #         return self.collection.find()
    #     except Exception as e:
    #         self.log.logger.warning("Read value in Test DB Error : "+e)
    #         assert False

    def remove_record(self, context, collection_name, userid):
        try:
            self.collection = self.db[collection_name]
            self.collection.delete_one({'Key': str(userid)})
        except Exception as e:
            self.log.logger.warning("Remove value in Test DB Error : "+e)
            assert False

    # Remove the multiple value from mongo database #
    def remove_multiple_record(self, context, collection_name, userid):
        try:
            self.collection = self.db[collection_name]
            self.collection.delete_many({'Key': str(userid)})
        except Exception as e:
            self.log.logger.warning("Remove Multiple value in Test DB Error : "+e)
            assert False

    # Get all the collection from mongo database #
    def get_all_collections(self, context):
        self.connect_mongo(context)
        collection_list = self.db.list_collection_names()
        return collection_list

    # Create the new collection mongo database #
    def create_new_collection(self, context, collection_name):
        new_collection = self.db[collection_name]
        return new_collection

    # Delete the collection from mongo database #
    def delete_docs_from_collection(self, context, collection_name):
        self.db[collection_name].delete_many({})
