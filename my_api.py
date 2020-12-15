import streamlit as st
from PIL import Image

import tools.query as query

### PRUEBA:
st.title("Radiant Qara")
st.header("1 Header")
st.subheader("1 Subheader")
st.text("Holi")
st.markdown("Holi in markdown")

img = Image.open("images/one.jpg")
st.image(img, width=300, caption="skincare")

#### FOR REAL:

