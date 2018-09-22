# -*- coding: utf-8 -*-

import requests
import re
import urllib
import base64
import sys

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
cookies = {"data": "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()
response = session.get(url, auth = (username, password), cookies = cookies )

content = response.text

orig_stdout = sys.stdout
f = open('content.html', 'w')
sys.stdout = f

print content

f.close

f = open ('cookies.txt', 'w')
sys.stdout = f

print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')

f.close
