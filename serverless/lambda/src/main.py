import traceback
import ast
from config.context import CustomContext
from func.selen import SeleniumDriver
from func.engine import run
from lib.log import get_logger


LOG = get_logger(
    "main.py",
    "'[%(levelname)s] [%(name)s]  [%(asctime)s] [%(funcName)s::%(lineno)d] [%(message)s]'",
)

def engine(event, context):
    """
        Called by api gateway.

        Parameters:
            - event (AWSEvent)  : This object is created by AWS. API Gayeway event.

        Returns:
            - response (dict) : This wrapper gets the response/results from run and
                                returns those results as a response to the api call.
    """
    response = None

    try:
        LOG.info(f"endpoint event --> {event}")

        custom_context = CustomContext(event=event, aws_ctx=context)

        session = SeleniumDriver()

        response = run(event=event, context=custom_context, session=session)

        session.end_session()
    except Exception as e:
        LOG.error(
            {
                "exception_type": type(e).__name__,
                "error_reason": e.args,
                "traceback": traceback.format_exc(),
            }
        )

        response = {
            "status_code": 500,
            'event': event,
            "exception_type": type(e).__name__,
            "error_reason": e.args,
            "traceback": traceback.format_exc()
        }

    return response