## Functions to clean datasets.
# ------------------------------

import pandas as pd


def droping_columns(data, lst):
    ''' Function to drop columns from a dataset.
        input = dataframe, list of columns names
        output = draframe 
    '''
    new_data = data.drop(lst, axis=1)
    return new_data


def sort_by_elements(data, serie, lst):
    ''' Function to sort a dataframe by specific values.
        input = serie, list of values
        output = dataframe
    '''
    new_data = data[serie.isin(lst)]
    return new_data


def new_index(data):
    ''' Function that resets the index of a dataframe
        input = dataframe
        output = dataframe
    '''
    new_data = data.reset_index(drop=True)
    return new_data