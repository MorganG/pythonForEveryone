import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
rcount = input('How many pages deep?')
pcount = input('At what position?')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
t = list()
count = 0
repcount = int(rcount) - 2
poscount = int(pcount) - 1

for tag in tags:
    t.append(tag.get('href', None))

print('Starting URL:',url)
print('URL#',count+1,":", t[poscount])

while count <= repcount:
    count = count + 1
    html = urllib.request.urlopen(t[poscount], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    t = list()

    for tag in tags:
        t.append(tag.get('href', None))
    print('URL#',count+1,":", t[poscount])
