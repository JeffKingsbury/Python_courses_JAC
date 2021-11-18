import sqlite3
import os

os.chdir('./Python 2')
conn = sqlite3.connect('mysqldb01.db');

conn.row_factory = sqlite3.Row; #This will return the row as a dictionary (key:value) instead of a tuple

cur = conn.cursor();
cur.execute('SELECT * FROM books');


rows = cur.fetchall();

for row in rows:
    print(row['bookid'], row['booktitle'], row['bookcateg'], row['bookprice'])
    
conn.commit(); #commit is important for writing. It will make sure changes are saved before closing connection
conn.close();