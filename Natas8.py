# webscraper for natas8
import requests
from bs4 import BeautifulSoup
import re
import base64
import binascii

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
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

def sourceRequest(): #shows 'encodedSecret";'
    session = requests.Session()
    resp2 = session.get(url+'/'+viewSource, auth=(username, password))
    content = resp2.text
    soup = BeautifulSoup(content, 'html.parser')
    SourceCode = str(soup.code)
    regex = re.findall("\w{32}", SourceCode)
    encodedSecret = str(regex)[2:34]
    print(encodedSecret)
    return encodedSecret

def decodeOperations(encodeSecret):
    operationData =bytes(encodeSecret, 'utf-8')
    firstOp = binascii.unhexlify(operationData)
    print(firstOp)
    operationData2 = str(firstOp)[2:18]
    print(operationData2)
    secondOp = operationData2[::-1]
    print(secondOp)
    thirdOp = base64.b64decode(secondOp)
    print(thirdOp)
    return thirdOp

def secretPost(): #make post with secret to obtain password
    session = requests.Session()
    resp3 = session.post(url, auth=(username, password), proxies=proxies, data={'secret':secret, 'submit':'Submit+Query'})
    content = resp3.text
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    passText=soup.find('div', id = 'content')
    print(passText.getText)


viewSource = initialRequest()
encodeSecret = sourceRequest()
secret = decodeOperations(encodeSecret)
secretPost()

