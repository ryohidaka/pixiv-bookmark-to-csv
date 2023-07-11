import logging


def init_logger():
    """
    Set the log level.

    Returns:
      logging.Logger: The logger object.
    """

    # Create a logger object.
    logger = logging.getLogger(__name__)

    # Set the log level for the logger object.
    logger.setLevel(logging.INFO)

    # Create a handler that outputs logs to the console.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Set the format for the console handler.
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger object.
    logger.addHandler(console_handler)

    # Return the logger object.
    return logger
