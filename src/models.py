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


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, nullable=False)
    


class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True, nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, nullable=False)
    likes_id = Column(Integer, ForeignKey("likes.id"), nullable=False)
    likes = relationship(Likes)
    favorites = Column(String(250), nullable=False)
    image_id = Column(Integer, ForeignKey("image.id"), nullable=False)
    image = relationship(Image)
    comments_id = Column(Integer, ForeignKey("comments.id"), nullable=False)
    comments = relationship(Comments)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), nullable=False)
    firstname = Column(Integer, nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    post_id = Column(String(250), ForeignKey("post.id"))
    post= relationship(Post)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
