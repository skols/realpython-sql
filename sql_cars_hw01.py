# Cars database homework 1

# import the sqlite3 library
import sqlite3

# create a cars database if the database doesn't already exist
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create the inventory table
cursor.execute("""CREATE TABLE inventory
                (Make TEXT, Model TEXT, Quantity INT)
               """)

# close the database connection
conn.close()
