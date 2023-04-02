import streamlit as st
import streamlit as st
from PIL import Image
import glob


st.set_page_config(
    page_title='diet plan app',
    page_icon='🥑'
)

pg_bg_img = """ 
<style>
    [data-testid="stAppViewContainer"]{
          background-image: linear-gradient(to bottom right, red, rgba(255, 165, 0,0.7));
</style>
"""

st.markdown(pg_bg_img,unsafe_allow_html=True)
st.title('welcome aman ! glad to have u 😊')
st.sidebar.success('')


# image_files = load_images()

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(label="steps 🚶", value="8000", delta="12000")
with c2:
    st.metric(label="calories burned ", value="40", delta="120")
with c3:
    st.metric(label="heart rate ",value="80", delta="75")
with c4:
    st.metric(label="weight", value="70", delta="65")

