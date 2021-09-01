from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import json
app = Flask(__name__)
ma = Marshmallow(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'

db = SQLAlchemy(app)
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "username", "email")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True,  nullable=False)

    email = db.Column(db.String(120),unique=True, nullable=False)




@app.route("/")
def index():
    return "HOME"

@app.route("/api/",methods=['GET'])
def all_data():
    r = User.query.all()
    print(r)
    result = users_schema.dump(r)
    
    return jsonify(result)
@app.route("/api/<id>")
def user_detail(id):
    user = User.query.get(id)
    result = user_schema.dump(user)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True,port=3000)