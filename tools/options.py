import pandas as pd 



# Functions to work with the dataframe

data = pd.read_csv('data/final_dataset_to_mongo.csv', index_col='Unnamed: 0')

######### 1º PART

one_list_type_skin = ['Normal', 'Dry', 'Combination', 'Oily', 'Sensitive']

######### 2º PART

# First list: Brand
list_brand = list(data.Brand.unique())

# Second list: Category
list_category = list(data.Category.unique())

# Third list: Skin Type
list_type_skin = ['Normal', 'Dry', 'Combination', 'Oily', 'Sensitive']

# Fourth list: Max moeny
max_money = int(data.Price.max())

# Fifth list: Min money
min_money = int(data.Price.min())