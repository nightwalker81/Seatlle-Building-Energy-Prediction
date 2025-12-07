# 🏙️ Seattle Building Energy Consumption Prediction  
### Machine Learning Pipeline + BentoML API Deployment

This project was developed as part of a mission for the **City of Seattle**, which aims to reach **carbon neutrality by 2050**. The goal is to analyze non-residential buildings and **predict their total energy consumption** based on structural and operational characteristics.

Your work includes:

- Exploratory Data Analysis (EDA)  
- Machine Learning model training & evaluation  
- Feature importance identification  
- Deploying the final model as a **BentoML API**  
- Demonstrating how a citizen can enter building info and instantly get a prediction

---

# 📂 Repository Structure

```
Seattle-Building-Energy-ML/
│
├── notebook.ipynb               # EDA + model testing
├── modele_final.ipynb           # Final model training + export
│
├── service.py                   # BentoML API service (final)
├── test_request.py              # Script to test the API locally
├── bentofile.yaml               # BentoML build configuration
│
├── modele_df.csv                # Modeling dataset
├── 2016_Building_Energy_Benchmarking.csv  # Raw/unscaled dataset
│
└── final_presentation/          # Demo slides for Seattle
```

---

# 🧠 Project Overview

The City of Seattle has collected detailed building data in 2016. These measurements are expensive, so the municipality wants to **predict** energy consumption for buildings where measurements are missing.

Your project lead, Douglas, also requested a **demo API** so citizens can enter building characteristics and obtain predictions in real time.

---

# 🏗️ Architecture Overview (End-to-End)

```
                      ┌─────────────────────────┐
                      │   Raw Building Data      │
                      │  (CSV: modele_df, etc.)  │
                      └─────────────┬───────────┘
                                    │
                                    ▼
                     ┌───────────────────────────┐
                     │   Data Preparation (EDA)   │
                     │ notebook.ipynb             │
                     │ - cleaning                 │
                     │ - feature selection        │
                     │ - correlation analysis     │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │  Model Training Pipeline   │
                     │ modele_final.ipynb         │
                     │ - train/test split         │
                     │ - model comparisons        │
                     │ - save final model         │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │     BentoML Packaging      │
                     │ bentofile.yaml             │
                     │ - includes model           │
                     │ - defines service entry    │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │   API Service (BentoML)    │
                     │ service.py                 │
                     │ - validates input          │
                     │ - loads model              │
                     │ - returns prediction       │
                     └─────────────┬─────────────┘
                                   │
                             HTTP POST Request
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │      test_request.py       │
                     │  (simulates user request)  │
                     └───────────────────────────┘
```

---

# 🔍 1. Exploratory Data Analysis (EDA)

Notebook: **`notebook.ipynb`**

The EDA includes:

- Histograms & distributions of energy consumption  
- Correlation between structural features & consumption  
- Detection of outliers and anomalous building types  
- Feature selection for ML training  

### ✔ Key Insights  
(*Customize these based on your actual results*)

- Older buildings tend to consume more energy  
- Floor area is a strong predictor  
- ENERGY STAR score correlates with efficiency  
- Building use type impacts consumption  

---

# 🤖 2. Machine Learning Workflow

Notebook: **`modele_final.ipynb`**

Models tested:

- Linear Regression  
- Random Forest  
- Gradient Boosting  
- Decision Tree  
- KNN Regressor  

### ✔ Final chosen model  
*Gradient Boosting*

### ✔ Metrics evaluated  
- RMSE  
- MAE  
- R²  

---

# 🧱 Machine Learning Training Pipeline Diagram

```
            ┌────────────────────────────────────┐
            │   Raw Seattle Building Dataset      │
            │   (CSV files: modele_df, etc.)      │
            └───────────────────┬─────────────────┘
                                │
                                ▼
            ┌────────────────────────────────────┐
            │ EDA + Preprocessing                │
            │ notebook.ipynb                     │
            │ - missing values                   │
            │ - outlier detection                │
            │ - feature selection                │
            │ - encoding/scaling                 │
            └───────────────────┬─────────────────┘
                                │
                                ▼
            ┌────────────────────────────────────┐
            │ Model Training                     │
            │ modele_final.ipynb                 │
            │ - CV, tuning                       │
            │ - evaluation                       │
            └───────────────────┬─────────────────┘
                                │
                                ▼
            ┌────────────────────────────────────┐
            │ Export Best Model for BentoML       │
            └────────────────────────────────────┘
```

---

# 🌐 3. API Deployment with BentoML

Your `bentofile.yaml` defines the BentoML build:

```yaml
service: "service.py:EnergyConsumptionService"
include:
  - "service.py"
  - "test_request.py"
models:
  consommation_model:latest
```

### ✔ `service.py`  

This BentoML service:

- Loads the trained model  
- Defines a Pydantic schema  
- Validates user input  
- Returns predictions as JSON  

---

# 🌍 API Architecture Diagram

```
                 ┌──────────────────────────┐
                 │  User Input (JSON)        │
                 │  Building characteristics │
                 └───────────────┬───────────┘
                                 │ POST /predict
                                 ▼
                 ┌──────────────────────────┐
                 │ BentoML API (service.py)  │
                 │ - validate input          │
                 │ - load model              │
                 │ - predict energy usage    │
                 └───────────────┬───────────┘
                                 │
                                 ▼
                 ┌──────────────────────────┐
                 │  JSON Prediction Output   │
                 └──────────────────────────┘
```

---

# ▶️ 4. Running the API

### **1. Install BentoML**
```bash
pip install bentoml
```

### **2. Build the Bento**
```bash
bentoml build
```

### **3. Serve the API**
```bash
bentoml serve service.py:EnergyConsumptionService
```

Access the API at:

```
http://localhost:3000
```

---

# ▶️ 5. Sending a Test Request

Run the following command:

```bash
python test_request.py
```

You’ll receive a response like:

```json
{
  "predicted_energy_consumption": 384512.22
}
```

---

# 🎤 6. Presentation for Seattle Committee

Your final slides showcase:

- Seattle's carbon neutrality goals  
- EDA insights and findings  
- ML model performance metrics  
- Feature importance  
- Live API prediction demo  

Located in:  
**`final_presentation/`**

---

# 🧰 7. Skills Demonstrated

- Data Engineering + ML integration  
- Feature engineering & preprocessing  
- Model training and evaluation  
- REST API deployment with **BentoML**  
- Input validation using **Pydantic**  
- Reproducible ML pipelines  
- Professional reporting and demo creation  

---
