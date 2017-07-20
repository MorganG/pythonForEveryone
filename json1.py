import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

countsum = list()

while True:
    url = input('Enter JSON source: ')
    #url = 'http://py4e-data.dr-chuck.net/comments_42.json' #<- bypass input
    if len(url) < 1: break

    print('Go fetch!', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    data = html.decode()
    print('Retrieved', len(data), 'characters. Good boy!')
    js = json.loads(data)

    for n in js['comments']:
        countsum.append(int(n['count']))

    print('Sum of \'Comment\' counts:', sum(countsum))
    break
