import streamlit as st
import pandas as pd

st.title('🤖 ML app')

st.info('This app builds ML model!')
with st.expander('Data'):
  st.write('Raw data**')
  df = pd.read_csv('https://github.com/Adithyarao19/intern-ML/blob/master/penguins_cleaned%20(1).csv')
  
