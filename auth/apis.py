from flask import Blueprint, request  
from common.bcrypt import bcrypt
from user.model import User
from datetime import datetime, timedelta
from db import db
import jwt
import os


auth_blp = Blueprint("auth", __name__)

@auth_blp.route('/registration', methods=['POST'])
def register():
    data = request.get_json()
    
    username = data['username']
    password = data['password']
    bio = data["bio"]
    
    user = User.query.filter_by(username=username).first()
    if user:
        return {
            "error" : "Username already in use. Please choose a different username."
        }, 400
    max_length = 20
    if len(username) > max_length:
        return {
            "error" : "Username too long. Please choose a different"
        }

    hash_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(username=username, password=hash_password, bio=bio)
    db.session.add(new_user)
    db.session.commit()
    
    return{
        "id" : new_user.id,
        "username" : new_user.username,
        "bio" : new_user.bio
    }
    
@auth_blp.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    
    username = data['username']
    password = data['password']
    
    user = User.query.filter_by(username=username).first()
    if not user:
        return {"error":"Username or Password Invalid"}, 400
    
    payload = {
        "user_id" : user.id,
        "username" : user.username,
        "exp": datetime.utcnow() + timedelta(minutes=5)
    }
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")
    
    return {
        "id" : user.id,
        "username" : user.username,
        "token" : token
    }
