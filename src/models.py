import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    date = Column(String(10), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    primaryPerson = relationship('primaryPerson', backref='person', lazy=True)




class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    date = Column(String(10), nullable=False)
    primaryPost = relationship('primaryPost', backref='post', lazy=True)
    person_id = Column(Integer, ForeignKey('person.id'))


    def to_dict(self):
        return {}


class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(String(10), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))


    def to_dict(self):
        return {}


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(String(10), nullable=False)
    text = Column(String(1000), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))


    def to_dict(self):
        return {}


class Share(Base):
    __tablename__ = 'share'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(String(10), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    person_id_send = Column(Integer, ForeignKey('person.id'))
    person_id_recieve = Column(Integer, ForeignKey('person.id'))


    def to_dict(self):
        return {}


class Diect(Base):
    __tablename__ = 'direct'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(String(10), nullable=False)
    text = Column(String(1000), nullable=False)
    person_id_send = Column(Integer, ForeignKey('person.id'))
    person_id_recieve = Column(Integer, ForeignKey('person.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e