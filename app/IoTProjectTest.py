import requests
import random
import time


def updateTemprature1(temp):
    url = f"https://fra1.blynk.cloud/external/api/update?token=O99InzkwHeQeZCFqDpXDp5u5BFgphLfI&V1={temp}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            apiResponse = response.json()
            print(apiResponse)
        else:
            return None
            
    except requests.exceptions.RequestException:
        return None
    
def updateTemprature2(temp):
    url = f"https://fra1.blynk.cloud/external/api/update?token=O99InzkwHeQeZCFqDpXDp5u5BFgphLfI&V2={temp}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            apiResponse = response.json()
            print(apiResponse)
        else:
            return None
            
    except requests.exceptions.RequestException:
        return None


def main():
  while True:
        try:
            temp=random.uniform(23.0, 45.0)
            print(f"Temparature is {temp} ")
            updateTemprature1(temp) 
            updateTemprature2(temp) 
            time.sleep(2)
        except ValueError:
            print("Error in calling API ")

if __name__ == "__main__":
    main()

