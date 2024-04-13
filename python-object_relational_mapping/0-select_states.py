#!/usr/bin/python3
''' Lists all states from the database hbtn_0e_0_usa'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # Check if the correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        exit(1)

    # Connect to the database
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cr = db.cursor()

    # Execute the SQL query to fetch all states
    cr.execute("SELECT * from states ORDER BY states.id")
    states = cr.fetchall()

    # Print the fetched states
    for state in states:
        print(state)

    # Close the cursor and database connection
    cr.close()
    db.close()

