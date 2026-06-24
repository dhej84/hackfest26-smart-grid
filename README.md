⚡ Smart Grid AI: Demand Prediction & Priority-Based Power Optimization

An AI-powered smart grid simulation system that predicts electricity demand using Machine Learning and optimizes power distribution using a priority-aware rule-based allocation engine. The system demonstrates how data-driven intelligence can improve energy distribution efficiency, prevent overloads, and ensure stable grid operation across multiple zones.

🚀 Features

📊 Synthetic smart grid dataset generation simulating real-world demand patterns
🤖 Demand prediction using Random Forest Regression
⚙️ Priority-based power allocation engine
⚡ Overload detection and underserve monitoring system
🌍 Multi-zone simulation (Zone A, Zone B, Zone C)
📈 Model evaluation using MAE and R² score
💾 Model persistence using Joblib
📊 Zone-level analytics with allocation transparency

🏗️ System Flow
1. 📊 Data Generation
Synthetic dataset simulating electricity demand fluctuations
Models peak, normal, and low load conditions
Multi-zone grid structure (Zone A, B, C)

⬇️

2. 🤖 Machine Learning Model
Random Forest Regressor used for demand prediction
Learns historical demand patterns
Outputs predicted demand per zone

⬇️

3. ⚙️ Priority-Based Optimization Engine

A rule-driven allocation system that distributes available power based on zone priority:

Zone A → Highest priority
Zone B → Medium priority
Zone C → Lowest priority

Allocation Logic:

Higher priority zones are served first
Remaining supply is distributed sequentially
Ensures critical zones receive stable power first

⬇️

4. ⚡ Load Monitoring System
Detects underserved zones using threshold-based evaluation (80%)
Flags deficit conditions per zone
Computes system-wide efficiency after allocation

Zone Status Indicators:

🟢 Stable
🟡 Warning (underserved)
🔴 Critical (high deficit / overload condition)

⬇️

5. 📊 Output Analytics Layer

Provides detailed system insights:

Total demand vs supply comparison
Final allocated power per zone
Efficiency after optimization
Zone-wise served percentage
System status and alerts
⚙️ Optimization Logic

The system uses a priority-first greedy allocation strategy:

Zones are sorted by priority level
Available supply is allocated starting from highest priority zone
If demand exceeds supply, allocation is capped
Underserve detection triggers alerts when served ratio < 80%
Final system status is computed based on efficiency and overload conditions
📊 Model Performance

Evaluation metrics used:

📉 Mean Absolute Error (MAE) → prediction accuracy
📈 R² Score → model fit quality
📦 Installation
git clone https://github.com/dhej84/hackfest26-smart-grid.git
cd hackfest26-smart-grid
pip install -r requirements.txt
🚀 How to Run
1️⃣ Train ML Model
python smart_grid_model.py
2️⃣ Run Optimization Engine
python optimization.py
3️⃣ Start Flask App
python app.py

Open in browser:

http://127.0.0.1:5000
🌐 API Endpoints
📌 /predict

Returns predicted electricity demand per zone

📌 /optimize

Runs priority-based allocation engine and returns results

📌 /status

Returns overall grid health status

📂 Project Structure
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
📈 Sample Output
{
  "Zone_A": {
    "demand": 420,
    "allocated": 400,
    "served_pct": 95.2
  },
  "Zone_B": {
    "demand": 300,
    "allocated": 260,
    "served_pct": 86.7
  },
  "Zone_C": {
    "demand": 500,
    "allocated": 340,
    "served_pct": 68.0
  }
}
💡 Future Enhancements

🔋 Reinforcement Learning-based optimization engine
🌦️ Weather-based demand prediction integration
📡 Real-time IoT sensor simulation
⚡ Dynamic pricing for energy distribution
📊 Interactive dashboard upgrade (React)
🧠 Multi-objective optimization (efficiency + fairness + stability)

🧠 Idea Behind the Project

This project simulates how intelligent smart grids can:

Predict electricity demand using machine learning
Prioritize power distribution across critical zones
Prevent overload and undersupply conditions
Improve overall grid efficiency and stability

It demonstrates a hybrid AI + rule-based energy management system inspired by real-world power distribution challenges.

⚡ Built With

Python • Flask • Scikit-learn • Pandas • NumPy • Joblib • HTML/CSS • JavaScript


