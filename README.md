# NEXUS

**Smart Grid Intelligence and Energy Operations Platform**

NEXUS is an energy analytics platform for forecasting household electricity consumption and supporting data-driven energy management. It integrates statistical forecasting, deep learning, explainable AI, simulation, and anomaly detection into a unified workflow for energy analysis.

---

## Overview

Accurate electricity demand forecasting is important for efficient energy management, resource planning, and smart-grid operations. Traditional forecasting approaches may capture individual patterns but can have limitations when dealing with complex and non-linear consumption behavior.

NEXUS combines multiple analytical and machine learning approaches to study electricity consumption and support intelligent energy-system analysis.

The platform integrates:

- Hybrid ARIMA-LSTM forecasting
- Explainable AI using SHAP
- Digital Twin simulation
- Vehicle-to-Grid (V2G) analysis
- Anomaly detection
- Interactive visualization and monitoring

---

## Key Capabilities

### Hybrid Forecasting

NEXUS combines statistical and deep learning approaches to model electricity consumption patterns.

- **ARIMA** captures linear and time-dependent patterns
- **LSTM** models complex non-linear temporal dependencies
- **Hybrid ARIMA-LSTM** combines both approaches for forecasting

---

### Digital Twin Simulation

The Digital Twin component provides a simulation-based environment for exploring energy-system scenarios.

It can simulate variations involving:

- Temperature
- EV load
- Electricity demand

This enables interactive scenario analysis and examination of changing energy conditions.

---

### Vehicle-to-Grid Analysis

The V2G component models EV battery discharge during periods of high demand.

It is used to explore:

- EV contribution during peak demand
- Energy-management scenarios
- Potential effects on grid stability
- Cost-related energy decisions

---

### Explainable AI

NEXUS incorporates SHAP-based explainability to provide insight into model predictions.

The explainability component helps analyze:

- Feature contributions
- Prediction behavior
- Model interpretability

This makes the forecasting workflow easier to inspect rather than treating predictions as a black box.

---

### Anomaly Detection

The platform uses **Isolation Forest** for identifying unusual electricity-consumption patterns.

Potential applications include:

- Abnormal consumption detection
- Fault detection
- Energy-theft analysis
- Appliance malfunction monitoring

---

### Interactive Dashboard

The NEXUS dashboard is built using **Streamlit** and **Plotly**.

It provides interactive capabilities for:

- Forecast visualization
- Model comparison
- Simulation controls
- KPI monitoring
- Energy-analysis workflows

---

## Models Used

| Model | Type | Purpose |
|---|---|---|
| ARIMA | Statistical | Time-series forecasting |
| Random Forest | Machine Learning | Non-linear regression |
| LSTM | Deep Learning | Sequential pattern learning |
| Hybrid ARIMA-LSTM | Combined | Integrated time-series forecasting |

---

## Dataset

NEXUS uses the **Household Power Consumption Dataset** sourced through UCI / Kaggle.

### Dataset Characteristics

- **Period:** 2006–2010
- **Frequency:** 1-minute intervals
- **Size:** Approximately 2 million records

### Key Features

- Global Active Power
- Voltage
- Intensity
- Sub-metering measurements

The dataset provides a foundation for studying household electricity-consumption patterns and developing forecasting models.

---

## Technology Stack

### Programming

- Python

### Machine Learning & Deep Learning

- Scikit-learn
- TensorFlow
- Statsmodels
- XGBoost

### Data Processing

- Pandas
- NumPy

### Explainable AI

- SHAP

### Visualization & Application

- Plotly
- Streamlit

---

## Evaluation

The forecasting models are evaluated using standard regression metrics:

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

These metrics are used to compare forecasting performance across the implemented models.

---

## System Workflow

```text
Household Power Consumption Data
                |
                v
       Data Extraction
                |
                v
     Data Preprocessing
                |
                v
      Time-Series Analysis
                |
        +-------+-------+
        |               |
        v               v
      ARIMA           LSTM
        |               |
        +-------+-------+
                |
                v
       Hybrid Forecasting
                |
        +-------+--------+----------------+
        |                |                |
        v                v                v
   SHAP Analysis   Anomaly Detection   Simulation
        |                |                |
        +----------------+----------------+
                         |
                         v
               Streamlit Dashboard
```

---

## Project Structure

```text
NEXUS-Energy-Intelligence/
│
├── app.py                  # Streamlit dashboard
├── extract.py              # Data extraction and preprocessing
├── sandbox_updater.py      # Project utility
├── tsa_proj.ipynb          # Forecasting and model development
├── README.md
├── LICENSE
└── .gitignore
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/thrishikav9-del/NEXUS-Energy-Intelligence.git
cd NEXUS-Energy-Intelligence
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install pandas numpy scikit-learn statsmodels tensorflow shap xgboost streamlit plotly
```

### 3. Run the Dashboard

```bash
streamlit run app.py
```

### 4. Open the Application

After the Streamlit server starts, open:

```text
http://localhost:8501
```

---

## Applications

NEXUS can be applied to energy-analysis scenarios such as:

- Smart-grid analytics
- Electricity demand forecasting
- Household energy management
- Energy-consumption monitoring
- Anomaly detection
- EV and V2G scenario analysis
- Industrial power monitoring

---

## Future Work

Potential extensions include:

- Multi-horizon forecasting for hourly, daily, and weekly demand
- Real-time IoT data integration
- Carbon-footprint estimation
- Reinforcement learning-based energy optimization
- Cloud-based deployment
- Expanded smart-grid simulation capabilities

---

## Project Highlights

NEXUS brings together several complementary approaches within a single energy-analysis workflow:

```text
Forecasting
    +
Deep Learning
    +
Explainable AI
    +
Anomaly Detection
    +
Digital Twin Simulation
    +
V2G Analysis
```

The project explores how these components can work together to support more interpretable and data-driven energy-system analysis.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Vullasa Thrishika**

B.Tech Artificial Intelligence  
Amrita Vishwa Vidyapeetham
