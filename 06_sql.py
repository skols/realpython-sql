# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # use a loop to iterate through the database, printing the results line
    # by line; returns tuples
    # for row in c.execute("SELECT firstname, lastname FROM employees"):
    #     print(row)

    # BETTER WAY
    c.execute("SELECT firstname, lastname FROM employees")

    # fetchall() returns all records from the query and stores as a list of
    # tuples
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1])
