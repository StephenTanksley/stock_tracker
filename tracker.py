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

current_portfolio = {'Ford': 'F',
                     'Cleveland-Cliffs': 'CLF',
                     'Catalyst Pharmaceuticals': 'CPRX',
                     'Amazon': 'AMZN',
                     'TherapeuticsMD': 'TXMD'}

st.sidebar.header("User Input Options")

selection = st.sidebar.selectbox("Which stock would you like to track?", ('Ford',
                                                                          'Cleveland-Cliffs',
                                                                          'Catalyst Pharmaceuticals',
                                                                          'Amazon',
                                                                          'TherapeuticsMD'))


# Get current date
today = date.today()

# Allow users to define start and end dates
start_date = st.sidebar.date_input(
    "Please select a start date: ", date(2010, 1, 1))
end_date = st.sidebar.date_input(
    "Please select an end date: ", today)


# Get the data attached to this ticker.
ticker_data = yf.Ticker(current_portfolio[selection])


# Get the historical prices for this ticker.

ticker_dataframe = ticker_data.history(
    period='1d', start=start_date, end=end_date)


# Display prices for the ticker
price_string = f"### Price of {selection} ('**{current_portfolio[selection]}**') at close."
st.markdown(price_string)
st.line_chart(ticker_dataframe.Close)

volume_string = f"### Volume of {selection} ('**{current_portfolio[selection]}**'). "
st.markdown(volume_string)
st.line_chart(ticker_dataframe.Volume)
