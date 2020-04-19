import boto3
import botocore
import traceback
from config.context import CustomContext
from lib.log import get_logger

LOG = get_logger(
    "results.py",
    "'[%(levelname)s] [%(name)s] [%(asctime)s] [%(funcName)s::%(lineno)d] [%(message)s]'",
)

def handler(event, context):
    """
        Example lambda function called by api gateway and returns response.

        Parameters:
            - event (AWSEvent)  : This object is created by AWS. API Gayeway event.

        Returns:
            - response (dict) : 
    """
    LOG.info(f"Result event --> {event}")

    custom_context = CustomContext(event=event, aws_ctx=context)

    # Construct response.
    response={}
    response["status_code"] = 200
    response["event"] = event

    return response


def create_presigned_url(bucket_name=None, key=None, expiration=3600):
    """
        Generate a presigned URL to share an S3 object

        Parameters:
        - bucket_name (str) : Name of a bucket.
        - object_name (string) : Key of a file in s3.
        - expiration (int) : Time in seconds for the presigned URL to remain valid. 120s = 2m
 
        Returns:
        - response (str) : Presigned URL as string. If error, returns None.
    """

    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': key},
                                                    ExpiresIn=expiration)
    except botocore.exceptions.ClientError as e:
        LOG.error(
            {
                "exception_type": type(e).__name__,
                "error_reason": e.args,
                "traceback": traceback.format_exc(),
            }
        )
    return response