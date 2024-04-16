#!/usr/bin/python3
"""
 script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.

"""


import sys
import MySQLdb


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY\
            '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
