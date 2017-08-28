# Cars database homework 3

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT i.make, i.model, i.quantity, COUNT(o.order_date) AS
              total_orders FROM inventory AS i INNER JOIN orders AS o ON
              i.model=o.model GROUP BY i.make, i.model
              """)

    rows = c.fetchall()

    for r in rows:
        print("Make and Model: " + r[0] + " " + r[1])
        print("Quantity: " + str(r[2]))
        print("Total orders: " + str(r[3]))
        print("")

# SOLUTIONS FROM BOOK
# PART 1
# """Using the COUNT() function, calculate the total number of orders for each make and model."""
#
# import sqlite3
#
# with sqlite3.connect("cars.db") as connection:
#     c = connection.cursor()
#
#     # create a dictionary of sql queries
#     sql = {'Focus count'    : "SELECT count(make) FROM orders WHERE model = 'Focus'",
#             'Civic count'   : "SELECT count(make) FROM orders WHERE model = 'Civic'",
#             'Ranger count'  : "SELECT count(make) FROM orders WHERE model = 'Ranger'",
#             'Accord count'  : "SELECT count(make) FROM orders WHERE model = 'Accord'",
#             'Avenger count' : "SELECT count(make) FROM orders WHERE model = 'Avenger'",}
#
#     # run each sql query item in the dictionary
#     for keys, values in sql.items():
#
#         # run sql
#         c.execute(values)
#
#         # fetchone() retrieves one record from the query
#         result = c.fetchone()
#
#         # output the result to screen
#         print(keys + ":", result[0])

# PART 2
# """Output the car's make and model on one line, the quantity on another line,
# and then the order count on the next line. The latter is a bit difficult,
# but please try it first before looking at the code. **Remember: Google-it-first!**"""
#
# import sqlite3
#
# with sqlite3.connect("cars.db") as connection:
#     c = connection.cursor()
#
#     # retrieve data
#     c.execute("SELECT * FROM inventory")
#
#     # fetchall() retrieves all records from the query
#     rows = c.fetchall()
#
#     # output the rows to the screen, row by row
#     for r in rows:
#         # output the car make, model and quantity to screen
#         print(r[0], r[1], "\n", r[2])
#
#         # retrieve order_date for the current car make and model
#         c.execute("SELECT count(order_date) FROM orders WHERE make=? and model=?",
#                 (r[0], r[1]))
#
#         # fetchone() retrieves one record from the query
#         order_count = c.fetchone()[0]
#
#         # output the order count to the screen
#          print(order_count)
