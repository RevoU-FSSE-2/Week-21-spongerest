from flask import Blueprint, request
from db import db
from tweet.model import Tweet
from user.model import User
import jwt, os, datetime

tweet_blueprint = Blueprint('tweet',__name__)

@tweet_blueprint.route('/', methods=['POST'])
def post_tweet():
    authorization_header = request.headers.get('Authorization')
    token = authorization_header.split(' ')[1]
    payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    
    data = request.get_json()
    
    tweet = data["tweet"]
    user_id = payload.get("user_id")
    
    max_length = 150
    if len(tweet)>max_length:
        return {
            "error" : "tweet must be max length 150"
        }, 400
    
    new_tweet = Tweet(tweet=tweet, user_id=user_id)
    db.session.add(new_tweet)
    db.session.commit()
    return {
        "id" : new_tweet.id,
        "publish_at" : new_tweet.publish_at,
        "tweet": new_tweet.tweet
    }