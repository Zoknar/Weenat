from os import environ


class Config:
    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{environ.get("MYSQL_USER")}:{environ.get("MYSQL_PASSWORD")}@{environ.get("MYSQL_HOST")}/{environ.get("MYSQL_DB")}'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
