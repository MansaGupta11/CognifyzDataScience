import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset .csv")

# Handle missing cuisines
df['Cuisines'] = df['Cuisines'].fillna('Unknown')

#  Step 1: Analyze Average Rating by Cuisine
avg_rating_by_cuisine = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
print("Average Rating by Cuisine:\n", avg_rating_by_cuisine.head(10))

#  Step 2: Most Popular Cuisines by Votes
cuisine_votes = df.groupby('Cuisines')['Votes'].sum().sort_values(ascending=False)
print("Most Popular Cuisines by Total Votes:\n", cuisine_votes.head(10))

#  Step 3: Top Cuisines with High Ratings (Min votes filter to avoid bias)
# Filter out cuisines with too few votes (e.g., < 1000)
filtered_df = df.groupby('Cuisines').filter(lambda x: x['Votes'].sum() > 1000)
top_cuisines_by_rating = filtered_df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
print("Cuisines with Highest Avg Ratings (with >1000 votes):\n", top_cuisines_by_rating.head(10))


