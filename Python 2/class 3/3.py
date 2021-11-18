# 3) Use the beautifulsoup module to fetch the contents from:
# www.groupce.com/python/html/thejourney.html
# Add up all the integers in the second column of the table.


import urllib.request as ur
from bs4 import BeautifulSoup

res = ur.urlopen('http://www.groupce.com/python/html/thejourney.html')
html = res.read().decode()
parsedHtml = BeautifulSoup(html, 'html.parser')

trTags = parsedHtml('tr')

trSum = 0
for trTag in trTags:
    tdTag = trTag('td')
    value = int(tdTag[1].contents[0])
    trSum += value

print('The sum of all the cell values is {}'.format(trSum))
