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
    st.image("avocado .png")
    st.subheader("This App Predict the price of Avocado ->")
    st.text("Avocado Price Prediction")


train=pd.read_csv('avocado.csv')
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

if r=='Avocado Price':
    st.header("Know the Price of Avocado")
    Total_Volume=st.number_input(" Total number of avocados sold")
    blue4046=st.number_input("Total number of small avocados sold (PLU 4046)")
    b4225=st.number_input("Total number of medium avocados sold (PLU 4225)")
    d4770=st.number_input("Total number of large avocados sold (PLU 4770)")
    Total_Bags=st.number_input("Total number of bags")
    Small_Bags=st.number_input("Total number of small bags")
    Large_Bags=st.number_input("Total number of large bags")
    XLarge_Bags=st.number_input("Total number of extra large bags")
    type=st.number_input("whether the price/amount is for conventional or organic")
    year=st.number_input("Year of sale")
    
    
    ypred=rfr.predict([[Total_Volume,blue4046,b4225,d4770,Total_Bags,Small_Bags,Large_Bags,XLarge_Bags,type,year]])
    if(st.button("Predict")):
        st.success(f"Your Predicted Avocado Price Is {abs(ypred)}")
    
    
        
        
    
