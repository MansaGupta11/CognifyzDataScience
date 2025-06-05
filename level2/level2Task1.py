import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"level2\Dataset .csv")

# 1. Percentage of Restaurants with Table Booking and Online Delivery
table_booking_percent = df['Has Table booking'].value_counts(normalize=True) * 100
online_delivery_percent = df['Has Online delivery'].value_counts(normalize=True) * 100

print("Table Booking Availability (%):\n", table_booking_percent)
print("\n Online Delivery Availability (%):\n", online_delivery_percent)

#  2. Compare Avg Rating: Table Booking vs No Booking
avg_rating_table_booking = df.groupby('Has Table booking')['Aggregate rating'].mean()
print("\n Average Rating (Table Booking vs No Booking):\n", avg_rating_table_booking)

#  3. Online Delivery vs Price Range
online_delivery_by_price = pd.crosstab(df['Price range'], df['Has Online delivery'], normalize='index') * 100
print("\n Online Delivery Availability by Price Range (%):\n", online_delivery_by_price)

# Optional Plot: Online delivery availability across price ranges
online_delivery_by_price.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='coolwarm')
plt.title("Online Delivery Availability by Price Range")
plt.ylabel("Percentage of Restaurants")
plt.xlabel("Price Range")
plt.legend(title="Online Delivery")
plt.tight_layout()
plt.show()
