import logging
from botocore.exceptions import ClientError
from Helpers.aws import AwsConfigurations
from Utilities.log import Logger

aws_config = AwsConfigurations()


class DeleteFilesFromS3Buckets:
    log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    def delete_bucket(self, context, bucket_name):
        """Delete a bucket (and all object versions)"""
        self.log.logger.info('Deleting ...'.format(bucket_name))

        try:
            s3 = aws_config.creating_aws_session(context)
            bucket = s3.Bucket(bucket_name)
            bucket.object_versions.delete()
            # bucket.delete()
        except ClientError as ex:
            self.log.logger.warning('error: {}'.format(ex.response['Error']))

        self.log.logger.info('done')

    def delete_file_from_bucket(self, context):
        """Delete multiple buckets (and all object versions respectively)"""
        raw_bucket_list = ['yw-rawfile-1', 'yw-loader-2', 'yw-golden-1']
        for bucket in raw_bucket_list:
            try:
                DeleteFilesFromS3Buckets.delete_bucket(self, context,  bucket)
            except Exception as e:
                self.log.logger.warning(str(e))
                assert False

    def delete_file_from_bucket_with_feature_name(self, context):
        """Delete multiple buckets (and all object versions respectively)"""
        feature_name = context.feature.filename
        feature_name = feature_name.split(".")[0].split("/")[1]
        raw_bucket_list = [feature_name]
        for bucket in raw_bucket_list:
            try:
                DeleteFilesFromS3Buckets.delete_bucket(self, context, bucket)
            except Exception as e:
                self.log.logger.warning(str(e))
                assert False
