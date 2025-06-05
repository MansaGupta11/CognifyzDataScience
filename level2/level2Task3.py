from tabulate import tabulate
import pandas as pd

# Load dataset
df = pd.read_csv(r"level2\Dataset .csv")
df.index = df.index + 1

# Feature engineering
df['Name Length'] = df['Restaurant Name'].apply(len)
df['Address Length'] = df['Address'].apply(len)
df['Has Table Booking (Binary)'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online Delivery (Binary)'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

# Shorten address text to improve table layout
df['Short Address'] = df['Address'].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

# Columns to display
selected_cols = [
    'Restaurant Name', 'Name Length', 'Address Length', 'Has Table Booking (Binary)', 'Has Online Delivery (Binary)'
]

# Print a nicely formatted table
print(tabulate(df[selected_cols].head(), headers='keys', tablefmt='grid', showindex=True))
