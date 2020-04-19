from lib.log import get_logger
from config.context import CustomContext

LOG = get_logger(
    "engine.py",
    "'[%(levelname)s] [%(name)s] [%(asctime)s] [%(funcName)s::%(lineno)d] [%(message)s]'",
)

def run(event=None, context=None):
    '''
        Funtionality for lambda function.

        Parameters:
            - () :

        Returns:
            - () :
    '''
    LOG.info(f"Triggered from main.py lambda. Event --> {event}.")

    custom_context = CustomContext(event=event, aws_ctx=context)

    response = {}

    return response