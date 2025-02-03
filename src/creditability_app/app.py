# app.py
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)

# Load the trained model
with open("src/creditability_app/models/log_reg_model.pkl", "rb") as f_in:
    dv, model = pickle.load(f_in)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()
    preprocessed_data = dv.transform(data)
    prediction = model.predict_proba(preprocessed_data)[0]
    prediction = prediction.tolist()
    y_pred = prediction[1] >= 0.6

    return jsonify({"prediction": y_pred})


if __name__ == "__main__":
    app.run(debug=True)
