# 📊 Telecom Customer Churn Prediction

An end-to-end machine learning project that predicts whether a telecom customer is likely to churn based on their account and service information.

## 🚀 Live Demo

👉 [Try the Telecom Churn Prediction App](https://telecom-churn-prediction-qkewlmu8guqzfotvhhv82x.streamlit.app/)

## 🎯 Project Overview

Customer churn is an important problem for telecom companies. The goal of this project is to build a machine learning model that estimates the probability that a customer will churn.

The project covers the complete machine learning workflow:

- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature preprocessing
- Model training
- Cross-validation
- Hyperparameter tuning
- Model evaluation
- Streamlit deployment
- Docker containerization

## 🤖 Models Used

The following classification models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

The final deployed application uses **Logistic Regression**.

## 📈 Model Performance

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 80.55% | 80.27% |
| Precision | 65.72% | 66.78% |
| Recall | 55.88% | 51.07% |
| F1 Score | 60.40% | 57.88% |
| ROC-AUC | 84.21% | 84.00% |

A probability threshold of **0.30** was used in the deployed application to classify customers as high churn risk.

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Docker
- Git & GitHub

## 📂 Project Structure

```text
telecom-churn-prediction/
│
├── app.py
├── telecom_churn_model.pkl
├── requirements.txt
├── runtime.txt
├── Dockerfile
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
└── README.md

🐳 Run with Docker

Build the Docker image:

docker build -t telecom-churn-app .

Run the container:

docker run -d -p 8501:8501 --name telecom-churn-container telecom-churn-app

Then open:

http://localhost:8501

🌐 Deployment

The application is deployed using Streamlit Community Cloud and is publicly accessible through the live demo link above.

📌 Note

The model identifies statistical patterns associated with customer churn. The predictions should be interpreted as model estimates rather than guaranteed outcomes.
