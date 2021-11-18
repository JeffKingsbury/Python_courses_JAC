# 2) Write a Python script that reads all the records from the table books and serialize them into
# a file called books_01.json
# Write the file to disk and verify that it was created (see the contents on notepad, or other
# editor)

import sqlite3
import os
import json

os.chdir('./Python 2')
conn = sqlite3.connect('mysqldb01.db');
conn.row_factory = sqlite3.Row; #This will return the row as a dictionary (key:value) instead of a tuple
cur = conn.cursor();

cur.execute('SELECT * from books');
rows = cur.fetchall();

booksJson = {"books":{}};

for x in rows:
    booksJson['books'][x['bookid']] = {"title": x['booktitle'], "Genre": x['bookCateg'], "price ($)": x['bookPrice'] }
    
with open('books.json', 'w') as outfile:
    json.dump(booksJson, outfile, indent=4, separators=(',',':'));