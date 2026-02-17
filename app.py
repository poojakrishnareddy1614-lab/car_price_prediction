import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("car_price_model.pkl")

st.title("🚗 Car Price Prediction App")

name = st.text_input("Car Name")
company = st.text_input("Company")
year = st.number_input("Year", min_value=1990, max_value=2025)
kms = st.number_input("Kilometers Driven", min_value=0)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])

if st.button("Predict Price"):
    
    input_df = pd.DataFrame({
        'name': [name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms],
        'fuel_type': [fuel]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Price: ₹ {int(prediction):,}")