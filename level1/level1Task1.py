#Task: Data Exploration and Preprocessing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
df = pd.read_csv("Dataset .csv")

# Step 1: Preview the dataset
print("Preview of the dataset:")
print(df.head())

# Step 2: Identify the number of rows and columns
print(f"\nTotal Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

# Step 3: Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 4: Handle missing values in 'Cuisines' column
df['Cuisines'] = df['Cuisines'].fillna('Unknown')

# Step 5: Check data types
print("\nData types of columns:")
print(df.dtypes)

# Step 6: Analyze distribution of target variable 'Aggregate rating'
print("\nAggregate rating distribution (counts):")
print(df['Aggregate rating'].value_counts().sort_index())

print("\nAggregate rating distribution (percentages):")
print(df['Aggregate rating'].value_counts(normalize=True).sort_index() * 100)

