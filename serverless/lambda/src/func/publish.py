import boto3
import os
from config.context import CustomContext
from lib.log import get_logger

LOG = get_logger(
    "publish.py",
    "'[%(levelname)s] [%(name)s]  [%(asctime)s] [%(funcName)s::%(lineno)d] [%(message)s]'",
)

def handler(event, context):
    """
        Example lambda function called by api gateway which triggers an SNS topic-subscription.

        Parameters:
            - event (dict)  : This object is created by AWS.
            - var(context) (LambdaContext) : aws_request_id, log_group_name, & other info.

        Returns:
            - response (dict) : 
    """
    LOG.info(f"Published event --> {event}")

    custom_context = CustomContext(event=event, aws_ctx=context)

    sns = custom_context.sns

    sns_trigger = publish_to_topic("triggering message from lambda", sns)

    LOG.info(f"sns_trigger info --> {sns_trigger}")

    # Construct response.
    response = {}
    response["status_code"] = 200
    response["event"] = event

    return response


def publish_to_topic(message, sns_client):
    '''
        Sends a message to an Amazon SNS topic

        Parameters:
        - message (str) : An api gateway triggered event obj containing 'dropID' & 'rebuild' keys.
        - sns_client (sns client obj) : A low-level client representing AWS SNS.

        Returns:
        - response (dict) : Response for Publish action. Message sent to SNS topic.
    '''
    response = sns_client.publish(
        TopicArn=os.environ['sns_topic_arn'],
        Message=message,
    )
    return response