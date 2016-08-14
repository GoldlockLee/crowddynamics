import logging as log
import logging.handlers
import os
import platform
import sys


def start_logging(level):
    log_format = log.Formatter('%(asctime)s, %(levelname)s, %(message)s')
    logger = log.getLogger()
    logger.setLevel(level)

    filename = "run.log"
    if os.path.exists(filename):
        os.remove(filename)  # Remove old log file
    file_handler = logging.handlers.RotatingFileHandler(
        filename, maxBytes=(10240 * 5), backupCount=2
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    console_handler = log.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)


def user_info():
    log.info("Platform: %s", platform.platform())
    log.info("Path: %s", sys.path[0])
    log.info("Python: %s", sys.version[0:5])