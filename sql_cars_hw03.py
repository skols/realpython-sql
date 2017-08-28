# Cars database homework 3

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE orders")

    # create orders table
    c.execute("""CREATE TABLE orders
              (make TEXT, model TEXT, order_date DATE)
              """)

    # orders data
    orders = [
        ("Ford", "Focus", "2017-05-23"),
        ("Ford", "Focus", "2017-06-18"),
        ("Ford", "Focus", "2017-07-12"),
        ("Ford", "Explorer", "2017-04-04"),
        ("Ford", "Explorer", "2017-06-11"),
        ("Ford", "Explorer", "2017-05-31"),
        ("Ford", "Ranger", "2017-08-23"),
        ("Ford", "Ranger", "2017-08-16"),
        ("Ford", "Ranger", "2017-08-25"),
        ("Honda", "CRV", "2017-06-05"),
        ("Honda", "CRV", "2017-07-06"),
        ("Honda", "CRV", "2017-08-07"),
        ("Honda", "Civic", "2017-06-13"),
        ("Honda", "Civic", "2017-07-14"),
        ("Honda", "Civic", "2017-08-15"),
    ]

    # insert data
    c.executemany("INSERT INTO orders VALUES (?, ?, ?)", orders)

    c.execute("""SELECT i.make, i.model, i.quantity, o.order_date FROM
              inventory as i INNER JOIN orders as o ON i.model=o.model
              GROUP BY i.make, i.model, i.quantity, o.order_date ORDER BY
              i.make, i.model
              """)

    rows = c.fetchall()

    for r in rows:
        print("Make and Model: " + r[0] + " " + r[1])
        print("Quantity in stock: " + str(r[2]))
        print("Order dates: " + str(r[3]))
        print("")
