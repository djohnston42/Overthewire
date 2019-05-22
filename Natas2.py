# webscraper for natas2
from bs4 import BeautifulSoup
import requests
import os

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()
resp = session.get(url, auth=(username, password))

content = resp.text

soup = BeautifulSoup(content, 'html.parser')
#print(soup.body)

el = soup.find('img')
file_location = (el['src'])
#print(file_location)
#pull out img src

def fileLocationRequest():
    resp2 = session.get(url+'/files/', auth=(username, password))
    #print(resp2.text)
    locationContent = resp2.text
    soup2 = BeautifulSoup(locationContent, 'html.parser')
    el2 = soup2.findAll('a')[6]
    print(el2['href']) #pull out href value for password file

fileLocationRequest()

