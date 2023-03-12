from datetime import datetime
from config.constants import Constants
from Utilities.log import Logger
import logging

log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))


# Performance log calculation
def performance_calc(context, start_date, end_date):
    start_date = str(start_date[0][0])
    end_date = str(end_date[0][0])
    start = datetime.strptime(start_date, Constants.date_format)
    end = datetime.strptime(end_date, Constants.date_format)  # Get interval between two datetime as timedelta
    diff = abs(end - start)  # I get the interval in minutes
    diff_in_minutes = diff.total_seconds() / 60
    log.logger.info('Difference between two datetime in minutes:' + str(diff_in_minutes))
    return diff_in_minutes


# Performance log calculation for selection criteria
def performance_calc_for_selection_criteria(context, start_date, end_date):
    start = datetime.strptime(start_date, Constants.date_format)
    end = datetime.strptime(end_date, Constants.date_format)  # Get interval between two datetime as timedelta
    diff = abs(end - start)  # I get the interval in minutes
    diff_in_minutes = diff.total_seconds() / 60
    log.logger.info('Difference between two datetime in minutes:' + str(diff_in_minutes))
    return diff_in_minutes
