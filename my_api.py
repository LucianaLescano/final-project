import streamlit as st
from PIL import Image
import pandas as pd 
import webbrowser

from tools import options, query

### PRUEBA:

img_one = Image.open("images/one.png")
st.image(img_one, width=700, caption="")

######### 1º PART

st.header("What about having your own personalized skincare routine?")
st.write(" ")

preference = st.selectbox("", ["Please select one", "Let’s go with the basic!", "Let’s go deep inside with the skincare routine!"])
#try:
if preference == 'Please select one':
    st.stop()
    st.success("Perfect!")

elif preference == "Let’s go with the basic!":
    #if st.button("Let's start by some basics!"):
    st.write(" ")
    img_two = Image.open("images/two.png")
    st.image(img_two, width=700, caption="Skin type infography")
    st.subheader("What's your skin type:")
    routine_skin_option = st.radio("", options.list_type_skin)
    # st.write(routine_skin_option)
    routine_skin_option_for_query = str(routine_skin_option)
    st.write(" ")
    st.subheader("How much money do you want to spend?")
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
    st.subheader("To cheer you up to have a wonderful skincare routine. Here you have available all the links to the products:")
    try:
        st.write(" ")
        st.markdown("Cleansers")
        skincare_routine_result_one_url = query.cleanser_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
        for i in range(0,3):
                url = skincare_routine_result_one_url[i].get('URL')
                if st.button(f"{skincare_routine_result_one_url[i].get('Name')}"):
                    webbrowser.open_new_tab(url)
    except:
        st.button("Basic: Sorry! There is no other cleansers we can offer you.")
    try:
        st.write(" ")
        st.markdown("Moisturizers")
        skincare_routine_result_two_url = query.moist_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
        for i in range(0,3):
                url = skincare_routine_result_two_url[i].get('URL')
                if st.button(f"{skincare_routine_result_two_url[i].get('Name')}"):
                    webbrowser.open_new_tab(url)
    except:
        st.button("Basic: Sorry! There is no other moisturizers we can offer you.")
    try:
        st.write(" ")
        st.markdown("Sunscreens")
        skincare_routine_result_three_url = query.sun_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
        for i in range(0,3):
                url = skincare_routine_result_three_url[i].get('URL')
                if st.button(f"{skincare_routine_result_three_url[i].get('Name')}"):
                    webbrowser.open_new_tab(url)
    except:
        st.button("Basic: Sorry! There is no other sunscreens we can offer you.")

elif preference == "Let’s go deep inside with the skincare routine!":
    #if st.button("Let's start by some basics!"):
    st.write(" ")
    img_three = Image.open("images/two.png")
    st.image(img_three, width=700, caption="Skin type infography")
    st.subheader("What's your skin type:")
    routine_skin_option = st.radio("", options.list_type_skin)
    # st.write(routine_skin_option)
    routine_skin_option_for_query = str(routine_skin_option)
    st.write(" ")
    st.subheader("How much money do you want to spend?")
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
    st.subheader("To cheer you up to have a wonderful skincare routine. Here you have available all the links to the products:")
    try:
        st.write(" ")
        st.markdown("Cleansers")
        skincare_routine_result_one_url = query.cleanser_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
        for i in range(0,3):
                url = skincare_routine_result_one_url[i].get('URL')
                if st.button(f"{skincare_routine_result_one_url[i].get('Name')}"):
                    webbrowser.open_new_tab(url)
    except:
        st.button("Pro: Sorry! There is no other cleansers we can offer you.")
    try:
        st.write(" ")
        st.markdown("Toners")
        skincare_routine_result_four_url = query.ton_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
        for i in range(0,3):
                url = skincare_routine_result_four_url[i].get('URL')
                if st.button(f"{skincare_routine_result_four_url[i].get('Name')}"):
                    webbrowser.open_new_tab(url)
    except:
        st.button("Pro: Sorry! There is no other toners we can offer you.")
    try:
        st.write(" ")
        st.markdown("Serums")
        skincare_routine_result_five_url = query.serum_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
        for i in range(0,3):
                url = skincare_routine_result_five_url[i].get('URL')
                if st.button(f"{skincare_routine_result_five_url[i].get('Name')}"):
                    webbrowser.open_new_tab(url)
    except:
        st.button("Pro: Sorry! There is no other serums we can offer you.")
    try:
        st.write(" ")
        st.markdown("Moisturizers")
        skincare_routine_result_two_url = query.moist_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
        for i in range(0,3):
                url = skincare_routine_result_two_url[i].get('URL')
                if st.button(f"{skincare_routine_result_two_url[i].get('Name')}"):
                    webbrowser.open_new_tab(url)
    except:
        st.button("Pro: Sorry! There is no other moisturizers we can offer you.")
    try:
        st.write(" ")
        st.markdown("Sunscreens")
        skincare_routine_result_three_url = query.sun_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query)
        for i in range(0,3):
                url = skincare_routine_result_three_url[i].get('URL')
                if st.button(f"{skincare_routine_result_three_url[i].get('Name')}"):
                    webbrowser.open_new_tab(url)
    except:
        st.button("Pro: Sorry! There is no other sunscreens we can offer you.")
#except:
#    st.stop()
#    st.write("Sorry!")

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