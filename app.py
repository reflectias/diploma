from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


"""app = Flask(__name__)
@app.route("/")
def hello():
    #html = "<H1> Hello!!! </H1>"
    return 'Hello, World!'

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
    #app.run(debug=True)"""

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://reflectias:P@ssw0rd123@db:3306/my_data"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

if __name__ == "__main__":
    app.run(debug=True)
