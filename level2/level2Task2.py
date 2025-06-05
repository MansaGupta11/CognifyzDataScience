# Task: Price Range Analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"level2\Dataset .csv")

# 1. Find the most common price range

price_counts = df['Price range'].value_counts()
most_common_price = price_counts.idxmax()

print(f"The most common price range among restaurants is: {most_common_price}")
print("\nPrice range frequency:")
print(price_counts)

# 2. Calculate average rating for each price range

avg_rating_by_price = df.groupby('Price range')['Aggregate rating'].mean().round(2)

print("\n Average aggregate rating for each price range:")
print(avg_rating_by_price)

# 3. Identify the rating color that represents the highest average rating

# Step 1: Find which price range has the highest average rating
best_price_range = avg_rating_by_price.idxmax()
best_avg_rating = avg_rating_by_price.max()

print("\nAll possible Rating Colors and how often they appear:")
print(df['Rating color'].value_counts())


# Step 2: For that price range, get the most frequent rating color
# (in case there are multiple, we take the mode)
rating_color_mode = df[df['Price range'] == best_price_range]['Rating color'].mode().iloc[0]

print(f"The price range with the highest average rating is {best_price_range} "
      f"with an average rating of {best_avg_rating}")
print(f"The most common rating color in this price range is: {rating_color_mode}")


# Visualize the average rating by price range

# Fix for FutureWarning: set hue=x and disable legend
plt.figure(figsize=(8, 5))
sns.barplot(
    data=avg_rating_by_price.reset_index(),
    x='Price range',
    y='Aggregate rating',
    hue='Price range',
    palette="Blues_d",
    legend=False
)
plt.title("Average Restaurant Rating by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Aggregate Rating")
plt.tight_layout()
plt.show()

