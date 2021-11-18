# 1) Create a SQLlite database called mysqldb01
# Using Sqlite DB Browser create a table called books
# Bookid Text
# Booktitle Text
# Bookcateg Text
# Bookprice Numeric
# 1.1 Write a Python scrip that writes 3 records into the table books
# Input the values for each field from the console (input())
# 1.2 Once, the records are inserted in the table, write code to read the records and display
# them on screen

import sqlite3
import os

os.chdir('./Python 2')
conn = sqlite3.connect('mysqldb01.db');
conn.row_factory = sqlite3.Row; #This will return the row as a dictionary (key:value) instead of a tuple
cur = conn.cursor();

cur.execute('SELECT count(*) from books');
rowCount = cur.fetchone()[0];
    
for x in range(3):
    rowCount += 1;
    bookId = int(rowCount);
    bookTitle = str(input('Please enter the title of the book. '));
    bookCateg = str(input('What genre is the book? '));
    bookPrice = float(input('How much does the book cost? '));
    
    cur.execute('INSERT INTO books VALUES (?,?,?,?)', [bookId, bookTitle, bookCateg, bookPrice]);
    conn.commit(); 

cur.execute('SELECT * FROM books');
rows = cur.fetchall();
for row in rows:
    print("Book ID:", row['bookid'], "- Title:", row['booktitle'], "- Category:", row['bookcateg'], "- Price:", row['bookprice'])
    
conn.close();