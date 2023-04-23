import logging

from app.com.saraswati.www.src.utilities import logger, log_message

logger.setLevel(logging.INFO)


def get_hello_world() -> str:
    """
    Test method which returns string "Hello World" to get started
    :return: String "Hello World"
    """
    log_message("This is hello world dummy")
    return "Hello World"
