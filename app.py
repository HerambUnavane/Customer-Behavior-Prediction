import streamlit as st
import pandas as pd
import pickle  # or joblib if you used that for your model

# Load the trained classification model (replace 'model.pkl' with your model's filename)
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the Streamlit app
st.title('Customer Behaviour Prediction')

st.write("""
This app predicts customer behaviour based on various features such as Age, Tenure, Usage Frequency, etc.
""")

# Input features
age = st.number_input('Age', min_value=18, max_value=100, value=30)
gender = st.selectbox('Gender', options=['Male', 'Female'])
tenure = st.number_input('Tenure (months)', min_value=0, max_value=240, value=12)
usage_frequency = st.number_input('Usage Frequency', min_value=0, max_value=100, value=10)
support_calls = st.number_input('Support Calls', min_value=0, max_value=50, value=5)
payment_delay = st.number_input('Payment Delay (days)', min_value=0, max_value=365, value=0)
subscription_type = st.selectbox('Subscription Type', options=['Basic', 'Standard', 'Premium'])
contract_length = st.selectbox('Contract Length', options=['Monthly', 'Quarterly'])
total_spend = st.number_input('Total Spend ($)', min_value=0.0, value=100.0)
last_interaction = st.number_input('Days Since Last Interaction', min_value=0, max_value=365, value=30)

# Encode categorical inputs
gender_male_encoded = 1 if gender == 'Male' else 0
contract_length_monthly = 1 if contract_length == 'Monthly' else 0
contract_length_quarterly = 1 if contract_length == 'Quarterly' else 0
subscription_type_basic = 1 if subscription_type == 'Basic' else 0
subscription_type_standard = 1 if subscription_type == 'Standard' else 0

# Create a dataframe for prediction with the correct features
input_data = pd.DataFrame({
    'Age': [age],
    'Tenure': [tenure],
    'Usage Frequency': [usage_frequency],
    'Support Calls': [support_calls],
    'Payment Delay': [payment_delay],
    'Total Spend': [total_spend],
    'Last Interaction': [last_interaction],
    'Gender_Male': [gender_male_encoded],
    'Contract Length_Monthly': [contract_length_monthly],
    'Contract Length_Quarterly': [contract_length_quarterly],
    'Subscription Type_Basic': [subscription_type_basic],
    'Subscription Type_Standard': [subscription_type_standard]
})

# Add a submit button
if st.button('Submit'):
    # Predict churn
    prediction = model.predict(input_data)[0]

    # Convert the output to "Yes" or "No"
    churn_prediction = "Yes" if prediction == 1 else "No"

    # Display prediction
    st.write(f'The predicted customer churn is: {churn_prediction}')
