⚡ Smart Grid AI: Demand Prediction & Optimization

An AI-based smart grid simulation system that predicts electricity demand using Machine Learning and optimizes power distribution using rule-based logic. The system demonstrates how data-driven intelligence can improve energy allocation efficiency.

🚀 Features
📊 Synthetic smart grid dataset generation
🤖 Demand prediction using Random Forest ML model
⚙️ Rule-based optimization engine for power allocation
⚡ Overload detection system
🌍 Multi-zone simulation (A, B, C)
📈 Model evaluation using MAE and R² score
💾 Model saved using Joblib
🏗️ System Flow
Data Generation
      ↓
ML Model Training
      ↓
Demand Prediction
      ↓
Optimization Engine
      ↓
Power Allocation Output
⚙️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
Random Forest Regressor
Joblib
📊 ML Model

Inputs:

Hour of day
Temperature
Renewable supply
Grid supply
Zone (A/B/C)

Output:

Predicted electricity demand (MW)
⚡ Optimization Logic
Prioritizes zones based on demand and importance
Uses renewable energy first
Allocates remaining grid supply efficiently
Detects overload conditions
📈 Results
MAE: ~6 MW
R² Score: ~0.97
Overload detection: Enabled
Balanced allocation across zones
🔮 Future Scope
Real-time IoT smart meter integration
Live energy data streaming
Smart city scaling
Renewable energy forecasting improvements
🧠 Project Idea

Simulates a smart grid system where AI predicts electricity demand and optimizes distribution to improve efficiency and reduce overload risks.

⚡ How to Run
pip install pandas numpy scikit-learn joblib
python ml_model.py
