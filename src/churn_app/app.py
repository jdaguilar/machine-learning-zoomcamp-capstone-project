# app.py
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from preprocessing import preprocess_input

app = Flask(__name__)

# Load the trained model
with open('model/churn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    preprocessed_data = preprocess_input(data)
    prediction = model.predict(preprocessed_data)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)