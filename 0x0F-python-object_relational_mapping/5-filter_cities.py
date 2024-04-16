#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa

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
    query = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC"

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    unique_cities = set()

    for row in rows:
        city_name = row[0]
        unique_cities.add(city_name)

    print(", ".join(unique_cities))

    cur.close()
    db.close()
