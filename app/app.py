from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

@app.route("/")
def server_info():
    return jsonify({
        "server": "My API"
    })

@app.route("/registrarusuario", methods=["POST"])
def new_user():
    json = request.get_json()
    name = json.get("name")
    new_user = User()
    new_user.name = name
    
    db.session.add(new_user)
    db.session.commit()

    if name == "":
        return jsonify({"message_error": "Name empty"}), 400
    else:
        return jsonify({"id": new_user.id}), 200

if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0")
    db.create_all()
    db.init_app(app)

    
