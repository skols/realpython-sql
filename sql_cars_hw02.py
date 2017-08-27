# Cars database homework 2

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # clear table of existing data
    c.execute("DELETE FROM inventory")

    # data to be inserted
    cars = [
        ("Ford", "Focus", 45),
        ("Ford", "Explorer", 23),
        ("Ford", "Ranger", 41),
        ("Honda", "CRV", 13),
        ("Honda", "Civic", 56),
    ]

    # insert data
    c.executemany("INSERT INTO inventory VALUES (?, ?, ?)", cars)

    # update quantities
    c.execute("UPDATE inventory SET quantity=33 WHERE model='Focus'")
    c.execute("UPDATE inventory SET quantity=22 WHERE model='CRV'")

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])

    print("-" * 80)

    c.execute("SELECT * FROM inventory WHERE make='Ford'")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
