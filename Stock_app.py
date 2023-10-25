#------------------------------
#------import libraries--------
#------------------------------
import streamlit as st
import pandas as pd
#import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
from datetime import datetime
import time
import yfinance as yf

#Streamlit app
# sidebar
with st.sidebar.form(key ='Form1'):
    st.title("Enter information")
    symbol = st.text_input('Stock symbol', 'e.g.AAPL')
    inter=st.selectbox('Enter the interval of time:',
    ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'))
    init = st.date_input("Enter the start date [YYYY-MM-DD]:", ) #datetime.date(2019, 7, 6)
    finish=st.date_input("Enter the finish date [YYYY-MM-DD]:", )#datetime.date(2019, 7, 6)
    st.markdown("**Analytics**")
    MA_30 = st.checkbox('MA-30 d')
    MA_15 = st.checkbox('MA-15 d')
    MA_5 = st.checkbox('MA-5 d')
    
    submit_code = st.form_submit_button(label ="Execute")

#main page
# title
st.subheader("Stock Analytics")
st.markdown("""---""")

# plot
if submit_code:
    if symbol:
        stock = yf.Ticker(symbol)
        df = stock.history(interval=inter, start=init, end=finish)

        # Calculate the 30/15/5-period moving average
        df['MA_30'] = df['Close'].rolling(window=30).mean()
        df['MA_15'] = df['Close'].rolling(window=15).mean()
        df['MA_5'] = df['Close'].rolling(window=5).mean()

        # Main plot
        fig = make_subplots(rows=2, cols=1,
                                shared_xaxes=True,
                                vertical_spacing=0.1,
                                subplot_titles=("Stock Price","Volumen"),
                                row_heights=[0.5,0.2])
        
        fig.add_trace(go.Candlestick(x=df.index,
              open=df['Open'],
              high=df['High'],
              low=df['Low'],
              close=df['Close']),row=1,col=1)
            
        fig.add_trace(go.Bar(x=df.index,
                             y=df['Volume'],
                             marker_color='blue'), row=2, col=1)
        
        # Add the 30/15/5-period moving average line
        if MA_30:
            fig.add_trace(go.Scatter(x=df.index, y=df['MA_30'], line=dict(color='red', width=1), name='MA 30'),
                          row=1, col=1)
        if MA_15:
            fig.add_trace(go.Scatter(x=df.index, y=df['MA_15'], line=dict(color='purple', width=1), name='MA 15'),
                          row=1, col=1)
        if MA_5:
            fig.add_trace(go.Scatter(x=df.index, y=df['MA_5'], line=dict(color='blue', width=1), name='MA 5'),
                          row=1, col=1)
        
        fig.update_layout(
                title=symbol,
                xaxis_rangeslider_visible=False,
                showlegend=False)
            
        fig.update_yaxes(title_text="stock price", row=1, col=1)
        fig.update_yaxes(title_text="volumen", row=2, col=1)
        fig.update_xaxes(title_text='Date', row=2, col=1)
            
        # hide weekends without transactions
        fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])
        
        col1,col2 = st.columns([0.8, 0.2])
        
        with col1:
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("**Summary**")
            stock_now=stock.history(period='1d').reset_index()
            st.write(stock_now['Close'])
            

        
        from datetime import datetime
        import time
        
        
        ##Current price
        #print(datetime.now())
        #display(stock.history(period='1d'))
        #time.sleep(60)
        #print(datetime.now())
        #display(stock.history(period='1d'))
        
        #Major stakeholders
        stock.institutional_holders
        stock.mutualfund_holders
        
    else:
        st.write("please enter a valid stock symbol")
