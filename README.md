# ⚡ NEXUS: Smart Grid Intelligence & Energy Operations Center

NEXUS is an industry-grade Time Series Analysis project built using advanced Deep Learning and Statistical methodologies. It transcends standard forecasting by implementing **Hybrid ARIMA-LSTM** architectures alongside **Explainable AI (SHAP)**, **Vehicle-to-Grid (V2G) automation**, and an interactive **Digital Twin Simulation Engine**.

This project provides a state-of-the-art interactive dashboard allowing users to visualize predictive energy metrics and execute tariff arbitrage algorithms.

---

## 🌟 Key Features

- **🧠 Hybrid AI Forecasting Pipeline**: Sequentially pairs the linear reliability of statistical ARIMA models with the complex, non-linear pattern recognition of Long Short-Term Memory (LSTM) neural networks.
- **🎛️ Digital Twin Simulator**: Stress-test the grid in real-time by dragging sliders for ambient temperature offsets or EV capacity penetration.
- **🚗 V2G (Vehicle-to-Grid) Arbitrage**: Automates discharging EV batteries during peak pricing hours to maximize profitability and grid stability.
- **🧬 Deep Explainability (XAI)**: Utilizes SHAP values visually to demystify complex neural network logic for stakeholders.
- **🚨 Predictive IoT Diagnostics**: Heuristic anomaly detection (Isolation Forests) for connected appliances (e.g., HVAC Motor Degradation).

---

## 🚀 Getting Started (Running Locally)

To view the live Neural Engine Operations Center on your local machine, follow these steps:

### 1. Clone the Repository
```bash
git clone <your-repository-url-here>
cd Smart_Energy_Project
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Run the following command to grab all ML modules:
```bash
pip install pandas numpy scikit-learn statsmodels arch shap xgboost tensorflow streamlit plotly
```

### 3. Launch the Dashboard
Boot up the Streamlit host server by running:
```bash
streamlit run app.py
```

### 4. View the App
Once the server starts, it will provide a Local URL in your terminal. Open your internet browser and navigate to:
👉 **http://localhost:8501**

---

## 📂 Project Structure
- `tsa_proj.ipynb`: The primary Jupyter Notebook containing the end-to-end data pipeline, model training logic, Multi-horizon forecasting, and comparative analysis (RMSE bounds).
- `app.py`: The ultra-modern, glassmorphism-themed Streamlit application operating the Real-Time Ops Center.

---

*Designed to showcase scalable infrastructure readiness, ethical AI transparency, and quantitative operations research.*
