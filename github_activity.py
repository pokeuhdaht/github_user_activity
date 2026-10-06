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
    
    if len(sys.argv) < 2:
        print(f"Error: Missing argument.")
        print(f"Usage: python github_activity.py <username>")
        sys.exit(1)

    username = sys.argv[1]

    get_user_data(username)