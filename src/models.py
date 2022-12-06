import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(250))
    password = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    planet_from = Column(String(250), ForeignKey('planet.name'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    size = Column(Integer)
    climate = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    data_added = Column(Integer)
    user_id = Column(Integer,ForeignKey('user.used_id'),primary_key=True)
    favorites_characters = Column(String(250),ForeignKey('character.name'))
    favorites_planet = Column(String(250),ForeignKey('planet.name'))
    favorites_vehicles = Column(String(250),ForeignKey('vehicle.name'))


class Vehicles(Base):
    __tablename__= 'vehicle'
    id = Column (Integer,primary_key=True)
    name = Column (String(250))
    vehicle_type = Column (String(250))
    pilot = Column(String(250), ForeignKey('character.name'))








    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
