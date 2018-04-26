import pandas as pd
import numpy as np
from datetime import date
from dateutil import relativedelta as rd

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def bias(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0