import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'efgnmrt454ytjhmgfwefgn'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://flask-app:flask@flask.xv7avzt.mongodb.net/?retryWrites=true&w=majority&appName=flask'
