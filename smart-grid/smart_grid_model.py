import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# STEP 1 - Generate data
np.random.seed(42)
records = []

for hour in range(1, 501):
    for zone in ["A", "B", "C"]:
        hour_of_day = hour % 24
        temp = round(28 + 8 * np.sin((hour_of_day - 6) * np.pi / 12) + np.random.uniform(-2, 2), 1)
        renewable_supply = round(max(0, 40 + 30 * np.sin((hour_of_day - 6) * np.pi / 12) + np.random.uniform(-5, 5)), 1)
        grid_supply = round(100 + np.random.uniform(-10, 10), 1)
        zone_scale = {"A": 1.0, "B": 1.3, "C": 0.8}[zone]
        demand = round((100 + 60 * np.sin((hour_of_day - 6) * np.pi / 12) + 0.5 * temp + np.random.uniform(-10, 10)) * zone_scale, 2)
        demand = max(50, demand)
        records.append({
            "time": hour,
            "hour_of_day": hour_of_day,
            "zone": zone,
            "temp": temp,
            "renewable_supply": renewable_supply,
            "grid_supply": grid_supply,
            "demand": demand
        })

df = pd.DataFrame(records)
df.to_csv("data.csv", index=False)
print("STEP 1 DONE - data.csv created!")

# STEP 2 - Train model
df = pd.read_csv("data.csv")
df = pd.get_dummies(df, columns=["zone"], drop_first=False)

features = [
    "hour_of_day",
    "temp",
    "renewable_supply",
    "grid_supply",
    "zone_A",
    "zone_B",
    "zone_C"
]

X = df[features]
y = df["demand"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=120,
    max_depth=12,
    random_state=42
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("STEP 2 DONE - Model trained!")
print(f"MAE  : {mae:.2f}")
print(f"R2   : {r2:.3f}")

# STEP 3 - Sample predictions
print("\nSample Predictions:")
samples = [
    {"hour_of_day": 18, "temp": 33, "renewable_supply": 60, "grid_supply": 150, "zone_A": 0, "zone_B": 1, "zone_C": 0},
    {"hour_of_day": 9,  "temp": 29, "renewable_supply": 45, "grid_supply": 120, "zone_A": 1, "zone_B": 0, "zone_C": 0},
    {"hour_of_day": 22, "temp": 27, "renewable_supply": 10, "grid_supply": 130, "zone_A": 0, "zone_B": 0, "zone_C": 1},
]

for s in samples:
    sample_df = pd.DataFrame([s])
    pred = model.predict(sample_df)[0]
    status = "OVERLOAD RISK" if pred > 180 else "Normal"
    print(f"  Zone {'B' if s['zone_B'] else 'A' if s['zone_A'] else 'C'} | Hour {s['hour_of_day']} | Temp {s['temp']}C | Demand: {pred:.2f} MW | {status}")

joblib.dump(model, "smart_grid_model.pkl")
print("\nSTEP 3 DONE - Model saved!")
print("\nAll done! Your Smart Grid ML model is ready!")
