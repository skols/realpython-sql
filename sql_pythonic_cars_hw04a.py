# Cars database homework 3

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    counts = {
        "Focus": "SELECT COUNT(order_date) FROM orders WHERE model='Focus'",
        "Explorer": "SELECT COUNT(order_date) FROM orders WHERE\
        model='Explorer'",
        "Ranger": "SELECT COUNT(order_date) FROM orders WHERE model='Ranger'",
        "CRV": "SELECT COUNT(order_date) FROM orders WHERE model='CRV'",
        "Civic": "SELECT COUNT(order_date) FROM orders WHERE model='Civic'",
    }

    for keys, values in counts.items():

        c.execute(values)

        result = c.fetchone()

        print(keys + ": ", result[0])
