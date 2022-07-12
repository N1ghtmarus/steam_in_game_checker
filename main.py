import requests
from datetime import datetime as dt
from jsonschema import validate
from notification import notification
import os
from dotenv import load_dotenv


load_dotenv()
SECRET_API_KEY = os.getenv('SECRET_KEY')

steam_user_id = '' # account id

api_url = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key='+str(SECRET_API_KEY)+'&steamids='+steam_user_id+''


# returning full JSON steam api
def api_request(url):
    result = requests.get(url)
    data = result.json()
    return data


def run_api_script():
    while True:
        now = dt.now()
        current_time = now.strftime("%S")
        if int(current_time) % 10 == 0:
            try:
                if not (validate(instance=api_request(api_url))):
                    print('In the game')
                    notification()
            except Exception:
                print('Not in the game, waiting ...')


if __name__ == '__main__':
    run_api_script()
