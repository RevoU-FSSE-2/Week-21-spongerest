from db import db
import datetime

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user=db.relationship("User",backref=db.backref('tweets', lazy=True))
    publish_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())