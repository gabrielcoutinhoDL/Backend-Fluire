from datetime import timedelta
import os

class Config:
    JWT_SECRET_KEY = os.getenv('JSECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)