import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to my Prediction App! 👋")

st.sidebar.success("Select a page above.")
st.sidebar.header("Hello")

st.markdown(
"""
    My prediction app bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla.
"""
)

st.markdown(
"""
    **👈 Select a page from the sidebar** to see more 
    information about my page!
    ### What you can see?
    - Information about sensors in Brasov
    - Air Quality standards
    - Predictions results
"""
)