import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    # SECRET_KEY='Ghdks87PlsxCvTx'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/bloglist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    
class ProdConfig(Config):
    pass
    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/bloglist_test'

class DevConfig(Config):
    DEBUG = True
        
        
        
config_options = { 
    'development' : DevConfig,
    'production' : ProdConfig,
    'test':TestConfig
}