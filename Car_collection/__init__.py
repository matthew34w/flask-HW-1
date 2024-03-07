from flask import Flask

from .auth import auth
from .cars import cars

def create_app():
    app = Flask(__name__)
    


    app.register_blueprint(auth)
    app.register_blueprint(cars)
    
    return app


