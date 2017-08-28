# import sqlite3
import sqlite3

# connect to the database
conn = sqlite3.connect("newnum.db")

# create a cursor
cursor = conn.cursor()

# create prompt
prompt = """
        Select the operation that you want to perform (1-5):
        1. Average
        2. Min
        3. Max
        4. Sum
        5. Exit
    """

while True:
    # get user input
    choice = input(prompt)

    if choice in set(["1", "2", "3", "4"]):

        # parse the corresponding operation text
        operation = {
            1: "AVG",
            2: "MIN",
            3: "MAX",
            4: "SUM",
        }[int(choice)]

        # retrieve data
        cursor.execute("SELECT {}(num) FROM numbers".format(operation))

        # fetchone retrieves one record from the query
        agg = cursor.fetchone()

        print("\n" + operation + ": %f" % agg[0])

    elif choice == "5":
        print("\nExit")
        break

    else:
        print("\nInvalid entry, please enter a valid choice.")
