import streamlit as st 
import streamlit as st

pg_bg_img = """ 
<style>
    [data-testid="stAppViewContainer"]{
          background-image: linear-gradient(to bottom right, red, rgba(255, 165, 0,0.7));
</style>
"""
st.markdown(pg_bg_img,unsafe_allow_html=True)

st.title("Register")



form = st.form("my_form")
form.text_input("NAME")
form.text_input("EMAIL")
form.text_input("AGE")
form.text_input("ANY DISEASE")

form.form_submit_button(label = 'signup')
