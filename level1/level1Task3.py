import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"level1\Dataset .csv")

#  1. Visualize Restaurant Locations (Latitude vs Longitude)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Longitude", y="Latitude", hue="Aggregate rating",
                palette="viridis", alpha=0.6, edgecolor=None)
plt.title("Restaurant Locations by Latitude and Longitude")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(title="Rating", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#  2. Analyze Distribution by City (Top 10 Cities)
top_cities = df['City'].value_counts().head(10)
print("Top 10 Cities with Most Restaurants:\n", top_cities)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_cities.index, y=top_cities.values, palette="rocket")
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  3. Analyze Distribution by Country Code
country_counts = df['Country Code'].value_counts()
print("\n Restaurant Count by Country Code:\n", country_counts)

#  4. Check Correlation: Rating vs Latitude
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Latitude', y='Aggregate rating', data=df, alpha=0.4, color='blue')
plt.title("Aggregate Rating vs Latitude")
plt.xlabel("Latitude")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

#  5. Check Correlation: Rating vs Longitude
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Longitude', y='Aggregate rating', data=df, alpha=0.4, color='green')
plt.title("Aggregate Rating vs Longitude")
plt.xlabel("Longitude")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

#  6. Correlation Matrix
corr_matrix = df[['Latitude', 'Longitude', 'Aggregate rating']].corr()
print("\n Correlation Matrix:\n", corr_matrix)
