import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:12345@localhost/watchlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


#   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:6720@localhost/watchlist'