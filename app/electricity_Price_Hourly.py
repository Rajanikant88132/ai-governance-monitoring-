import requests
from datetime import datetime, timezone

PRICE_ENDPOINT = "https://api.porssisahko.net/v2/price.json"

# Format date to include UTC offset without microseconds
now_utc_raw = datetime.now(timezone.utc).isoformat(timespec='seconds')
# Replace +00:00 with Z for UTC, as some APIs prefer this format
now_utc_z = now_utc_raw.replace('+00:00', 'Z')

response = requests.get(f"{PRICE_ENDPOINT}?date={now_utc_z}")

# The original retry logic becomes redundant if the initial format is correct
# but keeping it for robustness in case another date format is needed.
if not response.text.strip():
    # retry with only the date (this branch might not be hit with the new format)
    date_only = now_utc_z.split("T")[0]
    response = requests.get(f"{PRICE_ENDPOINT}?date={date_only}")

# Add a check for successful response and valid JSON content
if response.ok and response.text.strip():
    try:
        data = response.json()
        price = data.get("price")
        print(f"Hinta nyt on {price}")
    except requests.exceptions.JSONDecodeError:
        print(f"Error: Could not decode JSON from response. Raw response: {response.text}")
else:
    print(f"Error: Request failed or returned empty response. Status code: {response.status_code}, Response text: {response.text}")
