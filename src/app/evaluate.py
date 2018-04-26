import pandas as pd
import numpy as np

from datetime import date
from dateutil import relativedelta as rd

from app import data_loader as dl
from app import evaluate, metrics


def make_future_index(period_start, horizon=12):
    return pd.date_range(period_start, periods=horizon, freq='MS')


def calc_months_diff(x):
    return rd.relativedelta(x.month, x.forecast_start).months + 1


def generate_evaluation_set(df, period_start, period_end, horizon, model):
    def add_observations(result):
        return (
            pd.merge(result, dl.get_period_observations(df, period_start, period_end), on=['month'], how='inner')
            .assign(error = lambda x: x.y_pred - x.y_true)
            .assign(bias = lambda x: x.error.map(metrics.bias))
        )
        
    results = pd.DataFrame(None, columns=['month', 'y_true', 'y_pred'])
    
    for run_num in range(0, horizon):
        forecast_start = period_start + rd.relativedelta(months=run_num)
        train = dl.get_train_data(df, forecast_start)
        future = make_future_index(forecast_start, horizon)
        
        model.fit(train)
        estimates = model.predict(future)
        
        result = (
            pd.DataFrame({
                'month': future.values,
                'y_pred': estimates
            }, index=future)
            .assign(forecast_start = lambda x: pd.to_datetime(forecast_start))
            .assign(horizon = lambda x: x.apply(calc_months_diff, axis=1))
        )
        
        result = add_observations(result)
        
        results = pd.concat([results, result])
    
    return results


def build_period_score(df):
    return (
        df
        .groupby(['forecast_start'])
        .agg({
            'y_pred': np.sum,
            'y_true': np.sum,
        })
        .reset_index()
        .assign(mape = lambda x: metrics.mean_absolute_percentage_error(x.y_true, x.y_pred))
        .assign(mae = lambda x: metrics.mean_absolute_error(x.y_true, x.y_pred))
        .assign(rmse = lambda x: np.sqrt(metrics.mean_squared_error(x.y_true, x.y_pred)))
        .assign(bias = lambda x: (x.y_pred - x.y_true).map(metrics.bias))
    )


def build_horizon_score(df, group='horizon'):
    def aggregate(x):
        return pd.Series({
            'mape': metrics.mean_absolute_percentage_error(x.y_true, x.y_pred),
            'mae': metrics.mean_absolute_error(x.y_true, x.y_pred),
            'rmse': np.sqrt(metrics.mean_squared_error(x.y_true, x.y_pred)),
            'observations': x.y_true.count(),
            'bias': x.bias.sum() / x.bias.count()
        })
    
    return (
        df
        .groupby([group])
        .apply(aggregate)
        .reset_index()
    )
