from flask import Blueprint, request, jsonify
from user.model import User
from tweet.model import Tweet
from following.model import Following
from db import db
import jwt
import os

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/', methods=['GET'])
def get_user_profile():
    authorization_header = request.headers.get('Authorization')
    token = authorization_header.split(' ')[1]
    payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])

    user_id = payload["user_id"]
    user = User.query.get(user_id)

    if not user:
        return {"error": "User not found!"}, 404
    
    follower_count = Following.query.filter_by(following_user_id=user_id).count()
    following_count = Following.query.filter_by(user_id=user_id).count()
    
    tweets = [
        {
            "id": tweet.id,
            "tweet": tweet.tweet,
            "publish_at": tweet.publish_at,
        }
        for tweet in Tweet.query.filter_by(user_id=user_id).order_by(Tweet.publish_at.desc()).limit(10).all()
    ]
    
    return {
        "id": user.id,
        "username": user.username,
        "bio": user.bio,
        "followers": follower_count,
        "following": following_count,
        "tweet": tweets
    }
