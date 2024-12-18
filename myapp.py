import yfinance as yf
import pandas as pd
import streamlit as st


st.write("""
Simple stock pricing app for fun :)
         """)

#defines ticket symbol
tickersymbol = 'GOOGL'
#get data on ticker
tickerdata = yf.Ticker(tickersymbol)
#get historical prices for ticker
ticker_df = tickerdata.history(period = '1d', start = '2018-1-19', end = '2021-1-19')

st.line_chart(ticker_df)
