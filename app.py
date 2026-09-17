import pandas as pd
import joblib

model = joblib.load("telecom_churn_model.pkl")

import streamlit as st

st.title("📊 Telecom Customer Churn Prediction")

st.write("Predict whether a telecom customer is likely to churn based on their account and service information.")

st.subheader("Customer Information")

col1, col2 = st.columns(2)

# Numerical features

with col1:
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

with col2:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

st.subheader("Phone & Internet Services")

col3, col4 = st.columns(2)

# Phone and internet services

with col3:
    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

with col4:
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

st.subheader("Contract & Billing")

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

input_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})


if st.button("Predict Churn"):

    churn_probability = model.predict_proba(input_data)[0, 1]

    Y_prediction = int(churn_probability >= 0.3)

    st.write(f"Churn Probability: {churn_probability:.2%}")

    st.progress(churn_probability)

    if Y_prediction == 1:
        st.error("⚠️ High Churn Risk")
    else:
        st.success("✅ Low Churn Risk")

    st.info(
        "The model estimates the probability that this customer will churn. "
        "A probability of 30% or higher is classified as High Churn Risk."
    )
