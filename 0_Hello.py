import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to my Prediction App! 👋")

st.sidebar.success("Select a page above.")
st.sidebar.header("Hello")

st.markdown('<div style="text-align: justify;">For the current global scenario, air quality is a major concern. Many nations throughout the world suffer from severe air pollution, which has catastrophic health consequences or even death. Humanity has progressed tremendously in terms of technology during the previous century. However, there have been worldwide environmental implications as a result of this progress, most notably the burning of fossil fuels, which is required to drive automobiles, and the subsequent release of pollutants into the atmosphere. Human population increase is becoming an issue, and this overcrowding has resulted in a slew of negative environmental consequences. The most vital resource for human survival is air.<br><br></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">There are numerous key goals in this thesis. These include a desire to conduct a complete investigation of Brasovs pollution status, to identify the citys most polluted locations, and to detect any abnormalities in the citys sensor system.<br><br></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Another goal of the thesis is to construct Machine Learning methods that may be used to forecast the levels of contaminating compounds in an efficient and accurate manner. As a result, the goal is to develop an algorithm that will allow for the prediction of key pollutants over a period of time.<br><br></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Another goal of the project is to create a web application that allows users to see the results of the algorithm by selecting the desired substance and the time frame for which they want to see the anticipated data.<br><br></div>', unsafe_allow_html=True)

# st.markdown(
# """
# For the current global scenario, air quality is a major concern. Many nations throughout the world suffer from severe air pollution, which has catastrophic health consequences or even death. Humanity has progressed tremendously in terms of technology during the previous century. However, there have been worldwide environmental implications as a result of this progress, most notably the burning of fossil fuels, which is required to drive automobiles, and the subsequent release of pollutants into the atmosphere. Human population increase is becoming an issue, and this overcrowding has resulted in a slew of negative environmental consequences. The most vital resource for human survival is air.

# There are numerous key goals in this thesis. These include a desire to conduct a complete investigation of Brasov's pollution status, to identify the city's most polluted locations, and to detect any abnormalities in the city's sensor system.

# Another goal of the thesis is to construct Machine Learning methods that may be used to forecast the levels of contaminating compounds in an efficient and accurate manner. As a result, the goal is to develop an algorithm that will allow for the prediction of key pollutants over a period of time.

# Another goal of the project is to create a web application that allows users to see the results of the algorithm by selecting the desired substance and the time frame for which they want to see the anticipated data.
# """
# )

# st.markdown(
# """
#     My prediction app bla bla bla bla bla bla
#     bla bla bla bla bla bla bla bla bla bla bla bla bla bla
#     bla bla bla bla bla bla bla bla bla bla bla bla bla bla
#     bla bla bla bla bla bla bla bla bla bla bla bla bla bla.
# """
# )

# st.markdown(
# """
#     **👈 Select a page from the sidebar** to see more 
#     information about my page!
#     ### What you can see?
#     - Information about sensors in Brasov
#     - Air Quality standards
#     - Predictions results
# """
# )