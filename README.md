🚗 VehicleVision – Used Car Price Prediction

VehicleVision is a machine learning–based web application that predicts the resale price of used cars based on multiple real-world factors.
The project demonstrates an end-to-end ML workflow, from data preprocessing and model training to deployment using Flask.

This project was developed as part of my internship at CodeAlpha.

🌐 Live Demo

🚀 Deployed Application:
👉 https://codealpha-vehiclevision.onrender.com

Users can enter car details and instantly get a predicted resale price.

📌 Problem Statement

Determining the fair resale price of a used car is challenging due to multiple influencing factors such as age, usage, fuel type, ownership, and transmission.

VehicleVision aims to solve this problem by:

Learning patterns from historical car sales data

Predicting the resale price using regression techniques

Providing an easy-to-use web interface for real-time predictions

🎯 What This Project Predicts

The model predicts:

Selling Price of a used car (in ₹ Lakhs)

This is a regression problem, not a classification problem.

📊 Dataset Overview

The dataset contains historical used-car sales data with the following key features:

Feature	Description
Present_Price	Current showroom price (₹ Lakhs)
Kms_Driven	Total kilometers driven
Owner	Number of previous owners
Year	Manufacturing year
Fuel_Type	Petrol / Diesel
Seller_Type	Dealer / Individual
Transmission	Manual / Automatic
Selling_Price	Target variable (₹ Lakhs)
🛠 Feature Engineering

Converted Year → Car Age

Removed non-informative features

One-hot encoded categorical variables

Applied StandardScaler to numerical features

Final features used for prediction:

Present_Price
Kms_Driven
Owner
Car_Age
Fuel_Type_Diesel
Fuel_Type_Petrol
Seller_Type_Individual
Transmission_Manual

🤖 Machine Learning Model

Algorithm: Linear Regression

Task: Regression (Price Prediction)

📈 Model Performance
Metric	Value
R² Score	0.85
RMSE	1.86 Lakhs

The model explains ~85% of the variance in used car resale prices.

🌐 Web Application (Flask)

Flask backend with /predict API

HTML + Tailwind CSS frontend

JavaScript Fetch API for predictions

Real-time ML inference

📁 Project Structure
CodeAlpha_VehicleVision/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   ├── car_price_model.pkl
│   └── scaler.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── script.js
│
├── notebooks/
│   └── vehicle_price_prediction.ipynb
│
└── data/
    └── car_data.csv

🚀 Run Locally
git clone https://github.com/sm7313617-create/CodeAlpha_VehicleVision.git
cd CodeAlpha_VehicleVision
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


Open:

http://127.0.0.1:5000

☁️ Deployment

The application is deployed on Render:

🔗 https://codealpha-vehiclevision.onrender.com

Deployment stack:

Flask

Gunicorn

Scikit-learn

Render Cloud Platform

🧠 Key Learnings

End-to-end ML pipeline

Regression modeling

Feature engineering

Flask API development

Frontend–backend integration

Cloud deployment

👤 Author

Sayan Mondal
Intern @ CodeAlpha

GitHub: https://github.com/sm7313617-create