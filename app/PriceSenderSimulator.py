import requests
import random
import time

# Replace these values with your own
SSID = "MP-IOT"
PASSWORD = "3QDaDHLn10"
BROKER_IP = "broker.emqx.io"
PORT = 1883
URL = "https://api.porssisahko.net/v1/latest-prices.json"

# Function to connect to WLAN
def connect_wlan():
    # Connecting to the group WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    # Attempt to connect once per second
    while wlan.isconnected() == False:
        print("Connecting... ")
        sleep(1)

    # Print the IP address of the Pico
    print("Connection successful. Pico IP:", wlan.ifconfig()[0])
    
def connect_mqtt():
    mqtt_client=MQTTClient("", server=BROKER_IP, port=PORT)
    mqtt_client.connect(clean_session=True)
    return mqtt_client

    


def getElectricityPrice():
    response = requests.get(URL)
    prices = response.json()

    # Try to detect list inside dict (API format may vary)
    if isinstance(prices, dict):
        # Find the first list
        for key, value in prices.items():
            if isinstance(value, list):
                prices = value
                break

    # Get current UTC hour (API timestamps are in UTC)
    now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)

    current_price = None

    for entry in prices:
        if not isinstance(entry, dict):
            continue
        
        # Detect timestamp field
        ts = entry.get("startDate") or entry.get("timestamp")
        value = entry.get("price") or entry.get("value")

        if ts is None or value is None:
            continue

        try:
            ts_dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except:
            continue

        if ts_dt == now:
            current_price = value
            break

    if current_price is not None:
        print(f"Current price ({now} UTC): {current_price}")
    else:
        print("Current hour price not found")
    return current_price

def main():
    #Connect to WLAN
    connect_wlan()
    
    # Connect to MQTT
    try:
        mqtt_client=connect_mqtt()
        
    except Exception as e:
        print(f"Failed to connect to MQTT: {e}")

    while True:
        try:
            getElectricityPrice() 
            time.sleep(2)
            try:
                topic = "pico/rajani"
                message = "Great job group 10!"
                mqtt_client.publish(topic, message)
                print(f"Sending to MQTT: {topic} -> {message}")
                time.sleep(5)
            except Exception as e:
                print(f"Failed to send MQTT message: {e}")
        except ValueError:
            print("Error in calling API ")

if __name__ == "__main__":
    main()

