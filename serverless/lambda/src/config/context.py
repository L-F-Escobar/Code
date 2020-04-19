'''
    A context contains resources specific to an environment.
    Typically lambda passes in it's own aws context,
    however these are not very useful on their own.
    The following context is specific for the lambdas built for a given product
    and is meant to extend or replace the base aws context.
'''
import os
import json
import yaml
import boto3
from box import Box

class CustomContext:
    """
    Contains common external resources used for selenium & lambda processes
    needed. Can be easily mocked for test scenarios.

    Attributes:
      - event (object):  aws event.
      - aws_context: original context from aws.
      - args (object): injectable parameters.
    """

    def __init__(self, event=None, aws_ctx=None, args=None):
        const_path = args.get('const_path') if args else "./config/const.yml"
        const = load_const(const_path)
        env = load_env()
        var = dict()
        var.update(const)
        var.update(env)
        if args: 
            var.update(args)
        self.var = Box(var)

        self.aws_context = aws_ctx

        self.s3 = boto3.client('s3',
            endpoint_url=self.var.get('s3_endpoint')
        )

        self.sqs = boto3.resource('sqs',
            endpoint_url=self.var.get('sqs_endpoint'),
            region_name=self.var.region
        )

        self.sns = boto3.resource('sns',
            endpoint_url=self.var.get('sqs_endpoint'),
            region_name=self.var.region
        )

        self.lamb = boto3.client('lambda',
            endpoint_url=self.var.get('lambda_endpoint'),
            region_name=self.var.region
        )

        self.dynamo = boto3.resource('dynamodb',
            endpoint_url=self.var.get('dynamo_endpoint'),
            region_name=self.var.region
        )

        self.rds = None
        self.load_work(event)


def load_env():
    '''
    Captures any environment variable(s) and creates
    a property  for it.

    Returns:
        - box.Box: with properties equal to current environment.
    '''
    env = {}
    for name in os.environ:
        env[name.lower()] = os.environ.get(name)
    return env


def load_const(path="./config/const.yml"):
    '''
    Is called directly by lambda service via main.handler.

    Parameters:
        - path (str): Location of the yaml config file.

    Returns:
        - Dict: Dict of all consts from yml file.
    '''
    raw = None
    const = {}
    try:
        with open(path, 'r') as file:
            raw = file.read()
    except (FileNotFoundError, IOError) as error:
        print(f'No custom configuration file present!\n{str(error)}')

    if not raw is None:
        try:
            const = yaml.full_load(raw)
        except yaml.YAMLError as error:
            print(f'Custom config file loadingerror!\n{str(error)}')
    return const


def load_work(self, event, json_key='body'):
    '''
    Given a typical event list from AWS, extract
    the json message(s) within.

    Returns:
        - list: with all json messages deserialized into dict.
    '''
    def extract(record):
        return {
            'receipt': record['receiptHandle'],
            'received_count': int(record['attributes']['ApproximateReceiveCount']),
            'job': json.loads(record[json_key])
        }

    if event:
        self.work = [extract(record) for record in event.get('Records', [])]
    else:
        self.work = []