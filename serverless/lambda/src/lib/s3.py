'''
    Functions related to aws s3 read/write/download/upload/presign
'''
import os
import boto3
import botocore
from lib.log import get_logger

LOG = get_logger(
    "s3.py",
    "'[%(levelname)s] [%(name)s] [%(asctime)s] [%(funcName)s::%(lineno)d] [%(message)s]'",
)

# If bucket does not exist, create it.
def ensure_bucket_exists(context=None):
    if (bucket_exists(bucket_name=os.environ['bucket'], s3_client=context.s3) == False):
        location = {'LocationConstraint': os.environ['aws_region']}
        bucket = context.s3.create_bucket(Bucket=os.environ['bucket'], CreateBucketConfiguration=location)
        LOG.info(f"{os.environ['bucket']} did not exist; it has been created.")


def bucket_exists(bucket_name=None, s3_client=None):
    '''
        Determine whether bucket_name exists and if the user 
        has permission to access it

        Parameters:
            - bucket_name (string) : The name of the bucket to search for.
            - s3_client (s3 client obj) : A low-level client representing AWS S3.

        Returns:
            - (bool) : True if the referenced bucket_njoinedlist = listone + listtwoame exists, otherwise False
    '''
    try:
        response = s3_client.head_bucket(Bucket=bucket_name)
        return True
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 403:
            LOG.info(f"Private Bucket. Forbidden Access!")
            return True
        elif error_code == 404:
            LOG.info(f"Bucket Does Not Exist!")
            return False