from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input(' Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

spans = soup('span')

s = list()
numsum = 0
count = 0
for sp in spans:
    sp = str(sp)
    nums = re.findall('([0-9]+)', sp)
    if len(nums) <= .5 : continue
    for n in nums:
        ns = n.split()
        for i in ns:
            x = int(i)
        numsum = numsum + x
        count = count + 1
print('Sum:',numsum)
print('Count:',count)
