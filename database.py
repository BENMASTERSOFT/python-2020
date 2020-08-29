#####################################
# Learn Python Coding in 2020
# By Ben Mastersoft
# mastersoft.com.ng
###################################
import sqlite3
import os
from namer import nameit

os.system("clear")
################################################
# SQLite Database
###############################################

# Connect to the Database
conn = sqlite3.connect('customer.db')

# Create a Cursor
c = conn.cursor()

# Create Table
'''
c.execute("""CREATE TABLE customer (
			first_name text,
			last_name text,
			email text
			)""")
'''
# c.execute("INSERT INTO customer VALUES('Benjamin','Nwoke','benjamin@yahoo.com')")

c.execute("SELECT * FROM customer")
'''
print(c.fetchall())


print(c.fetchall()[0])

print(c.fetchall()[0][0])
'''

items =c.fetchall()

for item in items:
	print(item)
# Commit our Changes to Database
conn.commit()

# Close Database Database Connection
conn.close()