
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import json
import os

@app.route("/api/cars", methods=["GET"])
def get_cars():
    try:
        with open("mobile_de_listings.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

