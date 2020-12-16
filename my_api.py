import streamlit as st
from PIL import Image
import pandas as pd 

from tools import options, query

### PRUEBA:
st.title("Radiant Qara")
st.header("1 Header")
st.subheader("1 Subheader")
st.text("Holi")
st.markdown("Holi in markdown")

img = Image.open("images/one.jpg")
st.image(img, width=300, caption="skincare")

#### FOR REAL:

# First:

brand_option = st.selectbox("Please choose a brand:", options.list_brand)
brand_result = query.brand(brand_option)
st.table(brand_result)

# Second:

multi_brand_option = st.multiselect("Please the brands you like the most:", options.list_brand)
multi_brand_result = query.multi_brand(multi_brand_option)
st.table(multi_brand_result)

# Third

category_option = st.selectbox("Please choose a category:", options.list_category)
category_result = query.category(category_option)
st.table(category_result)

# Fourth

multi_category_option = st.multiselect("Please the categories you like the most:", options.list_category)
multi_category_result = query.multi_category(multi_category_option)
st.table(multi_category_result)

# Fifth
skin_option = st.selectbox("Please choose a skin type:", options.list_type_skin)
skin_result = query.skin_type(skin_option)
st.table(skin_result)

# Sixth
money_rank = st.slider('How much money do you want to spend', options.min_money, options.max_money)
money_result = query.money(money_rank)
st.table(money_result)

# Seventh
rating_option = st.slider('Rating', 0, 5)
rating_result = query.rating(rating_option)
st.table(rating_result)