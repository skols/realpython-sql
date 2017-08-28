# Cars database homework 3

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1] + "\n" + str(r[2]))

        c.execute("SELECT COUNT(order_date) FROM orders WHERE make=?\
                  AND model=?", (r[0], r[1]))

        # Need [0] to only get the result, otherwise get a tuple
        order_count = c.fetchone()[0]

        print(order_count)
