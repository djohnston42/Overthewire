# webscraper for natas0
from bs4 import BeautifulSoup
import requests
import os

username = 'natas0'
password = 'natas0'
url = 'http://natas0.natas.labs.overthewire.org'

session = requests.Session()
resp = session.get(url, auth=(username, password))

content = resp.text

#print(content)

soup = BeautifulSoup(content, 'html.parser')
print(soup.body)
#print(soup.head)

el = soup.findAll('div')[0]
print(el)