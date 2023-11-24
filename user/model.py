from db import db
from following.model import Following

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(200), nullable=False)
    followers = db.Column(db.Integer, default=0)
    following = db.Column(db.Integer, default=0)
    following_relations = db.relationship('Following', back_populates='user', foreign_keys=[Following.user_id])