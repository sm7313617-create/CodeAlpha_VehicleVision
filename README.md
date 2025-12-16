🚗 VehicleVision – Used Car Price Prediction

VehicleVision is a machine learning–based web application that predicts the resale price of used cars based on multiple real-world factors.
The project demonstrates an end-to-end ML workflow, from data preprocessing and model training to deployment using Flask.

This project was developed as part of my internship at CodeAlpha.

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

The following transformations were applied:

Year → converted to Car_Age

Car_Name → removed (non-predictive)

Categorical features → One-Hot Encoding

Numerical features → StandardScaler normalization

Final model input features:

Present_Price
Kms_Driven
Owner
Car_Age
Fuel_Type_Diesel
Fuel_Type_Petrol
Seller_Type_Individual
Transmission_Manual

🤖 Machine Learning Model

Algorithm Used: Linear Regression

Why Linear Regression?

Interpretable

Works well for price estimation

Suitable for real-world regression problems

📈 Model Performance

The model was evaluated using standard regression metrics:

R² Score: 0.85

RMSE: 1.86 Lakhs

Interpretation:

The model explains ~85% of the variance in used car resale prices

Average prediction error is around ₹1.8 Lakhs, which is reasonable for real-world pricing

🌐 Web Application (Flask)

The project includes a Flask-based web interface where users can:

Enter car details (price, age, fuel type, etc.)

Submit the form

Receive an instant resale price prediction

Backend:

Flask REST API

/predict endpoint for inference

Uses saved model and scaler

Frontend:

HTML + Tailwind CSS

JavaScript for async prediction (Fetch API)

📁 Project Structure
CodeAlpha_VehicleVision/
│
├── app.py                 # Flask backend
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
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

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/sm7313617-create/CodeAlpha_VehicleVision.git
cd CodeAlpha_VehicleVision

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py


Open browser:

http://127.0.0.1:5000

☁️ Deployment

The application is deployment-ready and can be hosted on platforms like Render using:

requirements.txt

app.py

Saved model files (.pkl)

🧠 Key Learnings

End-to-end ML project development

Feature engineering for regression

Model evaluation using R² and RMSE

Flask API development

Frontend ↔ backend integration

Real-world debugging and deployment readiness

🔮 Future Improvements

Try ensemble models (Random Forest, XGBoost)

Add confidence intervals for predictions

Improve UI with visual analytics

Add dataset expansion for better generalization

👤 Author

Sayan Mondal
Intern at CodeAlpha

GitHub: https://github.com/sm7313617-create

📜 License

This project is for educational and internship purposes.