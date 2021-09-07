import yfinance as yf
#https://towardsdatascience.com/financial-data-from-yahoo-finance-with-python-b5399743bcc6
import streamlit as st

st.write("""
### Simple Stock Price App
Shown are the stock closing price and volume of Google
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol) #get data on this ticker

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31') #get the historical prices for this ticker

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)

#to view the app on a browser, we need to run:
#>streamlit run main.py