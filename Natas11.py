# webscraper for natas11
import requests
from bs4 import BeautifulSoup
import re

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
url = 'http://%s.natas.labs.overthewire.org/' % username
proxies = {
    'http': 'http://127.0.0.1:6996',
    'https': 'http://127.0.0.1:6996',
}

def initialRequest():
    session = requests.Session()
    resp = session.get(url, auth=(username, password))
    content = resp.text
    print(content)



viewSource = initialRequest()

