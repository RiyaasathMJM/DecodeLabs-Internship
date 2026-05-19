"""
DecodeLabs - Project 2: Sri Lanka Property Price Predictor
Flask Backend API
"""

from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import pickle
import os
import re

app = Flask(__name__)

# ============================================
# Load Model and Configuration
# ============================================

MODEL_PATH = 'models/price_predictor.pkl'
CONFIG_PATH = 'models/feature_config.pkl'

# Check if model exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model not found at {MODEL_PATH}. "
        "Please run the notebook first to generate the model."
    )

# Load model
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

# Load feature config
feature_config = joblib.load(CONFIG_PATH)
feature_cols = feature_config['feature_cols']
categorical_features = feature_config['categorical_features']
numerical_features = feature_config['numerical_features']

print(f"✅ Model loaded: {feature_config['model_name']}")
print(f"✅ Features: {len(feature_cols)}")


# ============================================
# Helper Functions
# ============================================

def predict_price(input_data):
    """Predict property price from user input"""

    # Build complete feature dictionary
    complete_data = {}

    for col in feature_cols:
        if col in input_data and input_data[col] not in [None, '', 'Select']:
            # Try to convert to float for numerical features
            if col in numerical_features:
                try:
                    complete_data[col] = float(input_data[col])
                except (ValueError, TypeError):
                    complete_data[col] = 0
            else:
                complete_data[col] = str(input_data[col])
        elif col in numerical_features:
            complete_data[col] = 0
        else:
            complete_data[col] = 'Unknown'

    # Create DataFrame
    input_df = pd.DataFrame([complete_data])

    # Predict (model returns log price)
    log_pred = model.predict(input_df[feature_cols])[0]
    price = np.expm1(log_pred)

    return max(0, price)


# ============================================
# API Routes
# ============================================

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    """API endpoint for price prediction"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400

        # Predict price
        predicted_price = predict_price(data)

        # Format the response
        return jsonify({
            'success': True,
            'price': round(predicted_price, 2),
            'price_formatted': f"LKR {predicted_price:,.2f}",
            'price_millions': f"LKR {predicted_price / 1_000_000:,.2f} Million",
            'currency': 'LKR'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/locations', methods=['GET'])
def get_locations():
    """Return list of available locations"""
    # Top locations from the dataset
    locations = [
        'Colombo', 'Kandy', 'Galle', 'Negombo', 'Kurunegala',
        'Matara', 'Jaffna', 'Anuradhapura', 'Ratnapura', 'Batticaloa',
        'Kalutara', 'Gampaha', 'Nugegoda', 'Mount Lavinia', 'Dehiwala',
        'Moratuwa', 'Panadura', 'Ja-Ela', 'Wattala', 'Kelaniya'
    ]
    return jsonify({'locations': locations})


@app.route('/api/property-types', methods=['GET'])
def get_property_types():
    """Return list of property types"""
    types = ['House', 'Land', 'Apartment', 'Commercial', 'Villa', 'Bungalow']
    return jsonify({'types': types})


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model': feature_config['model_name'],
        'features': len(feature_cols)
    })


# ============================================
# Error Handlers
# ============================================

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500


# ============================================
# Run Application
# ============================================

if __name__ == '__main__':
    print("""
    ╔══════════════════════════════════════════════╗
    ║  🏠 Sri Lanka Property Price Predictor       ║
    ║  DecodeLabs - Project 2                      ║
    ║  Model: Random Forest Regressor              ║
    ║  Status: 🟢 Running                          ║
    ║  URL: http://127.0.0.1:5000                  ║
    ╚══════════════════════════════════════════════╝
    """)
    app.run(debug=True, host='127.0.0.1', port=5000)