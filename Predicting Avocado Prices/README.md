<img width="500" height="261" alt="image" src="https://github.com/user-attachments/assets/18f0059e-71e6-4ed3-b9c2-f38c1f47ba16" />


# Task 4: Predicting Avocado Prices 🥑

## 📌 Overview  
Agricultural commodities like avocados experience strong **seasonal, demand, and supply fluctuations** that directly affect their prices. Accurate price forecasting helps **farmers, retailers, supply chain managers, and policymakers** in making informed decisions.  

In this task, I developed and deployed an **interactive machine learning application** that predicts avocado prices based on **sales volume, product size distribution, packaging information, market type, and year**. The app provides real-time insights and allows users to simulate different market conditions.  

---

## 🌐 Live Demo  
👉 Try the deployed app here:  
**[Avocado Price Predictor Web App](https://business-analysis-projects-bbt2jvoefhjrsnzjwo3qzr.streamlit.app/)**  

The app allows users to input features such as total volume sold, PLU sizes, packaging type, avocado type, and year — and instantly receive a **predicted market price**.

---

## 🎯 Objectives  
- Analyze historical avocado sales data to capture pricing trends.  
- Build a **robust ML model (Random Forest)** to predict avocado prices.  
- Deploy a **Streamlit-based interactive web app** for real-time forecasting.  
- Provide **business insights** for retailers, farmers, and supply chain managers.  

---

## 🛠️ Methodology  

### 1. Data Preprocessing  
- Removed irrelevant columns (`Unnamed: 0`, `region`).  
- Encoded categorical variables (*Conventional/Organic*).  
- Standardized features with **StandardScaler**.  
- Split dataset into **train (80%)** and **test (20%)** sets.  

### 2. Model Development  
- Algorithm: **Random Forest Regressor** (250 estimators).  
- Train-Test Evaluation:  
  - **Training Accuracy:** ~0.98 (Excellent fit).  
  - **Testing Accuracy:** ~0.91 (Reliable generalization).  

### 3. Streamlit Application  
- **Home Page**: Project overview, methodology, and model performance.  
- **Price Predictor**: User inputs sales & product details → app predicts avocado price in real time.  
- **Model Performance**: Displays training vs testing scores, algorithm configuration, and feature information.  

---

## 📊 Key Features of the App  
- ✅ **Real-time avocado price prediction** based on user inputs.  
- ✅ **Clear model performance metrics** (train/test accuracy).  
- ✅ **Interactive and user-friendly design** with dropdowns, sliders, and numeric inputs.  
- ✅ **Insights into key features** (volume, packaging, type, seasonality).  
- ✅ **Deployment-ready** for business and academic use cases.  

---

## 🚀 Business Applications  
1. **Retailers** – Plan procurement & promotions around predicted seasonal prices.  
2. **Farmers** – Optimize harvest and selling periods to maximize returns.  
3. **Supply Chain Managers** – Anticipate disruptions and adjust logistics accordingly.  
4. **Policy Analysts** – Monitor perishable food prices for inflation and trade planning.  

---

## 🖥️ How to Run Locally  

1. Clone the repository:
   ```bash
   git clone https://github.com/daspritisundar/Business-Analytics-Projects.git
   cd Task4_Predicting_Avocado_Prices/App

---
## 👤 Author

## Pritisundar Das

---
## ✅ Task Status

Completed — ML model developed, evaluated, and deployed as a professional-grade interactive app.
