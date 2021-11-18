# 2) Use the beautifulsoup module to fetch the contents from:
# www.groupce.com/python/html/thejourney.html
# Print all <a> tags. How many are there?
# Print all <tr> tags. How many are there? (note: <tr> are tags to specify rows in an html table)
# For every <tr> tag, find all <td> tags. Print all <td> tags.
# Print the second <td> tag found in every <tr> tag .

import urllib.request as ur;
from bs4 import BeautifulSoup;

res = ur.urlopen('http://www.groupce.com/python/html/thejourney.html');
html = res.read().decode();
parsedHtml = BeautifulSoup(html, 'html.parser');

aTags = parsedHtml('a');
aTagsCount = 0;

for tags in aTags:
    print(tags);
    aTagsCount += 1;
    
trTags = parsedHtml('tr');
trTagsCount = 0;

for tags in trTags:
    print(tags);
    trTagsCount += 1;
    tdTags = tags('td');
    # For every <tr> tag, find all <td> tags. Print all <td> tags.
    for tags in tdTags:
        print(tags)
    # Print the second <td> tag found in every <tr> tag .
    print(tdTags[1])
    
    
print("There are {} <a> tags, and {} <tr> tags.".format(aTagsCount, trTagsCount))