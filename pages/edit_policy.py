# import os
# import logging
# import allure
# from allure_commons.types import AttachmentType
# from allure_commons._allure import attach
# from Utilities import bucket_file_download
# from selenium.webdriver.common import keys
# from datetime import datetime, timedelta
# from pages.database import DatabaseManagement
# from selenium.webdriver.common.by import By
# import time
# from Utilities import yaml_reader
# from config.web import WebConfigurations
# from config.driver_manager import WebDriverManager
# from Helpers.generics import GenericMethods
# from Helpers.reports import ReportsHelper
# from Helpers.selection_criteria import SelectionCriteriaHelper
# from Utilities.log import Logger
# from Elements.create_policy import CreatePolicyElements
# from config.constants import Constants
#
# database = DatabaseManagement()
# manage_driver = WebDriverManager()
# web_conf = WebConfigurations()
# helpers = GenericMethods()
# current_time = datetime.now()
# web_elements = CreatePolicyElements()
# report_helper = ReportsHelper()
# selection_criteria_helper = SelectionCriteriaHelper()
#
#
# class EditPolicyPage:
#     def __init__(self):
#         self.log = Logger(logging.basicConfig(
#             format='%(asctime)s %(levelname)-8s %(message)s',
#             level=logging.INFO,
#             datefmt='%Y-%m-%d %H:%M:%S'))
#
#      def verify_policy_name(self):
#          pass