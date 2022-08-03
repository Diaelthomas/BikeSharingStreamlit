### import modules

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

"""
# Welcome to Bike sharing data!
"""
st.image('https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/93e09053817167.59421b7366d44.gif')
st.header("About the dataset")
st.write("This dataset comes from the UCI Machine Learning Repository.https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset")
 
 
col1, col2 = st.columns(2)

with col1:
  """
  - instant: record index
  - dteday : date
  - season : season (1:winter, 2:spring, 3:summer, 4:fall)
  - yr : year (0: 2011, 1:2012)
  - mnth : month ( 1 to 12)
  - hr : hour (0 to 23)
  - holiday : whether day is holiday or not 
  - weekday : day of the week
  - workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
  + weathersit :
    - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
    - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
  - atemp: Normalized feeling temperature in Celsius. 
  - windspeed: Normalized wind speed. 
  - casual: count of casual users
  - registered: count of registered users
  - cnt: count of total rental bikes including both casual and registered
  
  """
  
with col2:
  df_hour = pd.read_csv('hour.csv')
  df = pd.read_csv('day.csv')
  
  info_df = pd.DataFrame( df_hour.dtypes, columns = ['data type'])
  
  info_df['Missing values'] =  df_hour.isna().sum()
  info_df['Number of unique values'] = df_hour.nunique()
  
  
  st.dataframe(data = info_df.astype(str), width = 600, height = 700)


