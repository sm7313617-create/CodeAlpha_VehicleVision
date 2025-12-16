from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model/car_price_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        present_price = float(data["present_price"])
        kms_driven = int(data["kms_driven"])
        year = int(data["year"])
        owner = int(data["owner"])
        
        # Calculate Car_Age from year
        car_age = 2024 - year

        fuel_diesel = 1 if data["fuel_type"] == "Diesel" else 0
        fuel_petrol = 1 if data["fuel_type"] == "Petrol" else 0
        seller_individual = 1 if data["seller_type"] == "Individual" else 0
        transmission_manual = 1 if data["transmission"] == "Manual" else 0

        features = np.array([[
            year,
            present_price,
            kms_driven,
            owner,
            car_age,
            fuel_diesel,
            fuel_petrol,
            seller_individual,
            transmission_manual
        ]])
        
        print(f"Features: {features}")
        # Scale features before prediction
        features_scaled = scaler.transform(features)
        print(f"Scaled features: {features_scaled}")
        prediction = model.predict(features_scaled)[0]
        print(f"Raw prediction: {prediction}")
        
        # Ensure prediction is non-negative
        predicted_price = max(0, float(prediction))

        return jsonify({
            "predicted_price": round(predicted_price, 2)
        })

    except Exception as e:
        import traceback
        print("ERROR:", e)
        traceback.print_exc()
        return jsonify({"error": str(e), "predicted_price": None}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
