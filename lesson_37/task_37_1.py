# Create a table of your choice inside the sample SQLite database, rename it, and add a new column.
# Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.
# As a solution to this task, create a file named: task1.sql,
# with all the SQL statements you have used to accomplish this task

import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE example_table (date text, main text, price real)''')
# cursor.execute('''INSERT INTO example_table VALUES ('2015-12-31', 'some important data', 345.234)''')
# cursor.execute('''INSERT INTO example_table VALUES ('2017-12-31', 'not some important data', 379.234)''')
# cursor.execute('''UPDATE example_table SET main='very important data' WHERE date='2016-12-31' ''')
# cursor.execute('''DELETE FROM  example_table WHERE main='very important data2' ''')
# cursor.execute('''ALTER TABLE example_table ADD id int ''')
# cursor.execute('''INSERT INTO example_table VALUES ('2019-12-31', 'not some important data', 379.234, 001)''')
# cursor.execute('''UPDATE example_table SET id='002' WHERE date='2015-12-31' ''')
conn.commit()