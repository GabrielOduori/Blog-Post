from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.strong'


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    
    app = Flask(__name__)
    moment = Moment(app)
    
    #Creating app configurations
    
    app.config.from_object(config_options[config_name])
    
    
    #Initialing bootstrap
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    #Registering Blueprints
    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    from app.blogs import blogs as blogs_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    app.register_blueprint(blogs_blueprint, url_prefix = '/')

    app.config['SECRET_KEY'] = '098&8&u^secreHHstring'
    
    
    return app
    
    