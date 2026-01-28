#Customer Churn Analysis & Prediction – Telecom Domain
#Overview

Customer churn is a major challenge in the telecom industry, directly impacting revenue and growth.
This project builds an end-to-end churn analytics system that combines data analysis, machine learning, and a backend API to understand churn behavior and predict high-risk customers.

Dataset

IBM Telco Customer Churn dataset

7,043 customers

33 features including contract type, charges, service details, churn reasons, and CLTV

Target variables:

Churn Label (Yes / No)

Churn Value (1 / 0)

#Tech Stack

Python

Pandas, Matplotlib

Scikit-learn

FastAPI

Thunder Client (API testing)

#Project Structure
customer-churn-analysis/
│
├── telecom_churn.csv
├── churn_analysis.py        # EDA & visualizations
├── churn_model.py           # ML churn prediction
├── api.py                   # FastAPI backend
├── churn_by_contract.png
├── churn_reasons.png
├── api_get_churn_stats.png
├── api_get_churn_reasons.png
├── api_post_churn_prediction.png
└── README.md

Exploratory Data Analysis (EDA)
Key Insights

Overall churn rate: ~26.5%

Month-to-month contracts show the highest churn (~43%)

Long-term contracts significantly reduce churn (<3%)

Churned customers pay higher average monthly charges

Customer support experience and competitor offerings are major churn drivers

Visualizations
Churn Rate by Contract Type

Top Reasons for Customer Churn

#Machine Learning – Churn Prediction

Model: Logistic Regression

Target: Churn Value

Features used:

Monthly Charges

Contract

Internet Service

Payment Method

CLTV

#Model Evaluation

Evaluated using confusion matrix, precision, recall, and F1-score

Focused on recall for churned customers due to class imbalance

Serves as a strong baseline churn prediction model

#Backend API (FastAPI)

A production-style backend was built to expose churn analytics and predictions via REST APIs.

#Available Endpoints
🔹 GET /churn/stats

Returns overall churn statistics.


🔹 GET /churn/reasons

Returns top churn reasons.


🔹 POST /churn/predict

Predicts churn probability for a customer.

Example request:

{
  "Monthly Charges": 85,
  "Contract": "Month-to-month",
  "Internet Service": "Fiber optic",
  "Payment Method": "Electronic check",
  "CLTV": 3500
}


Example response:

{
  "churn_prediction": 1,
  "churn_probability": 0.53
}


#How to Run the Project
1️⃣ Install dependencies
pip install pandas matplotlib scikit-learn fastapi uvicorn

2️⃣ Run analysis
python churn_analysis.py

3️⃣ Run ML model
python churn_model.py

4️⃣ Start backend
uvicorn api:app --reload


Test APIs using Thunder Client or any REST client.

#Business Impact

Identifies high-risk customer segments

Helps prioritize retention strategies

Enables real-time churn prediction through APIs

Demonstrates how analytics + ML + backend systems work together

#Conclusion

This project demonstrates a full churn analytics pipeline, from raw data exploration to machine learning and backend deployment. It reflects real-world problem solving and production-oriented thinking suitable for data analyst, backend, and ML roles.

Author

Sudhanva J Rao
