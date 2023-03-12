from Helpers.aws import AwsConfigurations
from Utilities.log import Logger
import logging

log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))
aws_config = AwsConfigurations()


# Create files to bucket #
def create_aws_bucket(context, bucket_name):
    # Creating Session With Boto3
    s3 = aws_config.creating_aws_session(context)
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'})


# Upload the files into the bucket with bucket name  and their location #
def upload_file_to_aws(context, location, bucket_name, key):
    # Creating Session With Boto3.
    s3 = aws_config.creating_aws_session(context)
    result = s3.meta.client.put_object(Body=open(location, 'rb'), Bucket=bucket_name, Key=key)
    res = result.get('ResponseMetadata')
    if res.get('HTTPStatusCode') == 200:
        log.logger.info('file Uploaded Successfully')
    else:
        log.logger.info('file Not Uploaded')


