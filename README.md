# Taxi_prediction
NYC Taxi Trip Duration Prediction
A Machine Learning project that predicts the duration of taxi trips in New York City using Linear Regression and geospatial feature engineering.
📌 Project Overview
This project aims to estimate taxi trip duration (in seconds) using features such as pickup location, dropoff location, time of day, and traffic-related indicators.
The project includes:
Data Cleaning
Feature Engineering
Linear Regression Model
Model Evaluation
Residual Diagnostics
Streamlit Web Application for predictions
Dataset
Dataset used: NYC Taxi Trip Duration Dataset
🔗 Kaggle Link
https://www.kaggle.com/competitions/nyc-taxi-trip-duration
The dataset contains information such as:
Pickup & dropoff coordinates
Pickup datetime
Passenger count
Trip duration
⚙️ Feature Engineering
The following features were created:
Passenger Count
Pickup Longitude & Latitude
Dropoff Longitude & Latitude
Distance (Haversine Formula)
Hour of pickup
Day of week
Rush hour indicator
Data Preprocessing
The dataset was cleaned using the following steps:
Converted datetime features
Extracted hour and day of week
Created rush hour indicator
Calculated distance using Haversine formula
Applied log transformation on trip duration
Removed extreme outliers
🤖 ## Model Used
Linear Regression
The model was trained using Scikit-learn.
Evaluation Metrics
R² Score
RMSE
Residual Plot
These metrics were used to analyze model bias and variance.
🌐 Streamlit Web Application
A Streamlit UI was developed so users can input trip details and get predictions.
## The interface allows users to enter:
Passenger count
Pickup location
Dropoff location
Distance
Pickup hour
Day of week
Rush hour indicator
## Project Structure
Taxi_predictor
│
├── train_cleaning.ipynb
├── model_training.ipynb
├── UI.py
├── README.md
└── .gitignore
## Technologies Used:
Python
Pandas
NumPy
Scikit-learn
Streamlit
Matplotlib
## How to Run the Project

1. Clone the repository

git clone https://github.com/Varshithakadiyam/Taxi_prediction.git

2. Install required libraries

pip install pandas numpy scikit-learn streamlit matplotlib

3. Run the Streamlit application

streamlit run UI.py

