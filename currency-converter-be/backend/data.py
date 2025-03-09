import requests
import json

url = "https://v6.exchangerate-api.com/v6/6b1594bd1198bde8e93cd5ea/latest/USD"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    conversion_rates = []
    for i, (key, value) in enumerate(data.items()):
        if key == "conversion_rates":
            for key, value in value.items():
                conversion_rates.append(f"{key}: {value}")

conversion_rates_json = json.dumps(conversion_rates, indent=4)
