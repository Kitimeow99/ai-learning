import pandas as pd

df = pd.read_csv("runs.csv")

print("FIRST FIVE ROWS")
print(df.head())

print("\nTABLE SIZE")
print(df.shape)

print("\nCOLUMN TYPES")
print("df.dtypes")

print("\nMISSING VALUES")
print(df.isna().sum())

print("\nNUMERICAL SUMMARY")
print(df.describe())

print("\nTOTAL DISTANCE")
print(df["distance_km"].sum())

print("\nRUNS OF AT LEAST 5 KM")
long_runs = df[df["distance_km"] >= 5]
print(long_runs)