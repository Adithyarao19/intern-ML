import streamlit as st
import pandas as pd

st.title('🤖 ML app')

st.info('This app builds ML model!')
with st.expander('Data'):
  st.write('Raw data**')
  df = pd.read_csv('penguins_cleaned (1).csv')
  
