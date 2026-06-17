import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from optimization import optimize_grid

app = Flask(__name__)
CORS(app)

MODEL_PATH = "smart_grid_model.pkl"
model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully")
else:
    print("Model file not found")

def predict_zone(zone, hour, temp, renewable_supply, grid_supply):
    zone_flags = {"A": [1,0,0], "B": [0,1,0], "C": [0,0,1]}
    flags = zone_flags[zone]
    sample = pd.DataFrame([{
        "hour_of_day": hour, "temp": temp,
        "renewable_supply": renewable_supply, "grid_supply": grid_supply,
        "zone_A": flags[0], "zone_B": flags[1], "zone_C": flags[2]
    }])
    return float(model.predict(sample)[0])

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        hour             = int(data.get("hour_of_day", 12))
        temp             = float(data.get("temp", 30))
        renewable_supply = float(data.get("renewable_supply", 50))
        grid_supply      = float(data.get("grid_supply", 100))
        total_supply     = renewable_supply + grid_supply
        demand_a = predict_zone("A", hour, temp, renewable_supply, grid_supply)
        demand_b = predict_zone("B", hour, temp, renewable_supply, grid_supply)
        demand_c = predict_zone("C", hour, temp, renewable_supply, grid_supply)
        optimization_result = optimize_grid(
            zone_demands={"Zone A": demand_a, "Zone B": demand_b, "Zone C": demand_c},
            available_supply=total_supply
        )
        return jsonify({
            "zone_predictions": {"Zone A": round(demand_a, 2), "Zone B": round(demand_b, 2), "Zone C": round(demand_c, 2)},
            "optimization": optimization_result
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        data         = request.json
        zone_demands = {k: float(v) for k, v in data.get("zone_demands", {}).items()}
        total_supply = float(data.get("available_supply", 500))
        result       = optimize_grid(zone_demands=zone_demands, available_supply=total_supply)
        return jsonify(result)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
