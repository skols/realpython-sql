# JOINing data from multiple tables

# import the sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # create a dictionary of queries
    sql = {
        "average": "SELECT AVG(population) FROM population",
        "maximum": "SELECT MAX(population) FROM population",
        "minimum": "SELECT MIN(population) FROM population",
        "sum": "SELECT SUM(population) FROM population",
        "count": "SELECT COUNT(city) FROM population",
    }

    # run each sql query item in the dictionary
    for keys, values in sql.items():

        # run sql
        c.execute(values)

        # fetchone() retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print(keys + ": ", result[0])
