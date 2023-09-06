from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username= db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
    
class Followers(db.Model):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    f_username = db.Column(db.String(120), unique=True, nullable=False)
    f_name = db.Column(db.String(250), nullable=False)
    f_lastname = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return '<Followers %r>' % self.f_username

    def serialize(self):
        return {
            "id": self.id,
            "f_name": self.f_name,
            "f_lastname":self.f_lastname
            # do not serialize the password, its a security breach
        }

class  Media(db.Model):
     __tablename__='media'
     id=db.Column(db.Integer, primary_key=True)
     post_id=db.Column(db.String(450), db.ForeignKey('post.id'))
     type=db.Column(db.Enum("picture","video",name="post_type"), nullable=False)
     description=db.Column(db.String(350))
     publicattion_date=db.Column(db.DateTime, nullable=False)
     author_id=db.Column(db.Integer, db.Foreignkey('user.id'),nullable=False)
     def __repr__(self):

        return '<Media %r>' % self.id

     def serialize(self):
        return {
            "id": self.id,
            "post_id":self.post_id,
            "type":self.type,
            "description": self.description,
            "publicattion_date":self. publicattion_date,
            "author_id":self.author_id
            # do not serialize the password, its a security breach
        }
class Post(db.Model):
 __tablename__='post'
id = db.Column(db.Integer, primary_key=True)
type=db.Column(db.Enum("picture","video",name="post_types"),nullable=False)
description=db.Column(db.String(350))
publicattion_date=db.Column(db.DateTime, nullable=False)
author_id=db.Column(db.Integer, db.Foreignkey('user.id'),nullable=False)
def __repr__(self):

        return '<Post %r>' % self.id

def serialize(self):
        return {
            "id": self.id,
            "type":self.type,
            "description": self.description,
            "publicattion_date":self. publicattion_date,
            "author_id":self.author_id
            # do not serialize the password, its a security breach
        }
class Comments(db.Model):
  __tablename__='comments'
id = db.Column(db.Integer, primary_key=True)
text=db.Column(db.String(350), nullable=False)
post_id=db.Column(db.Integer, db.Foreignkey('post.id'),nullable=False)
publicattion_date=db.Column(db.DateTime, nullable=False)
author_id=db.Column(db.Integer, db.Foreignkey('user.id'),nullable=False)
def __repr__(self):

        return '<Comments %r>' % self.id

def serialize(self):
        return {
            "id": self.id,
            "text":self.text,
            "post_id": self.post_id,
            "publicattion_date":self. publicattion_date,
            "author_id":self.author_id
            # do not serialize the password, its a security breach
        }