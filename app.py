from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

client = MongoClient(app.config['MONGO_URI'])
db = client['todo_db']  

jwt = JWTManager(app)

from routes import *
from auth import *

if __name__ == "__main__":
    app.run(debug=True)
