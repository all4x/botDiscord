 
import requests
from bs4 import BeautifulSoup


def cfg_config_csgo():

    state_url = ('https://prosettings.net/players/s1mple')
    page = requests.get(state_url)
    print(page.status_code)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.center-container') 


    print(indicadors)

    cfg_config_csgo()
