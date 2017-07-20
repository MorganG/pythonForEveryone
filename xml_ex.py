import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

countsum = list()


while True:
    url = input('Enter XML source: ')
    #url = 'http://py4e-data.dr-chuck.net/comments_42.xml' <- bypass input
    if len(url) < 1: break

    print('Go fetch!', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    data = html
    print('Retrieved', len(data), 'characters. Good boy!')
    #print(data.decode()) <- Shows full tree

    tree = ET.fromstring(data)
    branches = tree.findall('comments/comment')
    print('Comments:', len(branches))

    for branch in branches:
        countsum.append(int(branch.find('count').text))
        #print('Count:', branch.find('count').text) <- displays counts

    print('Sum of \'Comment\' counts:', sum(countsum))
    break
