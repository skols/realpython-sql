# import libraries
import sqlite3
import random

# establish a connection and create the "newnum.db" database
with sqlite3.connect("newnum.db") as connection:
    # open the cursor
    c = connection.cursor()

    # create a table called numbers, dropping it if it already exists
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers (num INT)")

    # use a for loop and random.randint() to insert 100 random values from
    # 0 to 100
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",
                  (random.randint(0, 100), ))
