import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("taxi_model.pkl", "rb"))

st.title("NYC Taxi Trip Duration Predictor")

st.write("Enter trip details to predict taxi trip duration")

# Inputs
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)

pickup_longitude = st.number_input("Pickup Longitude", value=-73.98)
pickup_latitude = st.number_input("Pickup Latitude", value=40.75)

dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.99)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.76)

distance = st.number_input("Distance (km)", min_value=0.0, value=1.0)

hour = st.slider("Pickup Hour", 0, 23, 10)

day_of_week = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 2)

rush_hour = st.selectbox("Rush Hour", [0, 1])

# Prediction
if st.button("Predict Duration"):

    features = np.array([[passenger_count,
                          pickup_longitude,
                          pickup_latitude,
                          dropoff_longitude,
                          dropoff_latitude,
                          hour,
                          day_of_week,
                          rush_hour,
                          distance]])

    prediction = model.predict(features)

    st.success(f"Predicted Log Trip Duration: {prediction[0]}")