import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"level3\Dataset .csv")
df['Cuisines'] = df['Cuisines'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')

# 1️ Histogram - Distribution of Aggregate Ratings
plt.figure(figsize=(8, 5))
sns.histplot(df['Aggregate rating'], bins=10, kde=True, color='skyblue')
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 2️ Bar Plot - Average Rating by Cuisine (Top 10)
top_cuisines = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
top_cuisines_df = top_cuisines.reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(
    x=top_cuisines_df['Aggregate rating'],
    y=top_cuisines_df['Cuisines'],
    hue=top_cuisines_df['Cuisines'],
    palette='Spectral',
    legend=False
)
plt.title("Top 10 Cuisines by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.show()

# 3️ Bar Plot - Average Rating by City (Top 10)
top_cities = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
top_cities_df = top_cities.reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(
    x=top_cities_df['Aggregate rating'],
    y=top_cities_df['City'],
    hue=top_cities_df['City'],
    palette='viridis',
    legend=False
)
plt.title("Top 10 Cities by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# 4️ Scatter Plot - Votes vs Aggregate Rating
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Votes', y='Aggregate rating', data=df, hue='Price range', palette='cool')
plt.title("Votes vs Aggregate Rating by Price Range")
plt.xlabel("Votes")
plt.ylabel("Aggregate Rating")
plt.tight_layout()
plt.show()

# 5️ Box Plot - Price Range vs Aggregate Rating
plt.figure(figsize=(8, 5))
sns.boxplot(
    x='Price range',
    y='Aggregate rating',
    data=df,
    hue='Price range',
    palette='pastel',
    legend=False
)
plt.title("Price Range vs Aggregate Rating")
plt.xlabel("Price Range")
plt.ylabel("Aggregate Rating")
plt.tight_layout()
plt.show()

# 6️ Heatmap - Correlation Between Numerical Features
df['Name Length'] = df['Restaurant Name'].apply(len)
df['Address Length'] = df['Address'].apply(len)
df['Has Table Booking (Binary)'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online Delivery (Binary)'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

numerical_features = ['Price range', 'Votes', 'Aggregate rating', 'Name Length', 'Address Length', 'Has Table Booking (Binary)', 'Has Online Delivery (Binary)']
corr = df[numerical_features].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Numerical Features")
plt.tight_layout()
plt.show()

# Summary of Visual Insights
print("\n📊📈 Data Visualization Summary:")
print("Chart Type      | Insight Example")
print("-"*40)
print("📊 Histogram     | Most ratings fall between 3.0 and 4.5")
print("📈 Bar (Cuisines)| Italian, Mexican may have high avg ratings")
print("🌍 Bar (Cities)  | Mumbai, Delhi may show better ratings")
print("🎯 Scatter Plot  | Votes increase with ratings (weak or strong?)")
print("📦 Box Plot      | High price ranges may get better ratings")
print("🔥 Heatmap       | Shows what features are correlated with ratings")
print("="*40)
