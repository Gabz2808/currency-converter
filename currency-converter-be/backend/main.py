from flask import Flask, request, jsonify
from flask_cors import CORS
from data import conversion_rates_json

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def get_rates():
    return conversion_rates_json


@app.route("/convert", methods=["POST"])
def convert():
    try:
        data = request.json
        origin = data.get("origin")
        destiny = data.get("destiny")
        amount = data.get("amount")

        origin_rate = float(origin_rate)
        destiny_rate = float(destiny_rate)

        rate = destiny_rate / origin_rate
        result = amount * rate

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
