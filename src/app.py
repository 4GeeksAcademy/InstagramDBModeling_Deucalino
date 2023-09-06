"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Followers,Media,Post,Comments
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    results=[]
    users=User.query.all()
    for user in users:
     results.append(user.serialize())
     return jsonify(results),200
@app.route('/followers', methods=['GET'])
def get_followers():
    results=[]
    followers=Followers.query.all()
    for followers in followers:
     results.append(followers.serialize())
     return jsonify(results),200
@app.route('/media', methods=['GET'])
def get_media():
    results=[]
    users=Media.query.all()
    for media in media:
     results.append(media.serialize())
     return jsonify(results),200
@app.route('/post', methods=['GET'])
def get_post():
    results=[]
    users=Post.query.all()
    for post in post:
     results.append(post.serialize())
     return jsonify(results),200

@app.route('/comments', methods=['GET'])
def get_comments():
    results=[]
    users=Comments.query.all()
    for comments in comments:
     results.append(comments.serialize())
     return jsonify(results),200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
