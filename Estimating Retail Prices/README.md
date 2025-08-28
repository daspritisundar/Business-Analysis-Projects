<img width="840" height="499" alt="image" src="https://github.com/user-attachments/assets/d785f7e3-d3b4-4f36-be41-448cdae655c5" />

# Task 2: Estimating Retail Prices

##  Overview  
This task focuses on building a machine learning model to estimate retail prices using product-level features and deploying it as an interactive Streamlit app for real-time use.

---

##  Live App  
Explore the deployed Streamlit app here:  
**[Retail Price Prediction Web App](https://business-analysis-projects-xhsbtrehpr9znwstjinoz2.streamlit.app/)**

Use this app to input product features and instantly get a price estimate — a valuable tool for retail strategy and benchmarking.

---

##  Objective  
Model and predict retail prices based on product attributes (both categorical and numerical) to support competitive and profitability-driven pricing decisions.

---

##  Methodology  
1. **Data Processing**  
   - Features: `category`, `brand`, `weight`, `rating`, `warranty_years`, `power_usage`, `feature_score`  
   - Handle categoricals with One-Hot Encoding; scale numericals as needed.

2. **Model Training**  
   - Used **Linear Regression** to estimate price.  
   - Evaluated performance using R² on training and test sets.  
   - Saved the final model as `sklearn_price_model.pkl`.

3. **Deployment with Streamlit**  
   - Developed `retailpricepredictapp.py` to collect user inputs via widgets.  
   - Inputs include dropdowns (Category, Brand) and sliders/numeric inputs (Weight, Rating, etc.).  
   - On clicking "**Predict Price**", the app displays the model’s R² score and the predicted price.

---

##  Key Insights  
- **Price Drivers:** Both category-level attributes (e.g., brand and product type) and numeric features (e.g., rating, warranty) significantly influence retail pricing.  
- **Model transparency:** Linear regression enables interpretability, helping stakeholders understand which features impact price most.  
- **Real-time feedback:** The app allows dynamic experimentation — adjusting feature sliders reflects how price estimates change instantly.

---

##  Business Applications  
- **Product Managers** can estimate pricing impact when changing warranty or rating.  
- **Merchandisers** can benchmark prices in real time against competitive features.  
- **Analysts** can integrate this tool into dashboards for pricing insights and scenario testing.

---

##  How to Run Locally  
1. Clone this repository.  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
