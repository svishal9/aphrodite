import sys

from app.com.saraswati.www.src.utilities import log_message, get_logging_config, _ExcludeErrorsFilter


def test_get_logging_config():
    expected = {
        'version': 1,
        'filters': {
            'exclude_errors': {
                '()': _ExcludeErrorsFilter
            }
        },
        'formatters': {
            # Modify log message format here or replace with your custom formatter class
            'my_formatter': {
                'format': '(%(process)d) %(asctime)s %(name)s (line %(lineno)s) | %(levelname)s %(message)s'
            }
        },
        'handlers': {
            'console_stderr': {
                # Sends log messages with log level ERROR or higher to stderr
                'class': 'logging.StreamHandler',
                'level': 'ERROR',
                'formatter': 'my_formatter',
                'stream': sys.stderr
            },
            'console_stdout': {
                # Sends log messages with log level lower than ERROR to stdout
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'my_formatter',
                'filters': ['exclude_errors'],
                'stream': sys.stdout
            },
            'file': {
                # Sends all log messages to a file
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'my_formatter',
                'filename': 'aphrodite.log',
                'encoding': 'utf8'
            }
        },
        'root': {
            # In general, this should be kept at 'NOTSET'.
            # Otherwise, it would interfere with the log levels set for each handler.
            'level': 'NOTSET',
            'handlers': ['console_stderr', 'console_stdout', 'file']
        },
    }
    actual = get_logging_config()
    assert actual == expected


def test_log_message(capfd):
    log_message("This is test log record")
    captured = capfd.readouterr()
    expected = "aphrodite_app_log : This is test log record\n"
    # So far 2 lines have been printed, taking the second line with just the logs
    actual = captured.out.split("|")[-1].split(" - ")[1]
    assert actual == expected
