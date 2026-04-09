# NEXUS: Smart Grid Intelligence and Energy Operations Center

NEXUS is an industry-grade Time Series Forecasting and Energy Intelligence Platform that integrates statistical modeling, deep learning, and real-time simulation to deliver advanced insights into household electricity consumption.

This project goes beyond traditional forecasting by combining Hybrid ARIMA-LSTM architectures, Explainable AI (SHAP), Vehicle-to-Grid (V2G) optimization, and a Digital Twin Simulation Engine to enable intelligent energy planning, anomaly detection, and operational decision-making.

---

## Overview

Modern energy systems require accuracy, adaptability, and transparency. NEXUS addresses these challenges by providing a scalable and intelligent platform capable of:

* Predicting energy consumption with high precision
* Simulating real-world grid scenarios
* Detecting anomalies and inefficiencies
* Delivering actionable optimization insights

---

## Key Features

### Hybrid Forecasting Engine

* ARIMA captures linear patterns
* LSTM captures complex non-linear dependencies

Result: Robust and accurate forecasting.

---

### Digital Twin Simulation

* Simulates temperature, EV load, and demand variations
* Enables real-time scenario analysis

---

### Vehicle-to-Grid Optimization

* Simulates EV battery discharge during peak demand
* Improves cost efficiency and grid stability

---

### Explainable AI

* SHAP-based interpretability
* Provides transparency in model predictions

---

### Anomaly Detection System

* Isolation Forest-based detection
* Identifies abnormal consumption patterns

Applications include:

* Fault detection
* Energy theft detection
* Appliance malfunction alerts

---

### Interactive Dashboard

Built using Streamlit and Plotly, providing:

* Real-time forecasting visualization
* Model comparison
* Simulation controls
* KPI monitoring

---

## Models Used

| Model             | Type             | Purpose                       |
| ----------------- | ---------------- | ----------------------------- |
| ARIMA             | Statistical      | Linear trend forecasting      |
| Random Forest     | Machine Learning | Non-linear regression         |
| LSTM              | Deep Learning    | Sequential pattern learning   |
| Hybrid ARIMA-LSTM | Combined         | Improved forecasting accuracy |

---

## Dataset

* Source: UCI / Kaggle Household Power Consumption Dataset
* Duration: 2006 to 2010
* Frequency: 1-minute intervals
* Size: approximately 2 million records

Features include:

* Global Active Power
* Voltage
* Intensity
* Sub-metering

---

## Technology Stack

* Programming Language: Python
* Libraries: pandas, numpy, scikit-learn, statsmodels, tensorflow, shap, xgboost
* Visualization: Plotly
* Frontend: Streamlit

---

## Evaluation Metrics

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

Hybrid and LSTM models demonstrate improved performance compared to traditional approaches.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/NEXUS-Energy-Intelligence.git
cd NEXUS-Energy-Intelligence
```

### 2. Install Dependencies

```bash
pip install pandas numpy scikit-learn statsmodels shap tensorflow xgboost streamlit plotly
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. View the Application

Once the server starts, open your browser and navigate to:
http://localhost:8501

---

## Project Structure

```
├── tsa_proj.ipynb        # End-to-end pipeline and model training
├── app.py                # Streamlit dashboard
├── data/                 # Dataset files
├── models/               # Saved models
├── utils/                # Helper functions
```

---

## Future Enhancements

* Multi-horizon forecasting (hourly, daily, weekly)
* Real-time IoT integration
* Carbon footprint estimation
* Reinforcement learning-based optimization
* Cloud deployment (AWS / GCP)

---

## Applications

* Smart Grid Systems
* Energy Demand Forecasting
* Home Energy Management
* Industrial Power Monitoring

---

## Authors

* Thrishika
* Team Members

---

## License

This project is licensed under the MIT License.

---

## Conclusion

NEXUS is a next-generation intelligent energy platform that integrates forecasting, explainability, and optimization into a unified system. It demonstrates scalable infrastructure readiness, transparent AI, and real-world applicability in modern smart energy systems.

---
