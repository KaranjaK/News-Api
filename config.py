from distutils.command.config import config
from distutils.debug import DEBUG
import os

class Config:

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    CATE_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}