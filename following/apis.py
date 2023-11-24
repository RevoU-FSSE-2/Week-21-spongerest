from flask import Blueprint, request, jsonify
from db import db
from user.model import User
from following.model import Following
import jwt, os

following_blueprint = Blueprint('following', __name__)

@following_blueprint.route('/', methods=['POST'])
def follow_unfollow():
    authorization_header = request.headers.get('Authorization')

    if not authorization_header or 'Bearer ' not in authorization_header:
        return {"error": "Invalid Authorization header format"}, 401

    token = authorization_header.split(' ')[1]

    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}, 401
    except jwt.InvalidTokenError:
        return {"error": "Token is not valid"}, 401

    user_id = payload["user_id"]

    data = request.get_json()
    following_user_id = data.get("following_user_id")

    if following_user_id == user_id:
        return {"error_message": "Follow the others!"}, 400

    user = User.query.get(user_id)
    following_user = User.query.get(following_user_id)

    if not user or not following_user:
        return {"error": "User not found"}, 404

    following_relation = Following.query.filter_by(user_id=user_id, following_user_id=following_user_id).first()

    if following_relation:
        # Unfollow
        db.session.delete(following_relation)
        user.following -= 1
        following_user.followers -= 1
        db.session.commit()
        return {"following_status": "unfollow"}

    # Follow
    new_following_relation = Following(user_id=user_id, following_user_id=following_user_id)
    db.session.add(new_following_relation)
    user.following += 1
    following_user.followers += 1
    db.session.commit()
    return {"following_status": "follow"}
