import pandas as pd
import numpy as np
from datetime import date
from dateutil import relativedelta as rd

from helpers import utils


def load_data():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
    df = pd.read_csv(utils.get_external_file('AirPassengers.csv'), parse_dates=['Month'], index_col='Month',date_parser=dateparse)
    df.columns = ['passengers']
    return df


def get_historical_slice(df, forecast_start, horizon=12):
    train = df[:forecast_start - rd.relativedelta(months=1)]
    test = df[forecast_start:forecast_start + rd.relativedelta(months=horizon-1)]
    
    return train, test


def get_period_observations(df, period_start, period_end):
    return (
        df.copy()
        [period_start:period_end]
        .reset_index()
        .rename(columns={'Month': 'month', 'passengers': 'y_true'})
    )


def get_train_data(df, forecast_start):
    return (
        df.copy()
        [:forecast_start - rd.relativedelta(months=1)]
    )
