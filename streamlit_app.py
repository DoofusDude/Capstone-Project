# Import necessary packages and functions
import streamlit as st
import pandas as pd
import numpy as np
# import pickle

# Load the trained model
model = pickle.load(open('model.pkl','rb'))

# Set Page configuration
st.set_page_config(page_title='Job Predictor', page_icon='🌷', layout='wide', initial_sidebar_state='expanded')

# Import necessary packages and functions
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('model.pkl','rb'))

# Set Page configuration
st.set_page_config(page_title='Job Predictor', page_icon='🌷', layout='wide', initial_sidebar_state='expanded')

# Add a title to the app
st.title('Data Engineer :male-technologist: Data Analyst :technologist:')

# Set input widgets in main section
st.subheader('Select your skill set')
r1 = st.radio("excel", ('Yes', 'No'))
r2 = st.radio("sql", ('Yes', 'No'))
r3 = st.radio("microsoft", ('Yes', 'No'))
r4 = st.radio("tableau", ('Yes', 'No'))
r5 = st.radio("python", ('Yes', 'No'))
r6 = st.radio("machine learning", ('Yes', 'No'))
r7 = st.radio("powerpoint", ('Yes', 'No'))
r8 = st.radio("looker", ('Yes', 'No'))
r9 = st.radio("azure", ('Yes', 'No'))
r10 = st.radio("ai", ('Yes', 'No'))
r11 = st.radio("scrum", ('Yes', 'No'))
r12 = st.radio("shell", ('Yes', 'No'))
r13 = st.radio("linux", ('Yes', 'No'))
r14 = st.radio("sharepoint", ('Yes', 'No'))
r15 = st.radio("devops", ('Yes', 'No'))
r16 = st.radio("mysql", ('Yes', 'No'))
r17 = st.radio("git", ('Yes', 'No'))
r18 = st.radio("vba", ('Yes', 'No'))
r19 = st.radio("java", ('Yes', 'No'))
r20 = st.radio("pandas", ('Yes', 'No'))
r21 = st.radio("scala", ('Yes', 'No'))
r22 = st.radio("css", ('Yes', 'No'))
r23 = st.radio("postgres", ('Yes', 'No'))
r24 = st.radio("power bi", ('Yes', 'No'))
r25 = st.radio("data analysis", ('Yes', 'No'))
r26 = st.radio("statistics", ('Yes', 'No'))
r27 = st.radio("business intelligence", ('Yes', 'No'))


        
# Use the trained model to make a prediction
if st.button('Predict'):
    # Preprocess the user input
    skill_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27]
    skill_list = [1 if skill == 'Yes' else 0 for skill in skill_list]

    # Make the prediction
    prediction = model.predict([skill_list])
    
    # Display the results to the user
    st.write(f'The predicted job category is: {prediction}')
        
