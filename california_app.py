import numpy as np
import joblib
import streamlit as st

#load the model
obj = joblib.load('california.joblib') #it is dict
model = obj['model']
cols = obj['columns']
#-------------------------------------
#streamlit
st.title('🏡 ML-Based California House Price Prediction')
st.caption("Predict California Housing Prices using Machine Learning")
st.info(
    "Enter housing and demographic details below to estimate the median house value."
)

feature_labels = {
    "MedInc": "💰 Median Income",
    "HouseAge": "🏠 House Age",
    "AveRooms": "🚪 Average Rooms",
    "AveBedrms": "🛏️ Average Bedrooms",
    "Population": "👥 Population",
    "AveOccup": "🏡 Average Occupancy",
    "Latitude": "📍 Latitude",
    "Longitude": "📍 Longitude"
}

#create inputs 
st.markdown("### Enter Housing Details")
In = []

for i in cols:
    label = feature_labels.get(i, i)
    v = st.number_input(f"Enter {label}:")
    In.append(v)

if st.button("Predict House Value"):
    Input = np.array([In])
    #predict house value
    out = model.predict(Input)

    st.success(
        f"🏠 Predicted Median House Value: ${out[0]:,.2f}"
    )

#----------------------------end of code-------------------------------

old_code_for_ref="""
Old Version (kept for learning/reference)

- Used original column names
- Basic prediction UI
- Replaced with user-friendly labels and improved UI
"""
old_code="""
In=[]

for i in cols:
   v=st.number_input(f'Enter {i} value:')
   In.append(v)

#if st.button('click'):
#st.success(In)
#we need to convert into array because 2Dim

if st.button('Predict House Value'):
   Input=np.array([In])
   #out=model.predict([In])
   out=model.predict(Input)
   st.success(f'The Median House value is:{out[0]:,.2f}')

"""