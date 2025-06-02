import streamlit as st
import joblib

# Load the saved model
model = joblib.load('restaurant_rating_model.pkl')

st.title("🍽️ Restaurant Rating Predictor")

# User inputs
name_length = st.number_input("Restaurant Name Length", min_value=1, value=10)
address_length = st.number_input("Address Length", min_value=1, value=20)
price_range = st.selectbox("Price Range", [1, 2, 3, 4])
votes = st.number_input("Number of Votes", min_value=0, value=100)
table_booking = st.selectbox("Has Table Booking?", ["Yes", "No"])
online_delivery = st.selectbox("Has Online Delivery?", ["Yes", "No"])

# Convert Yes/No to binary
table_binary = 1 if table_booking == "Yes" else 0
delivery_binary = 1 if online_delivery == "Yes" else 0

# Predict button
if st.button("Predict Rating"):
    input_data = [[name_length, address_length, price_range, votes, table_binary, delivery_binary]]
    prediction = model.predict(input_data)[0]
    st.success(f"⭐ Predicted Aggregate Rating: {round(prediction, 2)}")
