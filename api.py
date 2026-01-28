from fastapi import FastAPI
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

app = FastAPI(title="Customer Churn API")

df = pd.read_csv("telecom_churn.csv")

features = [
    "Monthly Charges",
    "Contract",
    "Internet Service",
    "Payment Method",
    "CLTV"
]

X = df[features].copy()
y = df["Churn Value"]

label_encoders = {}
for col in ["Contract", "Internet Service", "Payment Method"]:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

model = LogisticRegression(max_iter=1000)
model.fit(X, y)


@app.get("/")
def root():
    return {"status": "Churn API running"}


@app.get("/churn/stats")
def churn_stats():
    churn_counts = df["Churn Label"].value_counts()
    churn_rate = df["Churn Label"].value_counts(normalize=True) * 100

    return {
        "total_customers": int(len(df)),
        "churned": int(churn_counts.get("Yes", 0)),
        "not_churned": int(churn_counts.get("No", 0)),
        "churn_rate_percent": round(churn_rate.get("Yes", 0), 2)
    }


@app.get("/churn/reasons")
def churn_reasons():
    return (
        df[df["Churn Label"] == "Yes"]["Churn Reason"]
        .value_counts()
        .head(5)
        .to_dict()
    )


@app.post("/churn/predict")
def predict_churn(payload: dict):
    input_df = pd.DataFrame([payload])

    for col in ["Contract", "Internet Service", "Payment Method"]:
        input_df[col] = label_encoders[col].transform(input_df[col])

    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    return {
        "churn_prediction": int(pred),
        "churn_probability": round(float(prob), 2)
    }
