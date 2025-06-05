#build a regression model to predicct the aggregate rating
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Step 1: Load and prepare the dataset
df = pd.read_csv(r"level3\Dataset .csv")

# Basic feature engineering
df['Name Length'] = df['Restaurant Name'].apply(len)
df['Address Length'] = df['Address'].apply(len)
df['Has Table Booking (Binary)'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online Delivery (Binary)'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

# Step 2: Select features and target
features = [
    'Name Length', 'Address Length', 'Price range', 'Votes',
    'Has Table Booking (Binary)', 'Has Online Delivery (Binary)'
]
X = df[features]
y = df['Aggregate rating']

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train and evaluate different models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(random_state=42)
}

# Store results
results = []

# Loop through each model, train, predict, and evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    results.append({
        'Model': name,
        'R2 Score': round(r2, 3),
        'MAE': round(mae, 3),
        'MSE': round(mse, 3)
    })

# Step 5: Print the comparison of model performances
print("Model Performance Comparison:\n")
for result in results:
    print(f"{result['Model']} → R2: {result['R2 Score']}, MAE: {result['MAE']}, MSE: {result['MSE']}")


# Save the best model (e.g., Random Forest)
best_model = models['Random Forest']
joblib.dump(best_model, 'restaurant_rating_model.pkl')
