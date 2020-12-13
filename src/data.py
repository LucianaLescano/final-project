## Functions to API.
# ------------------------------

import pandas as pd
import sys
sys.path.append('../data')


def loading_data():
    data = pd.read_csv('../data/clean_data.csv', index_col='Unnamed: 0')
    return data

loading_data()