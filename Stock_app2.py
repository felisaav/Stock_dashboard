#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#------------------------------
#------import libraries--------
#------------------------------
import streamlit as st
import pandas as pd
import sqlite3
import yfinance
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
from datetime import datetime
import time

#Streamlit app
st.markdown('''
#Stock Analytics

#Select what company do you want to analyze
''')
st.title("Enter information")

stock = st.text_input('Stock symbol', 'e.g.AAPL')
interval=st.selectbox('Enter the interval of time:',
    ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'))
init = st.date_input("Enter the start date [YYYY-MM-DD]:", ) #datetime.date(2019, 7, 6)
finish=st.date_input("Enter the finish date [YYYY-MM-DD]:", )#datetime.date(2019, 7, 6)
submit_code = st.form_button("Execute")

if submit_code:
    st.write("Hello")

