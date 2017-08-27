# INSERT command with Error handler

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populationd VALUES ('New York City', \
                   'NY', 8400000)")
    cursor.execute("INSERT INTO populationd VALUES ('San Francisco', \
                   'CA', 800000)")

    # commit the changes
    conn.commit()
except sqlite3.OperationalError as error:
    print("Oops! Something went wrong. Try again...")
    raise  # Gives the python stacktrace error message

# close the database connection
conn.close()
