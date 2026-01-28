import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("telecom_churn.csv")

# Preview data
print(df.head())
print("\nDataset shape:", df.shape)

# Overall churn distribution
print("\nChurn distribution:")
print(df["Churn Label"].value_counts())

print("\nChurn percentage:")
print(df["Churn Label"].value_counts(normalize=True) * 100)

# Analyze churn reasons (only for churned customers)
print("\nTop churn reasons:")
print(
    df[df["Churn Label"] == "Yes"]["Churn Reason"]
    .value_counts()
    .head(10)
)

# Churn by contract type
print("\nChurn by Contract Type:")
print(
    df.groupby("Contract")["Churn Label"]
    .value_counts(normalize=True)
    * 100
)

# Average monthly charges by churn
print("\nAverage Monthly Charges by Churn:")
print(
    df.groupby("Churn Label")["Monthly Charges"]
    .mean()
)

# Prepare churn by contract (percentage of churned customers)
churn_contract = (
    df[df["Churn Label"] == "Yes"]
    .groupby("Contract")
    .size()
)

total_contract = df.groupby("Contract").size()

churn_rate_contract = (churn_contract / total_contract) * 100

# Plot
plt.figure()
churn_rate_contract.plot(kind="bar")
plt.title("Churn Rate by Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Contract Type")
plt.tight_layout()
plt.show()


# Top churn reasons
top_reasons = (
    df[df["Churn Label"] == "Yes"]["Churn Reason"]
    .value_counts()
    .head(5)
)

plt.figure()
top_reasons.plot(kind="bar")
plt.title("Top 5 Reasons for Customer Churn")
plt.ylabel("Number of Customers")
plt.xlabel("Churn Reason")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
