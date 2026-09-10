from flask import Flask, request, jsonify, send_from_directory
import pickle
import pandas as pd
import os


app = Flask(__name__)


# --------------------------------------------------
# Load the trained regression model
# --------------------------------------------------

MODEL_FILE = "model.pkl"

if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError(
        "model.pkl not found. Run 01_training_and_saving_a_regression_model.ipynb first."
    )

with open(MODEL_FILE, "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# --------------------------------------------------
# Prediction API
# --------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get JSON data from frontend
        data = request.get_json()

        # Read the four input variables
        area = float(data["area"])
        bedrooms = float(data["bedrooms"])
        bathrooms = float(data["bathrooms"])
        age = float(data["age"])

        # Create DataFrame in the same order
        # used while training the model
        input_data = pd.DataFrame({
            "area": [area],
            "bedrooms": [bedrooms],
            "bathrooms": [bathrooms],
            "age": [age]
        })

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Return prediction as JSON
        return jsonify({
            "success": True,
            "prediction": round(float(prediction), 2)
        })

    except KeyError as e:

        return jsonify({
            "success": False,
            "error": f"Missing input: {str(e)}"
        }), 400

    except (TypeError, ValueError):

        return jsonify({
            "success": False,
            "error": "Please enter valid numbers."
        }), 400

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# --------------------------------------------------
# Run Flask application
# --------------------------------------------------

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
