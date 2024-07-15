import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from models import db, User, Profile

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade, db downgrade
CORS(app)


@app.route('/')
def main():
    return jsonify({ "status": "API Running Successfully"}), 200


@app.route('/api/users', methods=['POST'])
def create_user():

    username = request.json.get("username")
    password = request.json.get("password")

    """ 
    user = User()
    user.username = username
    user.password = password

    db.session.add(user)
    db.session.commit()

    profile = Profile()
    profile.users_id = user.id

    db.session.add(profile)
    db.session.commit() 
    """

    user = User()
    user.username = username
    user.password = password

    profile = Profile()

    user.profile = profile
    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize_with_profile()), 201 


@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):

    #username = request.json.get("username")
    password = request.json.get("password")
    twitter = request.json.get("twitter")
    facebook = request.json.get("facebook")

    """
    user = User.query.get(id)
    profile = Profile.query.filter_by(users_id = user.id).first()

    user.password = password
    profile.twitter = twitter

    db.session.commit() 
    """

    user = User.query.get(id)
    user.password = password
    if twitter: user.profile.twitter = twitter
    if facebook: user.profile.facebook = facebook
    db.session.commit()


    return jsonify(user.serialize_with_profile()), 201 


@app.route('/api/users/<int:id>', methods=['GET'])
def get_user_by_id(id):

    user = User.query.get(id)

    return jsonify(user.serialize_with_profile()), 200


if __name__ == '__main__':
    app.run()