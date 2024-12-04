import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)


class followers(Base):
   __tablename__= "followers"
   id = Column(Integer, primary_key=True)
   from_id = Column(Integer, ForeignKey("users.id"))
   from_user = Column(Integer, ForeignKey("users.id"))
   to_id = relationship("Users", foreign_keys=[from_id], backref="follorwer")
   to_user = relationship("Users", foreign_keys=[from_id], backref="follorwing")


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_Text = Column(String(500), unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("Users", backref="comments")
    post_id = Column(Integer, ForeignKey("posts.id"))
    users = relationship("Posts", backref="comments")

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("Users", backref="posts")

class Medias(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('imagen', 'video', 'audio', name='media_types'), nullable=False)
    url = Column(String(500), unique=True, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    users = relationship("Posts", backref="medias")

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
