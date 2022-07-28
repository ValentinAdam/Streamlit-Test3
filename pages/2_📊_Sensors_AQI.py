import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sensors AQI",
    page_icon="📊",
)

st.write("# Air Quality Index (AQI) Basics 📊")

# st.markdown(
#     """
# AQI standards explained

# """
# )

# st.markdown('<div style="text-align: justify;"><i>Work in progress</i></div>', unsafe_allow_html=True)


from PIL import Image

st.write("Air Quality Index (AQI) Standards for CO2")
image_co2 = Image.open('images/AQI_CO2.png')
st.image(image_co2)

st.write("Air Quality Index (AQI) Standards for NO2")
image_no2 = Image.open('images/AQI_NO2.png')
st.image(image_no2)

st.write("Air Quality Index (AQI) Standards for SO2")
image_so2 = Image.open('images/AQI_SO2.png')
st.image(image_so2)

st.write("Air Quality Index (AQI) Standards for O3")
image_o3 = Image.open('images/AQI_O3.png')
st.image(image_o3)

st.write("Air Quality Index (AQI) Standards for PM10")
image_pm10 = Image.open('images/AQI_PM10.png')
st.image(image_pm10)

st.write("Air Quality Index (AQI) Standards for PM25")
image_pm25 = Image.open('images/AQI_PM25.png')
st.image(image_pm25)