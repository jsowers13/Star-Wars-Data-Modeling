import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), nullable=False)
    firstname = Column(Integer, nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    post= relationship('post')
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, nullable=False)
    likes_id = Column(Integer, ForeignKey("likes.id"), nullable=False)
    likes = relationship('likes')
    favorites = Column(Integer, nullable=False)
    media_id = Column(Integer, ForeignKey("media.id"), nullable=False)
    media = relationship('media')
    comment_id = Column(Integer, ForeignKey("comment.id"), nullable=False)
    comment = relationship('comment')

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    post= relationship('post')
    


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    post= relationship('post')
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, nullable=False)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("user.user_id"))
    author = relationship('user')
    post_id = Column(Integer, ForeignKey("post.id"))
    post= relationship('post')

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True, nullable=False)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user = relationship('user')
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user = relationship('user')

# class Address(Base):
#     __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    # def to_dict(self):
    #     return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
