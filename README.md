VehicleVision – Used Car Price Prediction
Project Overview

VehicleVision is a machine learning web application that predicts the resale price of used cars based on multiple vehicle attributes. The project showcases an end-to-end machine learning pipeline, from data preprocessing and feature engineering to model deployment using Flask.

This project was developed as part of an internship at CodeAlpha.

Problem Statement

Estimating the resale value of used cars is complex due to multiple influencing factors such as age, mileage, fuel type, ownership history, and transmission. This project aims to predict fair resale prices using historical car sales data.

Objective

Predict used car selling price

Apply regression techniques for price estimation

Handle categorical and numerical features effectively

Deploy the trained model as a web application

Dataset Description

The dataset consists of historical used car sales data.

Feature	Description
Present_Price	Current showroom price (₹ Lakhs)
Kms_Driven	Total kilometers driven
Owner	Number of previous owners
Year	Manufacturing year
Fuel_Type	Petrol / Diesel
Seller_Type	Dealer / Individual
Transmission	Manual / Automatic
Selling_Price	Target variable (₹ Lakhs)
Feature Engineering

Converted manufacturing year into car age

Dropped non-informative features

One-hot encoded categorical variables

Applied StandardScaler for normalization

Machine Learning Model

Algorithm: Linear Regression

Problem Type: Regression

Model Performance
Metric	Value
R² Score	~0.85
RMSE	~1.86 Lakhs

The model explains approximately 85% of the variance in used car prices.

Web Application

The Flask-based application allows users to:

Enter car details

Submit inputs through a form

Receive an instant resale price prediction

Project Structure
CodeAlpha_VehicleVision/
│
├── app.py
├── requirements.txt
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

Live Deployment

The project is deployed on Render:

https://codealpha-vehiclevision.onrender.com

How to Run Locally
git clone https://github.com/sm7313617-create/CodeAlpha_VehicleVision.git
cd CodeAlpha_VehicleVision
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

Key Learnings

End-to-end regression modeling

Feature engineering for structured data

Flask-based ML deployment

Frontend and backend integration

Practical experience with cloud deployment

Author

Sayan Mondal
Intern at CodeAlpha

License

This project is intended for educational and internship purposes only.