# 1) Using the beautifulsoup module, write a program that does the following:
# Open the URL www.meteomedia.com
# Find how many <a> tags are there in the html code
# Print all href links inside the <a> tags.

import urllib.request as ur;
from bs4 import BeautifulSoup;

res = ur.urlopen('http://www.meteomedia.com');
html = res.read().decode();
parsedHtml = BeautifulSoup(html, 'html.parser');

aTags = parsedHtml('a');

for tag in aTags:
    print(tag.get('href', "None"));
