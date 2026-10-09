import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("network_change_dataset.csv")

# Display first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Dataset size
print("\nDATASET SHAPE:")
print(df.shape)

# Column names
print("\nCOLUMNS:")
print(df.columns.tolist())

# Data types
print("\nDATA TYPES:")
print(df.dtypes)

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Impact distribution
print("\nIMPACT DISTRIBUTION:")
print(df["impact"].value_counts())
# Change type distribution
print("\nCHANGE TYPE DISTRIBUTION:")
print(df["change_type"].value_counts())

# Basic statistics
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

# Plot impact distribution
df["impact"].value_counts().plot(kind="bar")

plt.title("Network Impact Distribution")
plt.xlabel("Impact Level")
plt.ylabel("Number of Samples")
plt.tight_layout()
plt.show()