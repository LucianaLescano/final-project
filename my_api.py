import streamlit as st
import src.data as data

st.markdown("<h1 style='text-align: center; color: black;'>Skincare API</h1>", unsafe_allow_html=True)


@st.cache
def load_data():
    dataframe = data.loading_data()
    return dataframe

all_data = load_data()

# Select a type of product among options
cat = "Category"
prod = st.selectbox(
    'Choose a type of product',
     data.choice(cat))
'You selected: ', prod
