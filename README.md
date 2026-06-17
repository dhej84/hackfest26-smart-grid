

---

# ⚡ Smart Grid AI: Demand Prediction & Optimization

An AI-based smart grid simulation system that predicts electricity demand using Machine Learning and optimizes power distribution using rule-based logic. The system demonstrates how data-driven intelligence can improve energy allocation efficiency in a multi-zone electrical grid.

---

## 🚀 Features

* 📊 Synthetic smart grid dataset generation
* 🤖 Demand prediction using Random Forest ML model
* ⚙️ Rule-based optimization engine for power allocation
* ⚡ Overload detection system
* 🌍 Multi-zone simulation (Zone A, Zone B, Zone C)
* 📈 Model evaluation using MAE and R² score
* 💾 Model persistence using Joblib

---

## 🏗️ System Flow

### 1. 📊 Data Generation

* Creates synthetic electricity demand dataset
* Simulates real-world load variations (peak, normal, low demand)
* Generates multi-zone grid data

⬇️

### 2. 🤖 Machine Learning Model

* Uses Random Forest Regressor
* Learns demand patterns from historical data
* Predicts future electricity demand per zone

⬇️

### 3. ⚙️ Optimization Engine

* Compares predicted demand vs available supply
* Allocates power efficiently across zones
* Ensures balanced and fair distribution

Rules:

* If demand ≤ supply → normal allocation
* If demand > supply → proportional redistribution
* If overload → trigger warning state

⬇️

### 4. ⚡ Overload Detection

* Detects critical load conditions in real time
* Flags zones as:

  * 🟢 Stable
  * 🟡 Warning
  * 🔴 Critical
* Prevents cascading grid failure

⬇️

### 5. 📊 Output Layer

* Displays final power allocation
* Shows predicted vs actual demand
* Provides grid status summary

---

## 📊 Model Performance

The ML model is evaluated using:

* 📉 Mean Absolute Error (MAE) → prediction accuracy
* 📈 R² Score → model goodness of fit

These metrics validate how well the system learns electricity demand behavior.

---

## ⚙️ Optimization Logic

The system follows rule-based decision logic:

* Demand ≤ Supply → allocate normally
* Demand > Supply → redistribute load
* Overload → trigger warning system
* Maintain stability across all zones

---

## ⚡ Overload Handling

* Detects overloaded zones instantly
* Redistributes excess load to stable zones
* Prevents grid instability
* Maintains balanced power distribution

---

## 📦 Installation

```bash
git clone https://github.com/dhej84/hackfest26-smart-grid.git
cd hackfest26-smart-grid
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 1️⃣ Train ML Model

```bash
python smart_grid_model.py
```

### 2️⃣ Run Optimization Engine

```bash
python optimization.py
```

### 3️⃣ Start Flask App

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoints

### 📌 `/predict`

Returns predicted demand for all zones

### 📌 `/optimize`

Runs optimization and returns allocation results

### 📌 `/status`

Returns grid health status

---

## 📂 Project Structure

```
smart-grid-ai/
│
├── app.py
├── optimization.py
├── smart_grid_model.py
├── smart_grid_model.pkl
├── data.csv
├── dashboard_updated.html
├── templates/
├── static/
└── README.md
```

---

## 📈 Output Example

```json
{
  "Zone_A": {
    "demand": 120,
    "allocated": 110,
    "status": "Warning"
  },
  "Zone_B": {
    "demand": 90,
    "allocated": 90,
    "status": "Stable"
  },
  "Zone_C": {
    "demand": 150,
    "allocated": 130,
    "status": "Critical"
  }
}
```

---

## 💡 Future Enhancements

* 🔋 Reinforcement Learning-based optimization
* 🌦️ Weather-based demand prediction integration
* 📡 Real-time IoT sensor simulation
* 📊 Interactive dashboard (React frontend upgrade)
* ⚡ Dynamic pricing model for energy distribution

---

## 🧠 Idea Behind the Project

This project simulates how modern smart grids can:

* predict electricity demand using AI
* optimize distribution dynamically
* prevent overload failures
* improve energy efficiency across regions

---

