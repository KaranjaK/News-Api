import os

class Config:

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apikey={}'
    NEWS_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')