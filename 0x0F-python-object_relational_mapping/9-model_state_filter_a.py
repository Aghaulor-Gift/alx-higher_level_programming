#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_a = session.query(State).filter(
                State.name.like('%a%')).order_by(State.id).all()

    for state in states_a:
        print('{}: {}'.format(state.id, state.name))

    session.close()
