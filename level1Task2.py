import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Dataset .csv")

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

# 3. Visualizations

# Plot - Top 10 Cities
top_cities = df['City'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_cities.index, y=top_cities.values, palette='viridis')
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot - Top 10 Cuisines
top_cuisines = df['Cuisines'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(y=top_cuisines.index, x=top_cuisines.values, palette='coolwarm')
plt.title("Top 10 Most Common Cuisines")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.show()
