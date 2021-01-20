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

# current_portfolio = {'F': 'Ford',
#                      'CLF': 'Cleveland-Cliffs',
#                      'CPRX': 'Catalyst Pharmaceuticals',
#                      'AMZN': 'Amazon',
#                      'TXMD': 'TherapeuticsMD'}

current_portfolio = {'Ford': 'F',
                     'Cleveland-Cliffs': 'CLF',
                     'Catalyst Pharmaceuticals': 'CPRX',
                     'Amazon': 'AMZN',
                     'TherapeuticsMD': 'TXMD'}

# date_period = {
#     '1 day': '1d',
#     '5 days': '5d',
#     '1 month': '1mo',
#     '3 months': '3mo',
#     '6 months': '6mo',
#     '1 year': '1y',
#     '2 years': '2y',
#     '5 years': '5y',
#     '10 years': '10y',
#     'Year to date': 'ytd',
#     'Max': 'max'
# }

selection = st.sidebar.selectbox("Which stock would you like to track?", ('Ford',
                                                                          'Cleveland-Cliffs',
                                                                          'Catalyst Pharmaceuticals',
                                                                          'Amazon',
                                                                          'TherapeuticsMD'))

# period = st.sidebar.selectbox("Which period resolution would you like to track?", ('1 day',
#                                                                                    '5 days',
#                                                                                    '1 month',
#                                                                                    '3 months',
#                                                                                    '6 months',
#                                                                                    '1 year',
#                                                                                    '2 years',
#                                                                                    '5 years',
#                                                                                    '10 years',
#                                                                                    'Year to date',
#                                                                                    'Max'))

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

# # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max

ticker_dataframe = ticker_data.history(
    period='1d', start=start_date, end=end_date)

# Open     High     Low Close    Volume    Dividends    Stock Splits

price_string = f"### Price of {selection} ('**{current_portfolio[selection]}**') at close."
st.markdown(price_string)
st.line_chart(ticker_dataframe.Close)

volume_string = f"### Volume Price of {selection} ('**{current_portfolio[selection]}**'). "
st.markdown(volume_string)
st.line_chart(ticker_dataframe.Volume)
