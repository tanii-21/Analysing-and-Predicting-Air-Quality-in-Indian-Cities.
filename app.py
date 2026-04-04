import streamlit as st

st.title("Air Quality Prediction - India")

pm25 = st.number_input("Enter PM2.5")
pm10 = st.number_input("Enter PM10")

if st.button("Predict AQI"):
    aqi = (pm25 * 0.6) + (pm10 * 0.4)
    st.success(f"Predicted AQI: {int(aqi)}")