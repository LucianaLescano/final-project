from config.configuration import db, collection

# Functions to make queries to MongoDB to get the information
# that the users requests

# First list: Brand

def brand(brand_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the brand
    input = user's input
    output = dictionary
    '''
    one = list(collection.find({'Brand':brand_option}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(6).sort('Rating', -1))
    return one

# Second list: Multi-Brand

def multi_brand(multi_brand_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the brands
    input = user's input
    output = dictionary
    '''
    two = list(collection.find({'Brand':{"$in":multi_brand_option}}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(5).sort('Rating', -1))
    return two

# Third list: Category

def category(category_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the product's category
    input = user's input
    output = dictionary
    '''
    three = list(collection.find({'Category':category_option}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(5).sort('Rating', -1))
    return three

# Fourth list: Multi-Category

def multi_category(multi_category_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the product's categories
    input = user's input
    output = dictionary
    '''
    four = list(collection.find({'Category':{"$in":multi_category_option}}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(5).sort('Rating', -1))
    return four

# Fifth list: Skin Type

def skin_type(skin_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    five = list(collection.find({'Skin_Type':skin_option}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(5).sort('Rating', -1))
    return five

# Sixth list: Money

def money(money_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the price
    input = user's input
    output = dictionary
    '''
    six = list(collection.find({'Price':{"$lte":money_option}}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(5))
    return six

# Seventh list: Rating

def rating(rating_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the rating
    input = user's input
    output = dictionary
    '''
    seven = list(collection.find({'Rating':rating_option}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(5))
    return seven