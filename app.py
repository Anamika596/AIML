import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🚗 Accident Severity Prediction")
st.write("Enter all 12 feature values and click Predict")

# 12 input fields
start_lat = st.number_input("Start_Lat", value=0.0)
start_lng = st.number_input("Start_Lng", value=0.0)
distance = st.number_input("Distance(mi)", value=0.0)
temperature = st.number_input("Temperature(F)", value=0.0)
humidity = st.number_input("Humidity(%)", value=0.0)
pressure = st.number_input("Pressure(in)", value=0.0)
visibility = st.number_input("Visibility(mi)", value=0.0)
wind_speed = st.number_input("Wind_Speed(mph)", value=0.0)
precipitation = st.number_input("Precipitation(in)", value=0.0)
end_lat = st.number_input("End_Lat", value=0.0)
end_lng = st.number_input("End_Lng", value=0.0)
wind_chill = st.number_input("Wind_Chill(F)", value=0.0)

# Predict button
if st.button("Predict"):
    # Create input DataFrame with the exact 12 columns used by the model
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

    # Predict using the trained model
    prediction = model.predict(new_data)

    # Display result
    st.success(f"Predicted Severity: {prediction[0]}")