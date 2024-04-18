#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    states = session.query(State).join(City).order_by(City.id).all()

    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
