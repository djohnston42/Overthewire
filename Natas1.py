# webscraper for natas1
from bs4 import BeautifulSoup
import requests
import os

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'
url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()
resp = session.get(url, auth=(username, password))

content = resp.text

#print(content)

soup = BeautifulSoup(content, 'html.parser')
print(soup.body)
#print(soup.head)

el = soup.findAll('div')[0]
print(el)