import streamlit as st
import sklearn
from sklearn import datasets
from sklearn import metrics
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

r = st.sidebar.radio("Navigation Menu",["Home","Avocado Price"])

if r=="Home":
    
    st.write("""
    # Avocado Price Predictive System
    #    
    """)
    st.image("Price.png")
    st.subheader("This App Predict the price of Avocado")
 


train=pd.read_csv('avocado (1).csv')
train.drop(['Unnamed: 0','region'],axis=1,inplace=True)

x = train.drop(['Date','AveragePrice'],axis=1)
y = train['AveragePrice']

le = preprocessing.LabelEncoder()
for i in x.columns:
    if x[i].dtype == 'object':
        x[i] = le.fit_transform(x[i].astype(str))
        
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x = scaler.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .2, random_state = 26)
from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(n_estimators = 250,n_jobs=-1)
rfr.fit(x_train,y_train)

if r == 'Avocado Price':
    st.header("Avocado Price Prediction")
    st.markdown("Please enter the following details about avocado sales:")

    Total_Volume = st.number_input(
        "Total Volume Sold",
        min_value=0.0,
        format="%.2f",
        help="Enter the total number of avocados sold (in units)."
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        small_avocados = st.number_input(
            "Small Avocados Sold (PLU 4046)", min_value=0, step=1,
            help="Number of small avocados sold."
        )
    with col2:
        medium_avocados = st.number_input(
            "Medium Avocados Sold (PLU 4225)", min_value=0, step=1,
            help="Number of medium avocados sold."
        )
    with col3:
        large_avocados = st.number_input(
            "Large Avocados Sold (PLU 4770)", min_value=0, step=1,
            help="Number of large avocados sold."
        )
    st.markdown("### Bag Details")
    Total_Bags = st.number_input(
        "Total Number of Bags", min_value=0, step=1,
        help="Total bags used for packaging avocados."
    )
    col4, col5, col6 = st.columns(3)
    with col4:
        small_bags = st.number_input(
            "Small Bags", min_value=0, step=1,
            help="Number of small bags."
        )
    with col5:
        large_bags = st.number_input(
            "Large Bags", min_value=0, step=1,
            help="Number of large bags."
        )
    with col6:
        extra_large_bags = st.number_input(
            "Extra Large Bags", min_value=0, step=1,
            help="Number of extra large bags."
        )
    avocado_type = st.selectbox(
        "Avocado Type",
        options=["Conventional", "Organic"],
        help="Select whether the avocados are conventional or organic."
    )
    year = st.number_input(
        "Year of Sale",
        min_value=2000,
        max_value=2100,
        step=1,
        help="Enter the year when the sale took place."
    )

    # Make prediction only when Predict button is clicked
    if st.button("Predict"):
        features = [[
            Total_Volume,
            small_avocados,
            medium_avocados,
            large_avocados,
            Total_Bags,
            small_bags,
            large_bags,
            extra_large_bags,
            1 if avocado_type == "Organic" else 0,
            year
        ]]
        ypred = rfr.predict(features)
        st.success(f"Your Predicted Avocado Price is: ${abs(ypred[0]):.2f}")
