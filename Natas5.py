# webscraper for natas5
from bs4 import BeautifulSoup
import requests
import os

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
url = 'http://%s.natas.labs.overthewire.org' % username
uriString = ''
proxies = {
    'http': 'http://127.0.0.1:6996',
    'https': 'http://127.0.0.1:6996',
}

def initialRequest():
    session = requests.Session()
    resp = session.get(url, auth=(username, password), headers={'Cookie': 'loggedin=1'})
    content = resp.text
    soup = BeautifulSoup(content, 'html.parser')
    natasPass = soup.findAll('div')[0]
    print('give it a sec...')
    print(natasPass.getText())

initialRequest()


