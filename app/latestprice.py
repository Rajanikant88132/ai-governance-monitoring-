import requests
from datetime import datetime, timezone

PRICE_ENDPOINT = "https://api.porssisahko.net/v2/price.json"

now_utc_z = datetime.now(timezone.utc).isoformat()

response = requests.get(f"{PRICE_ENDPOINT}?date={now_utc_z}")

if not response.text.strip():
    # retry with only the date
    date_only = now_utc_z.split("T")[0]
    response = requests.get(f"{PRICE_ENDPOINT}?date={date_only}")

data = response.json()
price = data.get("price")

print(f"Hinta nyt on {price}")