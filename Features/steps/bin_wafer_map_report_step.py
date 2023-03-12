from behave import *
from pages.bin_wafer_map_report_page import BinWaferMapPage

wafer_map = BinWaferMapPage()


@Then('Verify bin wafer map report')
def create_bucket_on_aws_s3(context):
    wafer_map.verifying_data(context)


@Then('I generate the Report')
def generating_report(context):
    wafer_map.generate_report(context)


@Then('I Verify the Selection criteria window appeared')
def verify_selection_criteria(context):
    wafer_map.verify_selection_criteria(context)


@Then('Verifying the canvas exists')
def check(context):
    wafer_map.verify_canvas(context)