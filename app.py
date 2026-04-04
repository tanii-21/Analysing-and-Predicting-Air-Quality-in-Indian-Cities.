import streamlit as st

st.title("Air Quality Prediction - India")

pm25 = st.number_input("Enter PM2.5 (µg/m³)")
pm10 = st.number_input("Enter PM10 (µg/m³)")

def get_aqi_category(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Satisfactory"
    elif pm25 <= 200:
        return "Moderate"
    elif pm25 <= 300:
        return "Poor"
    elif pm25 <= 400:
        return "Very Poor"
    else:
        return "Severe"

if st.button("Predict AQI"):
    aqi = (pm25 * 0.7) + (pm10 * 0.3)
    category = get_aqi_category(pm25)

    st.success(f"Predicted AQI: {int(aqi)}")
    st.info(f"Air Quality Category: {category}")
