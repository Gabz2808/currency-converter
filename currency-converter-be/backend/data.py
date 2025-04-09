import requests
import sqlite3

# URL de la API
url = "https://v6.exchangerate-api.com/v6/6b1594bd1198bde8e93cd5ea/latest/USD"

DB_PATH = "exchange_rates.db"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    conversion_rates = data.get("conversion_rates", {})

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for currency_code, rate in conversion_rates.items():
        cursor.execute("""
            INSERT OR REPLACE INTO exchange_rates (currency_code, rate)
            VALUES (?, ?)
        """, (currency_code, rate))

    conn.commit()
    conn.close()

    print("Tasas de cambio insertadas correctamente en la base de datos.")
else:
    print(f"Error al obtener datos de la API: {response.status_code}")
