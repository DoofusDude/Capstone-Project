# Import necessary packages and functions
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('model.pkl','rb'))

# Add a title to the app
st.title('Data Engineer :male-technologist: Data Analyst :technologist:')
    
# Set input widgets
st.sidebar.subheader('Select your skill set')
r1 = st.radio("Tableau", ('Yes', 'No'))
r2 = st.radio("Tableau", ('Yes', 'No'))

        
# # Use the trained model to make a prediction
# if st.button('Predict'):
#     # Preprocess the user input
#     skill_list = []
#     if r1 == 'Yes':
#         skill_list.append(1)
#     else:
#         skill_list.append(0)
    
#     # Make the prediction
#     prediction = model.predict(skill_list)
    
#     # Display the results to the user
#     st.write(f'The predicted job category is: {prediction}')
        
