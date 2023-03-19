import logging as logging
import sys

DEBUG = logging.DEBUG
INFO = logging.INFO
ERROR = logging.ERROR

'''
level = python_supporter.logging.DEBUG
#level = python_supporter.logging.INFO
#level = python_supporter.logging.ERROR
python_supporter.logging.basic_config(level)
'''
def basic_config(level=DEBUG, log_file="log.txt"):
    for name in logging.root.manager.loggerDict:
        logger = logging.getLogger(name)
        #logger.disabled = True
        logger.setLevel(logging.ERROR)

    logging.basicConfig(
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout)
        ],
        format = '%(asctime)s: %(levelname)s: %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        level = level
    )

def debug(message):
    logging.debug(message)

def info(message):
    logging.info(message)

def error(message):
    logging.error(message)
