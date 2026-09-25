import numpy as np
import joblib
import streamlit as st

obj = joblib.load('california.joblib') #it is dict
model = obj['model']
cols = obj['columns']
#-------------------------------------
st.title('california app')
In=[]
for i in cols:
   v=st.number_input(f'Enter {i} value:')
   In.append(v)

if st.button('click'):
   out=model.predict([In])
   st.success(f'The Median House value is:{out}')