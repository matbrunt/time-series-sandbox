import pandas as pd
import numpy as np


class Naive(object):
    def fit(self, df):
        self.train_data = df
        
    def predict(self, idx):
        return pd.Series(np.repeat(self.train_data.iloc[-1].passengers, len(idx)), index=idx)


class SeasonalNaive(object):
    def fit(self, df):
        self.train_data = df
        
    def predict(self, idx):
        return pd.Series(self.train_data[-12:].passengers.values, index=idx)


class MovingAverage(object):
    def __init__(self, window=12):
        self.window = window
        
    def fit(self, df):
        self.train_data = df
        
    def predict(self, idx):
        return pd.Series(self.train_data.rolling(window=self.window, center=False).mean().iloc[-12:].passengers.values, index=idx)
