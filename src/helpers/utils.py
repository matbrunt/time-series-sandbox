import os
import sys
import logging
from dateutil import relativedelta as rd


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def get_project_root_dir():
    root_dir = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
    return root_dir


def get_project_path(*args):
    return os.path.abspath(os.path.join(get_project_root_dir(), *args))


def get_logger(name):
    logger = logging.getLogger(name)
    return logger


def get_queries_file(filename):
    return get_project_path('queries', filename)


def get_raw_file(filename):
    return get_project_path('data', 'raw', filename)


def get_external_file(filename):
    return get_project_path('data', 'external', filename)


def get_interim_file(filename):
    return get_project_path('data', 'interim', filename)


def get_processed_file(filename):
    return get_project_path('data', 'processed', filename)


def get_last_day_of_previous_month(date):
    """
    For the input date, return the last date of the previous month
    """
    return date + rd.relativedelta(day=1, days=-1)
