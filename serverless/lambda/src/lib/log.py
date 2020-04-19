'''
    A universal logger.
'''
import logging

def get_logger(name, format_string, level=None):
    """
    Creates a generic python logger with configurable name, formatter, and log level.
    ​
    Parameters:
        - name (str): The name of the logger.
        - format_string (str): Format string to use when creating the logger.
        - level (str): Culls out messages with lower priority level.
                       (debug, info, warning, error, critical)
    ​
    Returns:
        - logging.Logger: An instance logger.
    """
    level = "info" if level is None else level
    log_level = logging.__getattribute__(level.upper())
    logging.basicConfig(format=format_string)
    root = logging.getLogger()
    for h in root.handlers:
        h.setFormatter(logging.Formatter(format_string))
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    return logger
