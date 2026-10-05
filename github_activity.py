import sys

import requests


def get_user_data(name:str) -> None:

    try:
        response = requests.get(f"https://api.github.com/users/{name}/events",timeout=5)
        data = response.json()

        """
        if response.status_code == 200:
            print("Valid Username")
            print(response.text)

        else:
            print("Invalid Username")
        """


    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occured: {err}")
    finally:
        print(data)
    


if __name__ == "__main__":
    
    #get_user_data("pokeuhdaht")
    get_user_data(" ")