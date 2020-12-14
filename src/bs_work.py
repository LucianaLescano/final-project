import pandas as pd 
import requests
from bs4 import BeautifulSoup

def from_serie_to_list(serie):
    '''
    Function to get a list from a dataframe serie
    input = dataframe serie
    output = list
    '''
    lst = []
    for s in serie:
        lst.append(s)
    return lst 


def skin_type_category(lst):
    '''
    Function to get more information from webscraping
    input = list
    output = dataframe
    '''
    final_list = []
    for l in lst:
        try:
            response = requests.get(l)
            soup = BeautifulSoup(response.content, 'html.parser')
            skin_type = soup.find('b', text='Skin Type: ').next_sibling
            final_list.append(skin_type)
        except:
            final_list.append('ERROR')
    df = pd.DataFrame({'col':final_list})
    return df