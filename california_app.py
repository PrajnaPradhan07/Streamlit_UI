import numpy as np
import joblib
import streamlit as st

#load the model
obj = joblib.load('california.joblib') #it is dict
model = obj['model']
cols = obj['columns']
#-------------------------------------
#streamlit
st.title('california app')
In=[]
for i in cols:
   v=st.number_input(f'Enter {i} value:')
   In.append(v)

#if st.button('click'):
#st.success(In)
#we need to convert into array because 2Dim

if st.button('click'):
   Input=np.array([In])
   #out=model.predict([In])
   out=model.predict(Input)
   st.success(f'The Median House value is:{out[0]:,.2f}')