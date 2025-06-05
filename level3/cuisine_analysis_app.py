import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Use Streamlit's built-in support for rendering matplotlib
# st.set_option('deprecation.showPyplotGlobalUse', False)

# Load dataset
df = pd.read_csv("Dataset .csv")
df['Cuisines'] = df['Cuisines'].fillna('Unknown')

# Sidebar Filters
st.sidebar.title("🔍 Filters")

min_votes = st.sidebar.slider("Minimum total votes per cuisine", 0, 5000, 1000, step=100)
top_n = st.sidebar.slider("Top N Cuisines to Display", 5, 30, 10)

# Title
st.title("🍽️ Customer Preference Analysis: Cuisine vs Ratings")

# Average Rating by Cuisine
filtered_df = df.groupby('Cuisines').filter(lambda x: x['Votes'].sum() > min_votes)
top_rated_cuisines = filtered_df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False).head(top_n)

# Most Popular Cuisines by Total Votes
popular_cuisines = df.groupby('Cuisines')['Votes'].sum().sort_values(ascending=False).head(top_n)

# Show Data Option
if st.checkbox("📋 Show Raw Data (first 10 rows)"):
    st.dataframe(df.head(10))

# Plot 1: Top Rated Cuisines
st.subheader("🌟 Top Rated Cuisines (based on average rating)")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x=top_rated_cuisines.values,
    y=top_rated_cuisines.index,
    ax=ax,
    hue=top_rated_cuisines.index,  # to avoid palette warning
    palette="coolwarm",
    legend=False
)
ax.set_title("Top Rated Cuisines (based on average rating)")
ax.set_xlabel("Average Rating")
ax.set_ylabel("Cuisine")
st.pyplot(fig)


# Plot 2: Most Popular Cuisines
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x=popular_cuisines.values,
    y=popular_cuisines.index,
    ax=ax2,
    hue=popular_cuisines.index,
    palette="mako",
    legend=False
)
ax2.set_title("Most Popular Cuisines by Total Votes")
ax2.set_xlabel("Total Votes")
ax2.set_ylabel("Cuisine")

st.pyplot(fig2)

