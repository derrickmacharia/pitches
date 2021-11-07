from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from datetime import datetime

#Added this code to solve the Exception: Missing user_loader or request_loader.


@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))

# category table
class Category(db.Model):  
    _tablename_ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    post = db.relationship('Post', backref='category', lazy='dynamic')

    # save category

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Category {self.name}'


class Post(db.Model):
    _tablename_ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String)
    comment = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='post', lazy='dynamic')
    # save post
    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Post {self.title}'


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    post = db.relationship('Post',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter

    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer,db.ForeignKey("post.id"))