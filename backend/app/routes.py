"""Module providing routes for the demand prediction API."""
import os
from flask import Blueprint, request, jsonify
from .utils.data_procesing import load_data, clean_transform_data
from .models.prediction_model import train_model, predict

app_routes = Blueprint("app_routes", __name__)

# Define paths to store the uploaded files temporarily
SALES_PATH = os.path.join('uploads', 'VENTAS.csv')
PRICES_PATH = os.path.join('uploads', 'PRECIOS.csv')


# Endpoint for uploading sales and processing prediction
@app_routes.route('/api/upload_sales', methods=['POST'])


@app_routes.route('/api/upload_sales', methods=['POST'])
def upload_and_predict():
    """Handle uploading of sales data and perform prediction."""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    sales_file = request.files['file']
    sales_file.save(SALES_PATH)
    if not os.path.exists(PRICES_PATH):
        return jsonify({"error": "Prices file is missing"}), 500
    ventas, precios = load_data(SALES_PATH, PRICES_PATH)
    data_limpia = clean_transform_data(ventas, precios)
    model, metrics = train_model(data_limpia)
    predictions = predict(model, data_limpia.drop(columns=['CANTIDAD']))
    # Include the date and demand data in the response for plotting
    response_data = {
        "metrics": metrics,
        "predictions": predictions.tolist(),
    } 
    return jsonify(response_data)
