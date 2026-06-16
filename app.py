from models.db import db
from config.config import DATABASE_CONNECTION_URI
from flask import Flask

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


if __name__=="__main__":
    app.run(debug=True)