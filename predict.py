import streamlit as st
import pandas as pd
import os
import numpy as np
from predict import predict_price
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score

# Function to load model
def load_model():
    model_path = os.path.join('model/sklearn_price_model.pkl')
    if os.path.exists(model_path):
        try:
            return joblib.load(model_path), True
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None, False
    else:
        st.error("Model not found in the model directory. Please ensure the model is properly saved.")
        return None, False
  
st.title("💰 Product Price Estimator")

category = st.selectbox("Category", ['Electronics', 'Furniture', 'Apparel', 'Kitchen', 'Toys'])
brand = st.selectbox("Brand", ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE'])
weight_kg = st.slider("Weight (kg)", 0.1, 50.0, 10.0)
rating = st.slider("Rating (1-5)", 1.0, 5.0, 4.0)
warranty_years = st.slider("Warranty (years)", 0, 5, 1)
power_usage_watts = st.slider("Power Usage (Watts)", 0, 2000, 500)
feature_score = st.slider("Feature Score (0-100)", 0.0, 100.0, 50.0)

user_input = {
    'category': category,
    'brand': brand,
    'weight_kg': weight_kg,
    'rating': rating,
    'warranty_years': warranty_years,
    'power_usage_watts': power_usage_watts,
    'feature_score': feature_score
}

# Load the model when the app starts
model_data, model_loaded = load_model()

if model_loaded:
    st.info(f"📈 Model loaded successfully from model directory.")

if st.button("Predict Price"):
    if model_loaded:
        price = predict_price(user_input)  # Use the default function without passing model
        st.success(f"💵 Estimated Price: ₹{price}")
    else:
        st.error("Cannot make predictions without a trained model.")
