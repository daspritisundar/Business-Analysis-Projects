import streamlit as st
import pandas as pd
import os
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.metrics import accuracy_score


def train_model():
    df = pd.read_csv(r"C:\Users\91943\Downloads\Estimating Retail Prices\Data_product.csv")
    categorical=['category','brand']
    numerical=['weight_kg','rating','warranty_years','power_usage_watts','feature_score']
    target='price'

    encoder=OneHotEncoder(sparse_output=False)
    encoded_cat=encoder.fit_transform(df[categorical])
    scaler=StandardScaler()
    scaled_num=scaler.fit_transform(df[numerical])


    X=np.hstack([encoded_cat,scaled_num])
    y=df[target].values

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)
    model=LinearRegression()
    model.fit(X_train,y_train)
    score=model.score(X_test,y_test)

    joblib.dump((model,encoder,scaler), 'model_encoder_scaler.joblib')
    print(score)
def predict_price(data_dict):
  model,encoder,scaler=joblib.load('/content/model_encoder_scaler.joblib')
  cat_features=[[data_dict['category'],data_dict['brand']]]
  num_features=[[data_dict['weight_kg'],data_dict['rating'],data_dict['warranty_years'],data_dict['power_usage_watts'],data_dict['feature_score']]]

  encoded_cat=encoder.transform(cat_features)
  scaled_num=scaler.transform(num_features)
  input_data=np.hstack([encoded_cat,scaled_num])
  prediction=model.predict(input_data)
  return round(float(prediction[0]),2)

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

if st.button("Predict Price"):
    score = train_model()
    st.success(f"📈 Model Score: {score}")
    price = predict_price(user_input)
    st.success(f"💵 Estimated Price: ₹{price}")
