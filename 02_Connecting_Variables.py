import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

"""
## Connecting variables


Correlation plot


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

## Correlation Plot
cmap = sns.diverging_palette(180, 280, s=60, as_cmap=True)
fig, ax = plt.subplots(figsize=(15,10))
sns.heatmap(data = df.loc[:,['hum','windspeed','atemp','cnt']].corr(), 
               vmin = -1, vmax = 1, center=0, 
               cmap = cmap,
               annot=True, annot_kws={'size':16})
               
st.pyplot(fig)

cat_names = df.loc[:,['season','yr','mnth','holiday','weekday','workingday','weathersit']].columns.tolist()

with st.expander("Make a grouped correlation plot: "):
  user_cat = st.selectbox(
    'Select grouping variable:',
    cat_names,
    0
  )
  cmap = sns.diverging_palette(180, 280, s=60, as_cmap=True)  
  if user_cat == 'season':
    corr_per_season = df.loc[:,['hum','windspeed','atemp','cnt','season']].groupby(['season']).corr()

    the_season = df.season.unique().tolist()
    
    fig, axs = plt.subplots(1, len(the_season), figsize=(12, 6), sharex=True, sharey=True)
  
    for ix, x in enumerate(the_season):
        sns.heatmap(data = corr_per_season.loc[x],
                    vmin=-1, vmax=1, center=0,
                    cmap=cmap, cbar=False,
                    annot=True,
                    ax=axs[ix])
        axs[ix].set_title( x)                
    st.pyplot(fig)
    
  elif user_cat == 'yr':
    corr_per_yr = df.loc[:,['hum','windspeed','atemp','cnt','yr']].groupby(['yr']).corr()

    the_yr = df.yr.unique().tolist()
    
    fig, axs = plt.subplots(1, len(the_yr), figsize=(12, 6), sharey = True)
  
    for ix, x in enumerate(the_yr):
        sns.heatmap(data = corr_per_yr.loc[x],
                    vmin=-1, vmax=1, center=0,
                    cmap=cmap, cbar=False,
                    annot=True,
                    ax=axs[ix])
        axs[ix].set_title( x)                
    st.pyplot(fig)
  
  elif user_cat == 'mnth':
    corr_per_mnth = df.loc[:,['hum','windspeed','atemp','cnt','mnth']].groupby(['mnth']).corr()

    the_mnth = df.mnth.unique().tolist()
    
    fig, axs = plt.subplots(1, len(the_mnth), figsize=(24,6), sharex = True, sharey = True)
  
    for ix, x in enumerate(the_mnth):
        sns.heatmap(data = corr_per_mnth.loc[x],
                    vmin=-1, vmax=1, center=0,
                    cmap=cmap,cbar = False,
                    annot = True, annot_kws = {'rotation':'vertical'},
                    ax=axs[ix])
        axs[ix].set_title( x)                
    st.pyplot(fig)
    
  elif user_cat == 'holiday':
    corr_per_holiday = df.loc[:,['hum','windspeed','atemp','cnt','holiday']].groupby(['holiday']).corr()

    the_holiday = df.holiday.unique().tolist()
    
    fig, axs = plt.subplots(1, len(the_holiday), figsize=(12, 6), sharey = True)
  
    for ix, x in enumerate(the_holiday):
        sns.heatmap(data = corr_per_holiday.loc[x],
                    vmin=-1, vmax=1, center=0,
                    cmap=cmap, cbar=False,
                    annot=True,
                    ax=axs[ix])
        axs[ix].set_title( x)                
    st.pyplot(fig)
    
  elif user_cat == 'weekday':
    corr_per_weekday = df.loc[:,['hum','windspeed','atemp','cnt','weekday']].groupby(['weekday']).corr()

    the_weekday = df.weekday.unique().tolist()
    
    fig, axs = plt.subplots(1, len(the_weekday), figsize=(18, 6), sharey = True)
  
    for ix, x in enumerate(the_weekday):
        sns.heatmap(data = corr_per_weekday.loc[x],
                    vmin=-1, vmax=1, center=0,
                    cmap=cmap, cbar=False,
                    annot=True,
                    ax=axs[ix])
        axs[ix].set_title( x)                
    st.pyplot(fig)
    
  
  elif user_cat == 'workingday':
    corr_per_workingday = df.loc[:,['hum','windspeed','atemp','cnt','workingday']].groupby(['workingday']).corr()

    the_workingday = df.workingday.unique().tolist()
    
    fig, axs = plt.subplots(1, len(the_workingday), figsize=(12, 6), sharey = True)
  
    for ix, x in enumerate(the_workingday):
        sns.heatmap(data = corr_per_workingday.loc[x],
                    vmin=-1, vmax=1, center=0,
                    cmap=cmap, cbar=False,
                    annot=True,
                    ax=axs[ix])
        axs[ix].set_title( x)                
    st.pyplot(fig)
    
    
  else:
    corr_per_weathersit = df.loc[:,['hum','windspeed','atemp','cnt','weathersit']].groupby(['weathersit']).corr()

    the_weathersit = df.weathersit.unique().tolist()
    
    fig, axs = plt.subplots(1, len(the_weathersit), figsize=(12, 6),sharey = True)
  
    for ix, x in enumerate(the_weathersit):
        sns.heatmap(data = corr_per_weathersit.loc[x],
                    vmin=-1, vmax=1, center=0,
                    cmap=cmap, cbar=False,
                    annot=True,
                    ax=axs[ix])
        axs[ix].set_title( x)                
    st.pyplot(fig)
## Scatter plots

st.write("Choose hue and facets")

cont_names = ['atemp','hum','windspeed']

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
user_cont = st.selectbox(
  'Select x-axis variable:',
  cont_names,
  0
)

if row_facet:
  row_choose = st.selectbox(
    'Select row facet: ',
    cat_names,
    0
  )
else: row_choose = None
  
if hue_facet:
  hue_choose = st.selectbox(
    'Select hue facet: ',
    cat_names,
    0
  )
else: hue_choose = None
  
if col_facet:
  col_choose = st.selectbox(
    'Select column facet: ',
    cat_names,
    0
  )
else: col_choose = None

st.pyplot(sns.relplot(data = df, x = user_cont, y = 'cnt', hue = hue_choose, row = row_choose, col = col_choose, palette = 'Dark2'))






