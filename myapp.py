import yfinance as yf
import streamlit as st
import pandas as pd



st.write("""

   simple stock price app
   
   
   
""")

#define ticker symbol
tickerSymbol = 'Googl'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
