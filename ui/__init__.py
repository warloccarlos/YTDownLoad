from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

    from .convert import link
    
    app.register_blueprint(link, url_prefix='/')
    
    return app