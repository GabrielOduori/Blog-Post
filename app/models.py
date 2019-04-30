#Models.py file

from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin, LoginManager
from datetime import datetime
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    '''
    class for users
    '''
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String, nullable = False, default = 'default_profile_image.png')
    email = db.Column(db.String(100), unique = True, index =True)
    username = db.Column(db.String(72), unique=True,index=True)
    password_hash = db.Column(db.String(255))

    # Relationship with the Blog Post
    posts = db.relationship('Blog', backref = 'author', lazy = "dynamic")

    def __init__(self,email, username, password):
        self.email = email
        self.username =  username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
        
    def __repr__(self):
        return f"User {self.username}"

    
class Blog(db.Model):
    __tablename__ = "blogs"
    '''
    Class for blog posts
    '''
    # Relationship with the user table
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable = False)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable = False)
    
    def __init__(self,title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id
        
    def __repr__(self):
        return f"POST ID:{self.id} -- Date: {self.timestamp}"    


class Quote:
    def __init__(self,id, author, quote, permalink):
        self.id = id
        self.author = author 
        self.quote  = quote
        self.permalink =  permalink
