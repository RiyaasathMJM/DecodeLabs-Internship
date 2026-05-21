# 🏠 Sri Lanka Property Price Predictor

**DecodeLabs — Project 2 | Batch 2026**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)](https://scikit-learn.org/)
[![Model](https://img.shields.io/badge/Model-Random%20Forest-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

A machine learning-powered web application that predicts property prices in Sri Lanka. Built with a **Random Forest Regressor** trained on 200,000+ property advertisements scraped from ikman.lk.

---

## 📊 Overview

This project predicts real estate prices based on property features such as location, type, size, bedrooms, and bathrooms. The model achieves **86% accuracy (R² = 0.86)** in explaining price variations across Sri Lanka's property market.

### Key Features

- 🎯 **86% Prediction Accuracy** — Random Forest Regressor (R² = 0.86)
- 🌍 **20+ Sri Lankan Cities** supported
- 🏘️ **Multiple Property Types** — House, Land, Apartment, Commercial, Villa, Bungalow
- 📱 **Responsive UI** with professional dark theme
- ⚡ **Real-time Predictions** via Flask REST API
- 🧠 **Smart Form** — auto-hides irrelevant fields based on property type

---

## 🏗️ Architecture

```
project2-Land Price Prediction in SL/
│
├── 📓 notebook.ipynb           # Model development & EDA
├── 🌐 app.py                   # Flask REST API backend
├── 📄 properties.csv           # Dataset (200K+ records)
├── 📄 requirements.txt         # Python dependencies
│
├── 📁 models/                  # Trained models (generated locally)
│   ├── price_predictor.pkl
│   └── feature_config.pkl
│
├── 📁 templates/
│   └── index.html              # Web interface
│
└── 📁 static/
    ├── css/style.css           # Professional dark theme
    └── js/script.js            # Frontend logic
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git
- Jupyter Notebook

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/RiyaasathMJM/DecodeLabs-Internship.git
cd "project2-Land Price Prediction in SL"

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Train and save the model
jupyter notebook notebook.ipynb
# Run all cells — this generates models/price_predictor.pkl

# 6. Start the Flask server
python app.py

# 7. Open in browser
# http://127.0.0.1:5000
```

> ⚠️ **Note:** You must run `notebook.ipynb` first to generate the `.pkl` model files before launching the Flask app.

---

## 📚 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Backend logic |
| Flask 3.0 | Web framework & REST API |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Scikit-learn | ML pipeline & Random Forest |
| XGBoost | Gradient boosting (comparison model) |
| Joblib | Model serialization |
| HTML5 / CSS3 | Web interface |
| JavaScript | Frontend interactivity |

---

## 📁 Dataset

| Attribute | Details |
|-----------|---------|
| **Source** | [Sri Lanka Property Ads Dataset — Kaggle](https://doi.org/10.34740/KAGGLE/DS/2369689) |
| **Records** | 200,000+ advertisements |
| **Features** | 26 columns |
| **Origin** | ikman.lk property listings |
| **Coverage** | All major cities in Sri Lanka |

**Citation:**
> Oshan Mudannayake. (2022). *Sri Lanka Property Ads Dataset* [Data set]. Kaggle.
> https://doi.org/10.34740/KAGGLE/DS/2369689

---

## 🧠 ML Pipeline

```
Raw CSV Data (200K+ rows)
        │
        ▼
  Data Cleaning & EDA
  (null handling, outlier removal)
        │
        ▼
  Feature Engineering
  (encoding cities, property types)
        │
        ▼
  Model Training
  ├── Random Forest Regressor ✅ (selected)
  └── XGBoost Regressor       (comparison)
        │
        ▼
  Evaluation  →  R² = 0.86
        │
        ▼
  Model Serialization (.pkl)
        │
        ▼
  Flask REST API  →  Web UI
```

---

## 🌍 Supported Cities

Colombo, Gampaha, Kandy, Galle, Negombo, Kurunegala, Ratnapura, Anuradhapura, Matara, Jaffna, Batticaloa, Trincomalee, Badulla, Kegalle, Nuwara Eliya, Monaragala, Hambantota, Polonnaruwa, Vavuniya, Ampara, and more.

---

## 🔌 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the prediction UI |
| `POST` | `/predict` | Returns predicted price |

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "city": "Colombo",
    "property_type": "Apartment",
    "size_perches": 0,
    "size_sqft": 1200,
    "bedrooms": 3,
    "bathrooms": 2
  }'
```

### Example Response

```json
{
  "predicted_price": 28500000,
  "currency": "LKR",
  "formatted": "LKR 28.5M"
}
```

---



## 🛣️ Roadmap

- [x] Data collection & cleaning
- [x] EDA and feature engineering
- [x] Random Forest model training (R² = 0.86)
- [x] Flask REST API
- [x] Responsive dark-themed UI
- [ ] Model versioning & retraining pipeline
- [ ] Add more recent property data (2024–2025)
- [ ] Deploy to cloud (Render / Railway)

---

## 👨‍💻 Author

**Riyaasath MJM**
Built as part of the **DecodeLabs Industrial Training Program — Batch 2026**

[![GitHub](https://img.shields.io/badge/GitHub-RiyaasathMJM-black?logo=github)](https://github.com/RiyaasathMJM/DecodeLabs-Internship)

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
