import logging
from Utilities.log import Logger
from config.constants import Constants
from Helpers.db_config import DataBaseConfig
from pages.loader import LoaderClass
import allure
from allure_commons.types import AttachmentType
from behave.model_core import Status
from Hooks.delete_s3_bucket import DeleteFilesFromS3Buckets
delete_bucket = DeleteFilesFromS3Buckets()
db_config = DataBaseConfig()
loader = LoaderClass()
log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))


marked_file_path = Constants.marked_file_path


def before_scenario(context, scenario):
    log.logger.info("Start scenario name " + scenario.name)


def after_scenario(context, scenario):
    try:
        if "selection criteria" not in scenario.name and "parametric histogram " not in scenario.name:
            if "loader policy" in scenario.name:
                loader.rollback_the_transaction(context, marked_file_path)
            elif "converter policy" in scenario.name:
                loader.rollback_the_transaction_for_converter(context)
        else:
            log.logger.info("End scenario name " + scenario.name)
    except Exception as e:
        print(e)
    try:
        delete_bucket.delete_file_from_bucket_with_feature_name(context)
        if scenario.status == Status.failed:
            allure.attach(context.driver.get_screenshot_as_png(), name=scenario.name,
                          attachment_type=AttachmentType.PNG)
            context.driver.quit()
        else:
            context.driver.quit()
    except Exception as e:
        print(e)


def after_feature(context, feature):
    if "selectionCriteria" in feature.filename:
        loader.rollback_the_transaction(context, Constants.selection_marked_file_path)
    elif "parametricHistogram" in feature.filename:
        loader.rollback_the_transaction(context, Constants.parametric_histogram_marked_file_path)

