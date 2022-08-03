import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

"""
## Temporal trends


"""

st.sidebar.markdown("""
  - season : season (1:winter, 2:spring, 3:summer, 4:fall)
  - yr : year (0: 2011, 1:2012)
  - mnth : month ( 1 to 12)
  - holiday : whether day is holiday or not 
  - weekday : day of the week ( 0:Sunday, 6:Saturday)
  - workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
  + weathersit :
    - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
    - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog""")
    
df_hour = pd.read_csv('hour.csv')
df = pd.read_csv('day.csv')

tab1, tab2 = st.tabs(['Plot over time','Facet over time'])

with tab1:
  type_chart = st.selectbox('Select type of graph: ',['point','box','swarm','violin'],0, key = "plot_x_axis")
  cat_names = ['season','yr','mnth','holiday','weekday','workingday','weathersit']
  
  hue_facet = st.checkbox(
    'Add hue',
    False
  )
  
  row_facet = st.checkbox(
    'Facet by row',
    False
  )
  
  col_facet = st.checkbox(
    'Facet by column',
    False
  )
  
  
  if row_facet:
    row_choose = st.selectbox(
      'Select row facet: ',
      cat_names,
      0,
      key = "row_facet"
    )
  else: row_choose = None
    
  if hue_facet:
    hue_choose = st.selectbox(
      'Select hue facet: ',
      cat_names,
      0,
      key = "hue_facet"
    )
  else: hue_choose = None
    
  if col_facet:
    col_choose = st.selectbox(
      'Select column facet: ',
      cat_names,
      0,
      key = "col_facet"
    )
  else: col_choose = None
  st.pyplot(sns.catplot(data= df_hour, x = 'hr', y = 'cnt', col = col_choose, row = row_choose, hue = hue_choose, kind = type_chart, palette = 'Dark2' ))

with tab2:
  cat_names = ['season','yr','mnth','holiday','weekday','workingday','weathersit']
  type_chart = st.selectbox('Select type of graph: ',['point','box','swarm','violin'],0, key = "facet_time")
  user_cat = st.selectbox(
    'Select variable along x-axis:',
    cat_names,
    0,
    key = "facet_time"
  )
  
  hue_facet = st.checkbox(
    'Add hue',
    False,
    key = "facet_time"
  )
  
  if hue_facet:
    hue_choose = st.selectbox(
      'Select hue facet: ',
      cat_names,
      0,
      key = "facet_time"
    )
  else: hue_choose = None
    
  
  st.pyplot(sns.catplot(data= df_hour, col = 'hr',col_wrap = 3, y = 'cnt', x = user_cat, 
  hue = hue_choose, kind = type_chart, palette = 'Dark2'))






