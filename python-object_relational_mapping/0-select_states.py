#!/usr/bin/python3
''' Lists all states from the database hbtn0e0usa'''


if _name == "__main":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cr = db.cursor()
    cr.execute("SELECT * from states ORDER BY states.id")
    states = cr.fetchall()
    for state in states:
        print(state)
    cr.close()
    db.close()
