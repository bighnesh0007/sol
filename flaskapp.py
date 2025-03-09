from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Serve the form

@app.route('/predict.html')
def perd():
    return render_template("predict.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Convert JSON to NumPy array
        features = np.array(data["features"]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]

        return jsonify({"predicted_price": float(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
