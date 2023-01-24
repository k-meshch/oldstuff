import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

totnum=0
sum=0

print('Retrieving', url)
uh=urllib.request.urlopen(url)
xml=uh.read()
print('Retrieved', len(xml), 'characters')

tree=ET.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int (count.text)
    totnum +=1

print('Count:', totnum)
print('Sum:', sum)
