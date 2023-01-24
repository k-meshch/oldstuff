# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
c = int(input('Enter count: '))
p = int (input ('Enter position: ')) -1

# Retrieve all of the anchor tags
for c0 in range(c):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    findnewurl=tags[p].get('href', None)
    url=findnewurl
    finalurl=tags[p].contents[0]
print (finalurl)
