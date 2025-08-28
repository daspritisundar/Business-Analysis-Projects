import streamlit as st
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Avocado Price Predictor",
    page_icon="🥑",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .sub-header {
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }
    .prediction-result {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #2E8B57;
        padding: 1rem;
        border-radius: 10px;
        background-color: #f0f8f0;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for caching model
@st.cache_data
def load_and_train_model():
    """Load data and train the model"""
    try:
        # Load the dataset
        train = pd.read_csv('Predicting Avocado Prices/Data/avocado.csv')
        
        # Data preprocessing
        train.drop(['Unnamed: 0', 'region'], axis=1, inplace=True)
        x = train.drop(['Date', 'AveragePrice'], axis=1)
        y = train['AveragePrice']
        
        # Label encoding for categorical variables
        le = preprocessing.LabelEncoder()
        for i in x.columns:
            if x[i].dtype == 'object':
                x[i] = le.fit_transform(x[i].astype(str))
        
        # Feature scaling
        scaler = StandardScaler()
        x_scaled = scaler.fit_transform(x)
        
        # Train-test split
        x_train, x_test, y_train, y_test = train_test_split(
            x_scaled, y, test_size=0.2, random_state=26
        )
        
        # Train Random Forest model
        rfr = RandomForestRegressor(n_estimators=250, n_jobs=-1, random_state=26)
        rfr.fit(x_train, y_train)
        
        # Calculate model performance
        train_score = rfr.score(x_train, y_train)
        test_score = rfr.score(x_test, y_test)
        
        return rfr, scaler, le, train_score, test_score
        
    except FileNotFoundError:
        st.error("❌ Dataset file not found. Please ensure 'avocado.csv' is in the correct location.")
        return None, None, None, None, None
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        return None, None, None, None, None

# Load model
rfr, scaler, le, train_score, test_score = load_and_train_model()

# Sidebar navigation
st.sidebar.markdown("## 🧭 Navigation")
r = st.sidebar.radio(
    "Choose a section:",
    ["🏠 Home", "🥑 Price Predictor", "📊 Model Performance"],
    help="Select the section you want to explore"
)

# Home Page
if r == "🏠 Home":
    st.markdown('<h1 class="main-header">🥑 Avocado Price Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Advanced Machine Learning System for Avocado Price Prediction</p>', unsafe_allow_html=True)
    
    # Create columns for better layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ### Welcome to the Avocado Price Prediction System! 🎯
        
        This intelligent application uses advanced machine learning algorithms to predict avocado prices 
        based on various market factors including:
        
        - **Sales Volume Data** 📈
        - **Product Size Categories** 📏
        - **Packaging Information** 📦
        - **Market Type & Seasonality** 🗓️
        
        #### How It Works:
        1. Navigate to the **Price Predictor** section
        2. Enter your avocado sales data
        3. Get instant price predictions with high accuracy
        
        #### Key Features:
        - ✅ **Real-time Predictions**
        - ✅ **User-friendly Interface**
        - ✅ **High Accuracy Model**
        - ✅ **Professional Analysis**
        """)
    
    # Add some metrics if model is loaded
    if rfr is not None:
        st.markdown("---")
        st.markdown("### 📊 Model Performance")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Training Accuracy", f"{train_score:.3f}", delta="Excellent")
        with col2:
            st.metric("Testing Accuracy", f"{test_score:.3f}", delta="Reliable")
        with col3:
            st.metric("Model Type", "Random Forest", delta="Advanced ML")

# Price Predictor Page
elif r == "🥑 Price Predictor":
    if rfr is None:
        st.error("❌ Model not available. Please check the data file.")
        st.stop()
    
    st.markdown('<h1 class="main-header">🥑 Avocado Price Prediction</h1>', unsafe_allow_html=True)
    st.markdown("### Please provide the following market information:")
    
    # Create form for better user experience
    with st.form("prediction_form"):
        # Volume Information
        st.markdown("#### 📊 Sales Volume Information")
        col1, col2 = st.columns(2)
        
        with col1:
            Total_Volume = st.number_input(
                "Total Volume Sold (units)",
                min_value=0.0,
                value=10000.0,
                step=100.0,
                format="%.2f",
                help="Enter the total number of avocados sold"
            )
        
        with col2:
            Total_Bags = st.number_input(
                "Total Number of Bags",
                min_value=0,
                value=1000,
                step=10,
                help="Total bags used for packaging"
            )
        
        # Product Size Categories
        st.markdown("#### 📏 Product Size Categories (PLU Codes)")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            small_avocados = st.number_input(
                "Small Avocados (PLU 4046)",
                min_value=0,
                value=2000,
                step=50,
                help="Number of small avocados sold"
            )
        
        with col2:
            medium_avocados = st.number_input(
                "Medium Avocados (PLU 4225)",
                min_value=0,
                value=3000,
                step=50,
                help="Number of medium avocados sold"
            )
        
        with col3:
            large_avocados = st.number_input(
                "Large Avocados (PLU 4770)",
                min_value=0,
                value=2000,
                step=50,
                help="Number of large avocados sold"
            )
        
        # Bag Size Distribution
        st.markdown("#### 📦 Bag Size Distribution")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Small_Bags = st.number_input(
                "Small Bags",
                min_value=0,
                value=300,
                step=10,
                help="Number of small bags"
            )
        
        with col2:
            Large_Bags = st.number_input(
                "Large Bags",
                min_value=0,
                value=200,
                step=10,
                help="Number of large bags"
            )
        
        with col3:
            XLarge_Bags = st.number_input(
                "Extra Large Bags",
                min_value=0,
                value=100,
                step=5,
                help="Number of extra large bags"
            )
        
        # Market Information
        st.markdown("#### 🏪 Market Information")
        col1, col2 = st.columns(2)
        
        with col1:
            avocado_type = st.selectbox(
                "Avocado Type",
                options=["Conventional", "Organic"],
                index=0,
                help="Select the type of avocados"
            )
        
        with col2:
            year = st.number_input(
                "Year of Sale",
                min_value=2015,
                max_value=2030,
                value=2024,
                step=1,
                help="Year when the sale occurred"
            )
        
        # Prediction button
        predict_button = st.form_submit_button("🔮 Predict Price", use_container_width=True)
        
        if predict_button:
            try:
                # Prepare features for prediction
                type_encoded = 1 if avocado_type == "Organic" else 0
                
                features = np.array([[
                    Total_Volume,
                    small_avocados,
                    medium_avocados,
                    large_avocados,
                    Total_Bags,
                    Small_Bags,
                    Large_Bags,
                    XLarge_Bags,
                    type_encoded,
                    year
                ]])
                
                # Scale features
                features_scaled = scaler.transform(features)
                
                # Make prediction
                prediction = rfr.predict(features_scaled)[0]
                
                # Display result
                st.markdown("---")
                st.markdown(
                    f'<div class="prediction-result">Predicted Avocado Price: ${abs(prediction):.2f}</div>',
                    unsafe_allow_html=True
                )
                
                # Additional insights
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.info(f"**Market Type:** {avocado_type}")
                with col2:
                    st.info(f"**Total Volume:** {Total_Volume:,.0f} units")
                with col3:
                    st.info(f"**Year:** {year}")
                
            except Exception as e:
                st.error(f"❌ Prediction error: {str(e)}")

# Model Performance Page
elif r == "📊 Model Performance":
    if rfr is None:
        st.error("❌ Model not available. Please check the data file.")
        st.stop()
    
    st.markdown('<h1 class="main-header">📊 Model Performance Analysis</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Model Metrics")
        st.metric("Training Accuracy", f"{train_score:.4f}")
        st.metric("Testing Accuracy", f"{test_score:.4f}")
        st.metric("Model Type", "Random Forest Regressor")
        st.metric("Number of Estimators", "250")
    
    with col2:
        st.markdown("### 🔧 Model Configuration")
        st.write(f"**Algorithm:** Random Forest Regressor")
        st.write(f"**Training Set Size:** 80% of data")
        st.write(f"**Testing Set Size:** 20% of data")
        st.write(f"**Feature Scaling:** StandardScaler")
        st.write(f"**Random State:** 26 (for reproducibility)")
    
    st.markdown("### 📈 Feature Information")
    features_info = {
        "Feature": [
            "Total Volume", "Small Avocados (PLU 4046)", "Medium Avocados (PLU 4225)",
            "Large Avocados (PLU 4770)", "Total Bags", "Small Bags",
            "Large Bags", "Extra Large Bags", "Type", "Year"
        ],
        "Description": [
            "Total number of avocados sold",
            "Number of small avocados sold",
            "Number of medium avocados sold",
            "Number of large avocados sold",
            "Total number of bags used",
            "Number of small bags",
            "Number of large bags",
            "Number of extra large bags",
            "Conventional (0) or Organic (1)",
            "Year of sale"
        ]
    }
    
    st.table(pd.DataFrame(features_info))

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 2rem;'>
        🥑 Avocado Price Predictor | Built with Streamlit & Scikit-learn<br>
        Made with ❤️ for better market predictions
    </div>
    """,
    unsafe_allow_html=True
)
'''

print("Here's your improved, user-friendly and professional Streamlit app:")
print(streamlit_code)
