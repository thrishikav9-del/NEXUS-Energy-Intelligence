# ⚡ NEXUS: Smart Grid Intelligence & Energy Operations Center

NEXUS is an industry-grade **Time Series Forecasting and Energy Intelligence Platform** that integrates statistical modeling, deep learning, and real-time simulation to deliver advanced insights into household electricity consumption.

This project goes beyond traditional forecasting by combining **Hybrid ARIMA-LSTM architectures**, **Explainable AI (SHAP)**, and a **Digital Twin Simulation Engine** to enable intelligent energy planning, optimization, and anomaly detection.

---

##  Overview

Modern energy systems demand intelligent forecasting, adaptability, and transparency. NEXUS addresses these challenges by building a scalable, explainable, and interactive system capable of:

* Predicting energy consumption with high accuracy
* Simulating real-world grid scenarios
* Detecting anomalies and inefficiencies
* Providing actionable insights for optimization

---

##  Key Features

###  Hybrid Forecasting Engine

Combines:

* **ARIMA** → captures linear trends
* **LSTM** → captures complex non-linear dependencies

Result: Improved accuracy and robustness.

---

###  Digital Twin Simulation

Interactive environment to simulate:

* Temperature variations
* EV (Electric Vehicle) load
* Demand fluctuations

Enables “what-if” scenario analysis.

---

###  Vehicle-to-Grid (V2G) Optimization

* Simulates EV battery discharge during peak demand
* Maximizes cost efficiency and grid stability

---

###  Explainable AI (XAI)

* SHAP-based visualizations
* Interpretable model decisions

Ensures transparency for stakeholders.

---

###  Anomaly Detection System

* Uses Isolation Forest
* Detects abnormal energy usage patterns

Applications:

* Fault detection
* Energy theft identification
* Appliance malfunction alerts

---

###  Interactive Dashboard

Built using **Streamlit + Plotly**, providing:

* Real-time forecasting visualization
* Model comparison
* Simulation controls
* KPI monitoring

---

##  Models Used

| Model             | Type          | Purpose                       |
| ----------------- | ------------- | ----------------------------- |
| ARIMA             | Statistical   | Linear pattern forecasting    |
| Random Forest     | ML            | Non-linear regression         |
| LSTM              | Deep Learning | Sequential pattern learning   |
| Hybrid ARIMA-LSTM | Combined      | Enhanced forecasting accuracy |

---

##  Dataset

* Source: UCI / Kaggle Household Power Consumption Dataset
* Duration: 2006 – 2010
* Frequency: 1-minute intervals
* Size: ~2 million records

Features include:

* Global Active Power
* Voltage
* Intensity
* Sub-metering

---

##  Tech Stack

* **Languages**: Python
* **Libraries**:

  * pandas, numpy
  * scikit-learn
  * statsmodels
  * tensorflow / keras
  * shap
  * xgboost
* **Visualization**: Plotly
* **Frontend**: Streamlit

---

##  Evaluation Metrics

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)

LSTM and Hybrid models demonstrate superior performance over traditional methods.

---

##  Getting Started

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

### 4. Open in Browser

```
http://localhost:8501
```

---

##  Project Structure

```
├── tsa_proj.ipynb        # Data preprocessing & model training
├── app.py                # Streamlit dashboard
├── data/                 # Dataset files
├── models/               # Saved models
├── utils/                # Helper functions
```

---

##  Future Enhancements

* Multi-horizon forecasting (hourly, daily, weekly)
* Real-time IoT integration
* Carbon footprint estimation
* Reinforcement learning-based optimization
* Deployment on cloud (AWS / GCP)

---

## 🎯 Applications

* Smart Grid Systems
* Energy Demand Forecasting
* Home Energy Management
* Industrial Power Monitoring

---

##  Authors

* Thrishika
* Team Members

---

##  License

This project is licensed under the MIT License.

---

##  Conclusion

NEXUS represents a next-generation intelligent energy system that integrates forecasting, explainability, and optimization into a unified platform. It demonstrates the practical application of AI in building sustainable and efficient energy infrastructures.

---
