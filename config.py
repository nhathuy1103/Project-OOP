import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:110303@localhost/data_OOP'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
