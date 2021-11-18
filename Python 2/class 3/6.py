# 6) (BONUS Scraping exercise) Using beautifulsoup, start by fetching the contents of:
# www.groupce.com/python/html/thejourney.html
# Prompt the user for 2 numbers (ie. 2 integers) (between 1-4)
# Starting from the first html file: thejourney.html
# Find the table row corresponding to the first integer, extract its link (href)
# Follow the extracted “href” to the corresponding html page. Once in the page,
# use the second number to extract the corresponding row in the html.
# Once again follow the link (href) and find the new page. In the new page you need to
# find the title of the page. Inside the title, you will get a string containing a mathematical
# operation. Extract it and print the result of the operation (hint. Use eval() to evaluate a
# string containing some kind of algebraic operation).

import urllib.request as ur;
from bs4 import BeautifulSoup;

def parser(html):
    res = ur.urlopen(html);
    html = res.read().decode();
    return BeautifulSoup(html, 'html.parser');

parsedHtml = parser('http://www.groupce.com/python/html/thejourney.html');
choiceOne = int(input('Please enter a number between 1-4: ')) - 1;
choiceTwo = int(input('Please enter a number between 1-4: ')) - 1;
choiceName = "";
trTags = parsedHtml('tr');
choiceName = trTags[int(choiceOne)].find('td').contents[0];
href = trTags[int(choiceOne)].find('a')['href'];

parsedHtml = parser(href);


trTags = parsedHtml('tr');
href = trTags[int(choiceTwo)].find('a')['href'];

parsedHtml = parser(href);

print(eval(parsedHtml.title.contents[0].replace(choiceName + ' ', '')));

