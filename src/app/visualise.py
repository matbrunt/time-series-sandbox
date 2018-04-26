import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from app.evaluate import build_horizon_score


def plot_horizon_variance(df):
    sns.boxplot(x="horizon", y="error", data=df, palette="Set3")


def plot_horizon_score(df):
    df.plot(x='horizon', y='mape')


def plot_horizon_bias(df):
    sns.barplot(x='horizon', y='bias', data=df, color='b')


def plot_month_score(df, horizon=1):
    months = (
        build_horizon_score(df[df.horizon == horizon], 'forecast_start')
        .assign(start_month = lambda x: x.forecast_start.dt.strftime('%b'))
        .assign(month = lambda x: x.forecast_start.dt.month)
        .sort_values(['month'])
    )
    sns.barplot(x='start_month', y='mape', data=months)


def plot_horizon_score(df):
    sns.barplot(x="horizon", y="mape", data=df)
