import sys
import requests
from bs4 import BeautifulSoup

def cfg_csgo():

    state_url = (f'https://prosettings.net/players/{sys.argv[1]}')
    page = requests.get(state_url)
    status = page.status_code
    
    if status <= 200:    
       
        soup = BeautifulSoup(page.content, 'html.parser')
        indicadors = soup.select('.content')[0].text 
        cfg = soup.select('.download')[0].get('href')
        print(indicadors, cfg)
    
    else:
   
        print('O nome do jogador está errado, burro pra carai...')

cfg_csgo()
