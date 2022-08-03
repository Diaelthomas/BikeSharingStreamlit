import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
df_hour = pd.read_csv('hour.csv')
df = pd.read_csv('day.csv')
"""
# Describing the variables

## Counts
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
    
#categorical variables

col1,col2,col3 = st.columns(3)

with col1:
  col1.write("Working day")
  st.pyplot(sns.catplot(data = df, x = 'workingday', kind = 'count', palette = 'Dark2'))

with col2:
  col2.write("Weather")
  st.pyplot(sns.catplot(data = df, x = 'weathersit', kind = 'count', palette = 'Dark2'))

with col3:
  col3.write("Holiday")
  st.pyplot(sns.catplot(data = df, x = 'holiday', kind = 'count', palette = 'Dark2'))


st.subheader("Combinations")


with st.expander("Combine variables: "):

  cat_names = df.loc[:,['season','yr','mnth','holiday','weekday','workingday','weathersit']].columns.tolist()

  user_cat = st.selectbox(
    'Select x-axis variable:',
    cat_names,
    0
  )
  g_horizontal = st.checkbox('Horizontal bar chart?')
  
  second_cat = df.loc[:,['season','yr','mnth','holiday','weekday','workingday','weathersit']].drop(columns = user_cat).columns.tolist()
  
  user_second_cat = st.selectbox(
    'Select grouping variable:',
    second_cat, 
    0
  )
  
  
  if g_horizontal:
    st.pyplot( sns.catplot(data = df, y = user_cat, kind = 'count', 
    hue = user_second_cat, palette = 'Dark2'))
  else:
    st.pyplot( sns.catplot(data = df, x = user_cat, kind = 'count', 
    hue = user_second_cat, palette = 'Dark2'))
  
#Continuous variables
st.header("Distributions") 
type_cont_chart = st.selectbox('Select type of graph: ',['ecdf','hist','violin','box'],0, key = "cont_choose")

names = ['Temperature', 'Humiditiy', 'Windspeed', 'Count'] 

cols = st.columns(len(names))
cont_names = ['atemp','hum','windspeed','cnt']

for i,row in enumerate(cont_names):
  with cols[i]:
    cols[i].write(names[i])
    if type_cont_chart == 'ecdf':
      st.pyplot(sns.displot(data = df, x = cont_names[i], kind = type_cont_chart, palette = 'Dark2'))
    elif type_cont_chart == 'hist':
      st.pyplot(sns.displot(data = df, x = cont_names[i], kind = type_cont_chart, palette = 'Dark2'))
    else:
      st.pyplot(sns.catplot(data = df, y = cont_names[i], kind = type_cont_chart, palette = 'Dark2'))


#Choose to facet by one of the categorical variables

with st.expander("Facet by a categorical variable"):
  user_cont = st.selectbox(
    'Select continuous variable:',
    cont_names,
    0
  )
  
  user_cat2 = st.selectbox(
    'Select categorical variable:',
    cat_names,
    0,
    key = "user_cat_2"
  )
  
  type_cond_chart = st.selectbox('Select type of graph: ',['ecdf','hist','point','bar','violin','box'],0)
  
  if type_cond_chart == 'ecdf':
    st.pyplot(sns.displot(data = df, x = user_cont,hue = user_cat2, kind = type_cond_chart, aspect = 1.5, palette = 'Dark2'))
  elif type_cond_chart == 'hist':
    st.pyplot(sns.displot(data = df, x = user_cont,hue = user_cat2, kind = type_cond_chart, aspect = 1.5, palette = 'Dark2'))
  else: 
    st.pyplot(sns.catplot(data = df, y = user_cont,x = user_cat2, kind = type_cond_chart, aspect = 1.5, palette = 'Dark2'))
