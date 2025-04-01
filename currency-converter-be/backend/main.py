import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

url = "https://v6.exchangerate-api.com/v6/6b1594bd1198bde8e93cd5ea/latest/USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    conversion_rates_json = data.get("conversion_rates", {})
else:
    conversion_rates_json = {}


@app.route("/", methods=["GET"])
def get_rates():
    if not conversion_rates_json:
        return jsonify({"error": "No se pudieron obtener las tasas de cambio"}), 500
    print(conversion_rates_json)
    return jsonify(conversion_rates_json)


@app.route("/convert", methods=["POST"])
def convert():
    try:
        data = request.json
        origin = data.get("origin")
        destiny = data.get("destiny")
        amount = data.get("amount")

        if not origin or not destiny or amount is None:
            return jsonify({"error": "Faltan parámetros"}), 400

        origin_rate = conversion_rates_json.get(origin)
        destiny_rate = conversion_rates_json.get(destiny)

        if origin_rate is None or destiny_rate is None:
            return jsonify({"error": "Moneda no encontrada"}), 400

        origin_rate = float(origin_rate)
        destiny_rate = float(destiny_rate)
        amount = float(amount)

        rate = destiny_rate / origin_rate
        result = amount * rate
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
# https://ufidelitas-my.sharepoint.com/personal/gmairena10835_ufide_ac_cr/_layouts/15/stream.aspx?id=%2Fpersonal%2Fgmairena10835%5Fufide%5Fac%5Fcr%2FDocuments%2FGrabaciones%2FReuni%C3%B3n%20con%20MAIRENA%20GRANERA%20GABRIEL%20JOSUE%2D20250311%5F174933%2DGrabaci%C3%B3n%20de%20la%20reuni%C3%B3n%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E435552e2%2D8d96%2D4a44%2Da565%2D7670e2055baa
