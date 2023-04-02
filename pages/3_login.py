import streamlit as st 
import webbrowser
st.title("login")


import streamlit as st

pg_bg_img = """ 
<style>
    [data-testid="stAppViewContainer"]{
          background-image: linear-gradient(to bottom right, red, rgba(255, 165, 0,0.7));
</style>
"""
st.markdown(pg_bg_img,unsafe_allow_html=True)


form = st.form("my_form")
form.text_input("USERNAME")
form.text_input("PASSWORD")

form.form_submit_button(label = 'login',on_click=webbrowser.open("localhost:8501/"))
