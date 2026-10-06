import sys
import requests
from datetime import datetime

def get_user_data(name:str) -> None:
    print(f"\nGetting GITHUB User Data for {name}")
    print(f"-----------------------------------")
    response = requests.get(f"https://api.github.com/users/{name}/events",timeout=5)
    if response.status_code != 200:
        print(f"An HTTP error occured: {response.status_code}")
        return
    else:
        response = requests.get(f"https://api.github.com/users/{name}/events",timeout=5)      
        data = response.json()
        for event in data:
            if event['type'] == "PushEvent":
                print(f"{name} pushed to {event['repo']['name']} at {datetime.fromisoformat(event['created_at']).date()}")

       
if __name__ == "__main__":
    
    get_user_data("pokeuhdaht")
    get_user_data("feff39f")