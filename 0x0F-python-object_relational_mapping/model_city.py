#!/usr/bin/python3

"""
    Contains class definition of a city and an instance
    Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """Represents a city class of a state in the database"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    state = relationship("State")
