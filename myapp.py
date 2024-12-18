import yfinance as yf
import pandas as pd
import streamlit as st
# from datetime import date


st.write("""
## Simple Stock Pricing App for Fun :)
Analyze historical stock data interactively!
""")

# Create input box for the user to type a stock ticker symbol
ticker_symbol = st.text_input("Enter a stock ticker symbol (e.g., AAPL, MSFT, GOOGL):")

# Allow users to select start and end dates
st.write("### Select the date range for historical data:")
start_date = st.date_input("Start date:", key="start_date")
end_date = st.date_input("End date:", key="end_date")

# Validate dates
if start_date >= end_date:
    st.error("Error: End date must be later than start date.")
else:
    # List of features to analyze
    features_list = ["Close", "Dividends", "High", "Low", "Open", "Volume"]

    # Create a dropdown menu for the user to select a feature
    selected_feature = st.selectbox("Select a feature to analyze:", features_list)

    # Get data on the selected ticker
    ticker_data = yf.Ticker(ticker_symbol)

    # Get historical prices for the ticker within the user-defined date range
    ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

    if ticker_df.empty:
        st.warning(f"No data found for {ticker_symbol} in the given date range.")
    else:
        # Display the selected feature data as a line chart
        st.write(f"### **{ticker_symbol}** - **{selected_feature}** From {start_date} to {end_date}")
        st.line_chart(ticker_df[selected_feature])
