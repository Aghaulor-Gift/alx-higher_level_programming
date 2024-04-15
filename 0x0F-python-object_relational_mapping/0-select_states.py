#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    cur = db.cursor()

    try:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        states = cur.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        db.close()
        sys.exit(1)

    for state in states:
        print(state)

    
    cur.close()
    db.close()
