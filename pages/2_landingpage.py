import streamlit as st 

pg_bg_img = """ 
<style>
    [data-testid="stAppViewContainer"]{
          background-image: url("https://img.freepik.com/free-vector/flat-background-world-vegetarian-day_23-2149612310.jpg?w=996&t=st=1680391170~exp=1680391770~hmac=d22ce347a8f51df3994e6813c8f00ce67f0dc57bb6fb6cbc03542a2ac41bf352");
          background-size:cover;
    }
</style>
"""

st.markdown(pg_bg_img,unsafe_allow_html=True)
st.header(":red[welcome to ur first healty diet]")