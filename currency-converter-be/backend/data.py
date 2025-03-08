import requests
import json

# URL de la API pública
url = "https://v6.exchangerate-api.com/v6/6b1594bd1198bde8e93cd5ea/latest/USD"

# Realizar la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    data = response.json()  # Convertir la respuesta en JSON
    conversion_rates = []
    for i, (key, value) in enumerate(data.items()):
        if key == "conversion_rates":
            for key, value in value.items():
                conversion_rates.append(f"{key}: {value}")
# Convertir la lista de tasas de conversión a JSON
conversion_rates_json = json.dumps(conversion_rates, indent=4)
print(conversion_rates_json)
