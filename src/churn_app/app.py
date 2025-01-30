# app.py
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from extras.preprocessing import preprocess_input


app = Flask(__name__)

# Load the trained model
with open('src/churn_app/models/log_reg_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    preprocessed_data = preprocess_input(data)
    prediction = model.predict(preprocessed_data)
    return jsonify({'prediction': int(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)