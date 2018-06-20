"""
This module is used for basic data processing purpose.
"""
import pandas as pd

def list_missing_pct(df):
    """
    return missing value's percentage by columns
    :param df: pd.Dataframe
    :return: pd.Series
    """
    percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
    return percent

def group_by_missing_percent(df, threshold=0.5):
    """
    based on given threshold, seperate table into two sub sets.
    First is with missing pct below threshold and second is for others.
    :param df: pd.Dataframe
    :param threshold: double
    :return: pd.Dataframe, pd.Dataframe
    """
    percent = list_missing_pct(df)
    condition = percent < threshold
    return df[percent[condition].index], df[percent[~condition].index]

