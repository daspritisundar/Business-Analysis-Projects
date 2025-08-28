import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import warnings

# Suppress all warnings
warnings.filterwarnings('ignore')

# --- Data Loading and Model Training ---
# @st.cache_data is a decorator that caches the function's output.
# This prevents reloading the data and retraining the model every time
# a user interacts with the app, making it significantly faster.
@st.cache_data
def load_and_train_model():
    """Loads the data and trains the RandomForestRegressor model."""
    try:
        train = pd.read_csv('avocado(1).csv')
    except FileNotFoundError:
        st.error("Data file 'avocado(1).csv' not found. Please ensure the file path is correct.")
        return None, None

    # Drop unnecessary columns
    train.drop(['Unnamed: 0', 'region'], axis=1, inplace=True)

    # Separate features and target variable
    x = train.drop(['Date', 'AveragePrice'], axis=1)
    y = train['AveragePrice']

    # Encode categorical features
    le = LabelEncoder()
    for col in x.columns:
        if x[col].dtype == 'object':
            x[col] = le.fit_transform(x[col].astype(str))

    # Scale numerical features
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    # Split data for training
    x_train, _, y_train, _ = train_test_split(x_scaled, y, test_size=0.2, random_state=26)

    # Train the model
    rfr = RandomForestRegressor(n_estimators=250, n_jobs=-1, random_state=42)
    rfr.fit(x_train, y_train)

    return rfr, scaler, le, x.columns

# Load and train the model once
rfr, scaler, le, feature_names = load_and_train_model()

if rfr is None:
    st.stop()

# --- Streamlit UI and Logic ---
st.set_page_config(
    page_title="Avocado Price Predictor",
    page_icon="🥑",
    layout="wide"
)

# Navigation
r = st.sidebar.radio("Navigation Menu", ["Home", "Avocado Price Predictor"])

# Home Page
if r == "Home":
    st.title("🥑 Avocado Price Prediction System")
    st.markdown("""
        <div style="text-align: center;">
            <p style="font-size: 1.2em;">Welcome to the Avocado Price Predictor! This app uses machine learning to forecast the price of avocados based on various market factors.</p>
        </div>
    """, unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1543781702-53b00c592edb?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D") # Adding a high-quality, relevant image
    st.subheader("How It Works:")
    st.markdown("""
    - **Step 1:** Select "Avocado Price Predictor" from the navigation menu on the left.
    - **Step 2:** Enter the requested details about the avocado sales data.
    - **Step 3:** Click the "Predict Price" button to get the estimated average price.
    """)
    st.info("The model is trained on historical avocado price data from 2015 to 2018.")

# Prediction Page
if r == 'Avocado Price Predictor':
    st.header("🛒 Predict the Price of an Avocado")
    st.write("Please enter the following details to get a price prediction.")
    
    # Use st.columns for a better layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Volume & Bag Information")
        total_volume = st.number_input("Total Volume", min_value=0.0, format="%.2f", help="Total number of avocados sold.")
        plu_4046 = st.number_input("PLU 4046 Volume", min_value=0.0, format="%.2f", help="Total volume of small avocados (PLU 4046).")
        plu_4225 = st.number_input("PLU 4225 Volume", min_value=0.0, format="%.2f", help="Total volume of medium avocados (PLU 4225).")
        plu_4770 = st.number_input("PLU 4770 Volume", min_value=0.0, format="%.2f", help="Total volume of large avocados (PLU 4770).")
        total_bags = st.number_input("Total Bags", min_value=0.0, format="%.2f", help="Total number of bags sold.")

    with col2:
        st.subheader("Bags, Type & Year")
        small_bags = st.number_input("Small Bags", min_value=0.0, format="%.2f", help="Total number of small bags.")
        large_bags = st.number_input("Large Bags", min_value=0.0, format="%.2f", help="Total number of large bags.")
        xlarge_bags = st.number_input("Extra Large Bags", min_value=0.0, format="%.2f", help="Total number of extra large bags.")
        
        # Use a dropdown selectbox for 'type'
        type_options = {'conventional': 0, 'organic': 1}
        selected_type = st.selectbox(
            "Avocado Type",
            options=list(type_options.keys()),
            help="Select the type of avocado (Conventional or Organic)."
        )
        type_value = type_options[selected_type]
        
        year = st.selectbox(
            "Year of Sale",
            options=range(2000, 2026), 
            help="The year of the sale."
        )

    # Prediction button
    if st.button("Predict Price", use_container_width=True):
        if total_volume + plu_4046 + plu_4225 + plu_4770 + total_bags + small_bags + large_bags + xlarge_bags > 0:
            # Create a DataFrame for the user input
            input_df = pd.DataFrame([[total_volume, plu_4046, plu_4225, plu_4770, total_bags,
                                      small_bags, large_bags, xlarge_bags, type_value, year]],
                                    columns=feature_names)
            
            # Scale the input data using the same scaler used for training
            input_scaled = scaler.transform(input_df)
            
            # Predict the price
            prediction = rfr.predict(input_scaled)[0]
            
            # Display the prediction in a professional way
            st.success(f"### 💰 Predicted Average Price: ${prediction:.2f}")
            st.markdown("The price is a predicted average per avocado.")
        else:
            st.warning("Please enter valid positive values to get a prediction.")
