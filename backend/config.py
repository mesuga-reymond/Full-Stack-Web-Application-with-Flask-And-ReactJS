from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLACHEMY_TRACK_MODIFICATIONS=config('SQLACHEMY_TRACK_MODIFICATIONS', cast=bool)


class DevConfig(Config):
    SQLACHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,'dev.db')
    DEBUG=True
    SQLALCHEMY_ECHO=True


class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass
