
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cars_data = [
    {
        "brand": "Toyota",
        "model": "Proace Verso",
        "year": 2021,
        "engine_cc": 1998,
        "mileage": 42000,
        "price": 24500,
        "location": "Berlin",
        "url": "https://suchen.mobile.de/fahrzeuge/details.html?id=415751086"
    },
    {
        "brand": "Peugeot",
        "model": "5008",
        "year": 2022,
        "engine_cc": 1499,
        "mileage": 31000,
        "price": 23900,
        "location": "Munich",
        "url": "https://example.com"
    },
    {
        "brand": "Volkswagen",
        "model": "Touran",
        "year": 2021,
        "engine_cc": 1498,
        "mileage": 45000,
        "price": 22990,
        "location": "Hamburg",
        "url": "https://example.com"
    }
]

@app.route("/api/cars", methods=["GET"])
def get_cars():
    return jsonify(cars_data)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

