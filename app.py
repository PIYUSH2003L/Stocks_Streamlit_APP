import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Streamlit page configuration
st.set_page_config(page_title="Nifty Stocks Explorer", layout="wide")

# Title
st.title("📈 Nifty Stocks Explorer")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Nifty_Stocks.csv")
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure proper datetime format
    return df

df = load_data()

# Show available categories
categories = df['Category'].unique()
selected_category = st.selectbox("Select a Category", categories)

# Filter symbols based on selected category
symbols = df[df['Category'] == selected_category]['Symbol'].unique()
selected_symbol = st.selectbox("Select a Stock Symbol", symbols)

# Filter the final data
filtered_data = df[(df['Category'] == selected_category) & (df['Symbol'] == selected_symbol)]

# Plotting
st.subheader(f"Closing Price Trend for {selected_symbol}")

fig, ax = plt.subplots(figsize=(15, 6))
sb.lineplot(x=filtered_data['Date'], y=filtered_data['Close'], ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
ax.set_title(f"{selected_symbol} Closing Price Over Time")

# Show plot
st.pyplot(fig)

# Optional: Show data table
with st.expander("📋 Show Raw Data"):
    st.dataframe(filtered_data)
