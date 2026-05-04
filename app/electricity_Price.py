import requests
import json

URL = "https://api.porssisahko.net/v1/latest-prices.json"

def main():
    response = requests.get(URL)
    data = response.json()

    # Print raw JSON for debugging
    # print(json.dumps(data, indent=2))

    # The API returns something like:
    # { "prices": [ { "startDate": "...", "price": ... }, ... ] }

    # Detect correct key automatically
    if isinstance(data, dict):
        for key in data:
            if isinstance(data[key], list):
                data = data[key]
                break

    # Now `data` should be the list of price entries
    for entry in data:
        if isinstance(entry, dict):
            ts = entry.get("startDate") or entry.get("timestamp")
            value = entry.get("price") or entry.get("value")
            print(f"{ts}  -->  {value}")
        else:
            print("Unexpected entry:", entry)

if __name__ == "__main__":
    main()