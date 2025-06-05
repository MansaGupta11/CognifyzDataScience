import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"level1\Dataset .csv")

#  1. Basic Statistical Measures for Numerical Columns
print("Descriptive Statistics (Mean, Median, Std):\n")
numerical_summary = df.describe().T[['mean', '50%', 'std']]  # 50% = median
print(numerical_summary)

#  2. Distribution of Categorical Variables

# Country Code Distribution
print("\n Country Code Distribution:\n")
print(df['Country Code'].value_counts())

# City Distribution - Top 10 Cities
print("\n Top 10 Cities with Most Restaurants:\n")
print(df['City'].value_counts().head(10))

# Cuisines Distribution - Top 10 Cuisines
print("\n Top 10 Most Common Cuisines:\n")
print(df['Cuisines'].value_counts().head(10))

