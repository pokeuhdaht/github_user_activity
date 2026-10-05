import sys

import requests


def get_user_data(name:str) -> None:

    try:
        response = requests.get(f"https://api.github.com/users/{name}/events",timeout=5)      


    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occured: {response.status_code}")
    finally:
        data = response.json()

        for event in data:
            if event["type"] == "PushEvent":
                print(f"{name} pushed to {event['repo']['name']}")
        #print(data)
    


if __name__ == "__main__":
    
    get_user_data("pokeuhdaht")
    get_user_data(" ")