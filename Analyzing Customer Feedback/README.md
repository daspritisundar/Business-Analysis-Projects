# Task 3: Analyzing Customer Feedback 📝

## 📌 Overview  
Understanding customer sentiment is critical for banks to maintain trust, improve service quality, and enhance customer satisfaction.  
In this task, I developed a **complete ETL pipeline** to extract, transform, and load (ETL) customer reviews of **CIH Bank branches in Morocco**, followed by **AI-powered sentiment analysis** and visualization.  

The system leverages **Apache Airflow** for workflow orchestration, **Hugging Face Transformers (BERT multilingual)** for sentiment analysis, and **PostgreSQL** for structured storage, enabling CIH Bank to make **data-driven decisions** for service improvement.  

---

## 🎯 Objectives  
- Automate the **extraction** of Google Maps reviews using **Apify API**.  
- Perform **data transformation**, including text cleaning, geolocation extraction, and sentiment scoring.  
- Store transformed data in a **PostgreSQL data warehouse** for analytics and reporting.  
- Deliver **visual insights** (heatmaps, sentiment trends) to support branch-level decision-making.  

---


---

## 🛠️ Methodology  

### 🔹 1. Data Extraction  
- API: **Apify Google Maps Scraper**.  
- Query: `"CIH Bank"` limited to **Morocco** and **English reviews**.  
- Collected metadata: Review text, geolocation (lat/long), city, state, country code, and published date.  

### 🔹 2. Data Transformation  
- Implemented in `transform.py`:  
  - Removed missing/invalid text.  
  - Extracted geolocation and date components (day, month, year).  
  - Applied **Hugging Face BERT multilingual model (`nlptown/bert-base-multilingual-uncased-sentiment`)** for sentiment scoring:  
    - Positive = `+1`  
    - Neutral = `0`  
    - Negative = `-1`  
- Structured the data for analysis and reporting.  

### 🔹 3. Data Loading  
- Implemented in `load.py`:  
  - Connected to **PostgreSQL** via SQLAlchemy.  
  - Loaded transformed data into the `banks` table.  

### 🔹 4. Orchestration with Airflow  
- Defined in `etl.py`:  
  - **DAG** scheduled monthly (`0 0 1 * *`).  
  - Task order: `extract_task >> transform_task >> load_task`.  
  - Ensures fully automated refresh of the customer feedback warehouse.  

### 🔹 5. Visualization & Reporting  
- Tools: **Power BI** (and matplotlib for basic plots).  
- Created **heatmaps** of sentiment by branch location.  
- Generated **trend reports** on positive/negative reviews per region.  
- Produced actionable insights summarized in the report.  

---

## 📊 Key Findings (from CIH Bank case study):contentReference[oaicite:1]{index=1}  
- Customer reviews showed clear **geographic sentiment variations**.  
- **Negative themes**: service delays, support inefficiencies.  
- **Positive themes**: accessibility, staff friendliness.  
- Heatmaps revealed specific **branches requiring urgent attention**.  
- Overall, the automated pipeline ensures **real-time monitoring** of customer satisfaction.  

---

## 🚀 Business Applications  
1. **Branch Managers** – Identify locations with declining satisfaction and prioritize interventions.  
2. **Customer Service Teams** – Focus on recurring issues (e.g., support response times).  
3. **Executives** – Track **KPIs (NPS-like sentiment index)** across branches.  
4. **Data Teams** – Extend pipeline for multilingual sentiment analysis & advanced trend modeling.  

---

## 🖥️ How to Run Locally  

### 1. Clone the Repository
```bash
git clone https://github.com/daspritisundar/Business-Analytics-Projects.git
cd Task3_Analyzing_Customer_Feedback/ETL_Pipeline


