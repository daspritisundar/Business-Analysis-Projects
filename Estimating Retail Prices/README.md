<img width="840" height="499" alt="image" src="https://github.com/user-attachments/assets/d785f7e3-d3b4-4f36-be41-448cdae655c5" />

## Estimating Retail Prices

## 📌 Overview  
Pricing strategy plays a pivotal role in retail competitiveness and profitability. This task involved building a **machine learning–based retail price prediction system**, which was subsequently deployed as an **interactive Streamlit web application**. The app allows users to input product details and instantly obtain predicted retail prices, supporting data-driven decision-making in product management and merchandising.

---

## 🌐 Live Demo  
👉 Access the deployed application here:  
**[Retail Price Prediction Web App](https://business-analysis-projects-xhsbtrehpr9znwstjinoz2.streamlit.app/)**  

The app enables experimentation with product attributes (category, brand, rating, warranty, power usage, etc.) to understand their impact on pricing.

---

## 🎯 Objectives  
- **Develop a predictive model** to estimate product prices based on structured product attributes.  
- **Identify key drivers of price** such as category, brand, technical specifications, and customer-facing features.  
- **Deploy a user-friendly tool** that integrates analytics into business workflows for real-time decision-making.  

---

## 🛠️ Methodology  

### 1. Data Preparation  
- **Features used:**  
  - *Categorical*: `Category`, `Brand`  
  - *Numerical*: `Weight (kg)`, `Rating`, `Warranty (years)`, `Power usage (Watts)`, `Feature score`  
- **Target variable:** `Retail Price`  
- **Preprocessing steps:**  
  - Applied **One-Hot Encoding** for categorical features.  
  - Standardized numerical variables using **StandardScaler**.  
  - Handled missing values and ensured dataset integrity.  

### 2. Model Development  
- Algorithm: **Linear Regression** (interpretable baseline).  
- Evaluation metric: **R² Score** (coefficient of determination).  
- Model trained on train/test split and validated for generalization.  
- Final model exported as `sklearn_price_model.pkl`.  

### 3. Deployment with Streamlit  
- Built an interactive web application (`retailpricepredictapp.py`).  
- Users provide product specifications via dropdowns and sliders.  
- Application displays:  
  - Model R² score (performance transparency).  
  - **Predicted retail price** (₹).  

---

## 📊 Key Findings  
- **Brand and Category** are strong categorical determinants of retail price.  
- **Technical attributes** like *warranty* and *power usage* directly influence pricing in electronics and appliances.  
- **Ratings and feature scores** serve as proxies for quality and customer value, which positively correlate with higher prices.  
- The model demonstrated reliable performance, making it suitable for practical benchmarking and strategic use.  

---

## 🚀 Business Applications  
1. **Strategic Pricing**  
   - Supports **value-based pricing** by aligning prices with product features and brand positioning.  

2. **Competitive Benchmarking**  
   - Retailers can compare estimated prices against competitor products in the same category.  

3. **Product Development**  
   - Helps managers simulate “what-if” scenarios (e.g., extending warranty or improving ratings) to see the impact on predicted price.  

4. **E-commerce Integration**  
   - Can be embedded into seller dashboards to recommend optimal product listing prices.  

---

## 🖥️ How to Run Locally  

1. Clone the repository:
   ```bash
   git clone https://github.com/daspritisundar/Business-Analytics-Projects.git
   cd Estimating_Retail_Prices

---

## 👤 Author

## Pritisundar Das

---

✨ This version positions Task 2 as a **full professional project** — it reads like a mini case study with clear methodology, findings, and applications.  

Would you like me to now also **draft the matching professional PDF Report** for Task 2 (like we did for Task 1), so it’s ready to drop into your `Reports/` folder?

