#!/usr/bin/python3

"""
    Contains class definition of a city and an instance
    Base = declaclarative_base

"""


from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
        Define the City attributies with id, state_id and name
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
