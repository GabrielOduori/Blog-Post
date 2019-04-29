import os

class Config:
    # SECRET_KEY=os.environ.get('SECRET_KEY')
    SECRET_KEY='Ghdks87PlsxCvTx'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/bloglist'

    

    
class ProdConfig(Config):
    pass
    

class DevConfig(Config):
    DEBUG = True
        
        
        
config_options = { 
    'development' : DevConfig,
    'production' : ProdConfig
}