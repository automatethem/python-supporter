import logging 
import sys

'''
cranberry.logging_lib.basic_config()

level = logging.DEBUG
#level = logging.INFO
#level = logging.ERROR
cranberry.logging_lib.basic_config(level)
'''
def basic_config(level=logging.DEBUG, log_file="log.txt"):
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
