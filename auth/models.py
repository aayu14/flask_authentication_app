from . import db
from flask_login import UserMixin





class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),nullable=False)
    username = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(80),nullable=False)
   

    def __init__(self,email,username,password):
                       self.email=email
                       self.username=username
                       self.password=password
                     