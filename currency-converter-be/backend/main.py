import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = "exchange_rates.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            currency_code TEXT PRIMARY KEY,
            rate REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def fetch_rates_from_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT currency_code, rate FROM exchange_rates")
    rates = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    return rates

@app.route("/", methods=["GET"])
def get_rates():
    try:
        rates = fetch_rates_from_db()
        if not rates:
            return jsonify({"error": "No se encontraron tasas de cambio en la base de datos"}), 500
        return jsonify(rates)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/convert", methods=["POST"])
def convert():
    try:
        data = request.json
        origin = data.get("origin")
        destiny = data.get("destiny")
        amount = data.get("amount")

        if not origin or not destiny or amount is None:
            return jsonify({"error": "Faltan parámetros"}), 400

        rates = fetch_rates_from_db()
        origin_rate = rates.get(origin)
        destiny_rate = rates.get(destiny)

        if origin_rate is None or destiny_rate is None:
            return jsonify({"error": "Moneda no encontrada"}), 400

        rate = destiny_rate / origin_rate
        result = float(amount) * rate
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db()
    app.run(debug=True)