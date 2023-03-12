import boto3
from config.constants import AWSCredential

aws_credential = AWSCredential()


class AwsConfigurations:
    accessKey = aws_credential.access_key
    secretKey = aws_credential.secret_key

    def creating_aws_session(self, context):
        global s3
        session = boto3.Session(
            aws_access_key_id=self.accessKey,
            aws_secret_access_key=self.secretKey
        )
        # Create Bucket
        s3 = session.resource('s3')
        return s3

    def creating_aws_client(self, context):
        return boto3.client('s3', aws_access_key_id=self.accessKey, aws_secret_access_key=self.secretKey)
