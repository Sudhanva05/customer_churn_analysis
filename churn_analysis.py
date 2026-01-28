import pandas as pd

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
