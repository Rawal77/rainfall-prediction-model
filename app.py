import streamlit as st
import pandas as pd
import pickle

# Load the trained model and feature names from the pickle file
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

# Extract the model and feature names
model = model_data["model"]
feature_names = model_data["feature_names"]

# Streamlit UI to get user input
st.title("Rainfall Prediction App")
st.write("This app predicts whether it will rain based on weather conditions.")

# Creating input fields for each feature
pressure = st.number_input("Pressure (hPa)", value=1015.9)
maxtemp = st.number_input("Max Temperature (°C)", value=19.9)
humidity = st.number_input("Humidity (%)", value=81)
cloud = st.number_input("Cloud Cover (%)", value=95)
sunshine = st.number_input("Sunshine (hrs)", value=0.0)
windspeed = st.number_input("Windspeed (km/h)", value=40.0)
dewpoint = st.number_input("Dewpoint (°C)", value=13.7)

# Prepare the input data
input_data = (pressure, maxtemp, humidity, cloud, sunshine, windspeed, dewpoint)
input_df = pd.DataFrame([input_data], columns=feature_names)

# Button to make the prediction
if st.button("Predict Rainfall"):
    prediction = model.predict(input_df)
    
    # Display the result
    if prediction[0] == 1:
        st.write("Prediction: **Rainfall**")
    else:
        st.write("Prediction: **No Rainfall**")

