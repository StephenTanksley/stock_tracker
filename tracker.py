import yfinance as yf
import streamlit as st
import pandas as pd
import requests as req
import random
from datetime import date


st.write("""
         # Stock Comparison App
         
         Shown are the stock closing price and volume of my hypothetical portfolio.
         
         """)

current_portfolio = {'F': 'Ford',
                     'CLF': 'Cleveland-Cliffs',
                     'CPRX': 'Catalyst Pharmaceuticals',
                     'AMZN': 'Amazon',
                     'TXMD': 'TherepeuticsMD'}


# Define the ticker we want to track.
# ticker_symbol = random.choice(current_stocks)

# for key, value in current_portfolio.items():
#     print(f"{key}: {value}")

ticker_symbol = random.choice(list(current_portfolio.keys()))

# Get the data attached to this ticker.
ticker_data = yf.Ticker(ticker_symbol)

# Get current date
today = date.today()

# Get the historical prices for this ticker.
ticker_dataframe = ticker_data.history(
    period='1d', start='2010-5-31', end=today)

# Open     High     Low Close    Volume    Dividends    Stock Splits

st.write(f"Price of {current_portfolio[ticker_symbol]} at close.")
st.line_chart(ticker_dataframe.Close)

st.write(f" Volume of {current_portfolio[ticker_symbol]} at close. ")
st.line_chart(ticker_dataframe.Volume)
