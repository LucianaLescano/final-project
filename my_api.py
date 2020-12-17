import streamlit as st
from PIL import Image
import pandas as pd 
import webbrowser

from tools import options, query

### PRUEBA:
st.title("Radiant Qara")
st.header("1 Header")
st.subheader("1 Subheader")
st.text("Holi")
st.markdown("Holi in markdown")

img = Image.open("images/one.jpg")
st.image(img, width=300, caption="skincare")

######### 1º PART

st.header("What about having your own personalized skincare routine?")
st.write(" ")

# First:

preference = st.selectbox("", ["Please select one", "Let’s go with the basic!", "Let’s go deep inside with the skincare routine!"])

if preference == 'Please select one':
    st.stop()
st.success("Perfect!")

if preference == "Let’s go with the basic!":
    st.stop()
    #if st.button("Let's start by some basics!"):
    st.write(" ")
    st.write("What's your skin type:")
    routine_skin_option = st.radio("", options.list_type_skin)
    # st.write(routine_skin_option)
    routine_skin_option_for_query = str(routine_skin_option)
    st.write(" ")
    st.write("How much money do you want to spend?")
    routine_money_option = st.text_input("", 0)
    # if st.button("Submit"):
    #    st.success("Perfect!")
    # st.write(routine_money_option)
    routine_money_option_for_query = float(routine_money_option)/3
    skincare_routine_result_one = query.cleanser_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query)
    skincare_routine_result_two = query.moist_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query)
    skincare_routine_result_three = query.sun_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query)
    st.table(skincare_routine_result_one)
    st.table(skincare_routine_result_two)
    st.table(skincare_routine_result_three)
    st.write(" ")
    st.write("To cheer you up to have a wonderful skincare routine. Here you have available all the links to the products:")
    st.write(" ")
    skincare_routine_result_one_url = query.cleanser_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
    st.write(skincare_routine_result_one_url)
    # try:
    #    link_one = st.write(skincare_routine_result_one_url[0].get('URL'))
    #    if st.button("Open"):
    #        webbrowser.open_new_tab(link_one)
    # except:
    #    pass

elif preference == "Let’s go deep inside with the skincare routine!":
    #if st.button("Let's start by some basics!"):
    st.write(" ")
    st.write("What's your skin type:")
    routine_skin_option = st.radio("", options.list_type_skin)
    # st.write(routine_skin_option)
    routine_skin_option_for_query = str(routine_skin_option)
    st.write(" ")
    st.write("How much money do you want to spend?")
    routine_money_option = st.text_input("", 0)
    # if st.button("Submit"):
    #    st.success("Perfect!")
    # st.write(routine_money_option)
    routine_money_option_for_query = float(routine_money_option)/5
    skincare_routine_result_one = query.cleanser_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query)
    skincare_routine_result_two = query.moist_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query)
    skincare_routine_result_three = query.sun_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query)
    skincare_routine_result_four = query.ton_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query)
    skincare_routine_result_five = query.serum_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query)
    st.table(skincare_routine_result_one)
    st.table(skincare_routine_result_four)
    st.table(skincare_routine_result_five)
    st.table(skincare_routine_result_two)
    st.table(skincare_routine_result_three)
    st.write(" ")
    st.write("To cheer you up to have a wonderful skincare routine. Here you have available all the links to the products:")
    st.write(" ")
    skincare_routine_result_one_url = query.cleanser_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
    st.write(skincare_routine_result_one_url)
    # try:
    #    link_one = st.write(skincare_routine_result_one_url[0].get('URL'))
    #    if st.button("Open"):
    #        webbrowser.open_new_tab(link_one)
    # except:
    #    pass

######### 2º PART

st.write(" ")
st.header("If you want to know more about the products")

# First:

# st.write("")
# brand_option = st.selectbox("", options.list_brand)
# brand_result = query.brand(brand_option)
# st.table(brand_result)

# Second:

st.write(" ")
st.write("Please choose the brand(s) you like the most:")
multi_brand_option = st.multiselect("", options.list_brand)
multi_brand_result = query.multi_brand(multi_brand_option)
st.table(multi_brand_result)

# Third

st.write(" ")
st.write("Please choose the category(s) you want:")
category_option = st.selectbox("", options.list_category)
category_result = query.category(category_option)
st.table(category_result)

# Fourth

# st.write("")
# multi_category_option = st.multiselect("", options.list_category)
# multi_category_result = query.multi_category(multi_category_option)
# st.table(multi_category_result)

# Fifth

st.write(" ")
st.write("Please choose a skin type:")
skin_option = st.selectbox("", options.list_type_skin)
skin_result = query.skin_type(skin_option)
st.table(skin_result)

# Sixth

st.write(" ")
st.write("Maybe you want to explore what’s the cost of some products...")
money_rank = st.slider("", options.min_money, options.max_money)
money_result = query.money(money_rank)
st.table(money_result)

# Seventh

st.write(" ")
st.write("... or its ratings")
rating_option = st.slider("", 0, 5)
rating_result = query.rating(rating_option)
st.table(rating_result)