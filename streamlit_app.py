# Import necessary packages and functions
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import GradientBoostingClassifier

# Load the trained model
model = GradientBoostingClassifier()
model.load('model.pkl')


# Define the Streamlit app
@st.cache
def run_app():
    # Add a title to the app
    st.title('Job Category Predictor')
    
    # Add a sidebar for user input
    with st.sidebar:
        st.subheader('Enter job description:')
        description = st.text_input('Description')
        
    # Use the trained model to make a prediction
    if st.button('Predict'):
        # Preprocess the user input
        scaler = StandardScaler()
        x = scaler.fit_transform(description)
        
        # Make the prediction
        prediction = model.predict(x)
        
        # Display the results to the user
        st.write(f'The predicted job category is: {prediction}')
        
# Run the app
run_app()
