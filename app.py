import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page setup
st.set_page_config(page_title="Accident Severity Predictor")
st.title("🚗 Accident Severity Prediction App")
st.write("Enter all accident details below:")

# =========================
# USER INPUTS (NO DEFAULT VALUES)
# =========================

start_lat = st.number_input("Start_Lat")
start_lng = st.number_input("Start_Lng")
distance = st.number_input("Distance(mi)")
temperature = st.number_input("Temperature(F)")
humidity = st.number_input("Humidity(%)")
pressure = st.number_input("Pressure(in)")
visibility = st.number_input("Visibility(mi)")
wind_speed = st.number_input("Wind_Speed(mph)")
precipitation = st.number_input("Precipitation(in)")
end_lat = st.number_input("End_Lat")
end_lng = st.number_input("End_Lng")
wind_chill = st.number_input("Wind_Chill(F)")

# =========================
# PREDICTION
# =========================

if st.button("Predict Severity"):

    # Create input dataframe
    new_data = pd.DataFrame([{
        "Start_Lat": start_lat,
        "Start_Lng": start_lng,
        "Distance(mi)": distance,
        "Temperature(F)": temperature,
        "Humidity(%)": humidity,
        "Pressure(in)": pressure,
        "Visibility(mi)": visibility,
        "Wind_Speed(mph)": wind_speed,
        "Precipitation(in)": precipitation,
        "End_Lat": end_lat,
        "End_Lng": end_lng,
        "Wind_Chill(F)": wind_chill
    }])

    st.subheader("Input Data")
    st.write(new_data)

    # Prediction
    prediction = model.predict(new_data)

    severity = prediction[0]

    st.success(f"Predicted Severity: {severity}")

    # Interpretation
    if severity == 1:
        st.info("🟢 Low Severity Accident")
    elif severity == 2:
        st.warning("🟡 Moderate Severity Accident")
    elif severity == 3:
        st.warning("🟠 High Severity Accident")
    elif severity == 4:
        st.error("🔴 Very Severe Accident")