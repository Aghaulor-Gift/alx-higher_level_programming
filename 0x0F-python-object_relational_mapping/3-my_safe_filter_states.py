#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument and safe from MySQL injections!.

"""


import sys
import MySQLdb


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY\
            %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
