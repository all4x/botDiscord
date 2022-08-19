 
import requests
from bs4 import BeautifulSoup


def cfg_config_csgo(player):

    state_url = (f'https://prosettings.net/players{player}')
    page = requests.get(state_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.center-container') 


    return [ (ind.select('.name')[0].text: ind.select('.content')[0].text) for ind in indicadors ]


    cfg_config_csgo('')
