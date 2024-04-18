#!/usr/bin/python3
"""
A script that creates the State “California” with the
City “San Francisco” from the database
"""

import sys
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California", cities=[City(name="San Francisco")])
    session.add(state)
    session.commit()
    session.close()
